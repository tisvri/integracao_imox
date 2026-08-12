from __future__ import annotations

import logging
from typing import Optional, Dict, Any

import pandas as pd

from integracao.polotrial_client import PoloTrialClient
from integracao.redcap_client import RedcapClient
from integracao.sync_engine import (
    get_participant_info,
    sync_procedures,
    sync_executor
)
from integracao.config import config
from integracao.visits_catalog import VisitConfig

logger = logging.getLogger(__name__)

def sync_vnp(
    *,
    record_id: str,
    event_name: str,
    visit_config: VisitConfig,
    redcap: RedcapClient,
    polotrial: PoloTrialClient,
    protocol_nickname: str,
    repeat_instance: str | None = None,
) -> None:
    """
    Handler específico para Visita Não Programada (VNP).
    
    Diferente das outras visitas, a VNP pode ocorrer múltiplas vezes.
    Este handler:
    1. Verifica se é uma VNP já existente ou nova usando data e campos identificadores
    2. Se existente, atualiza; se nova, cria na PoloTrial
    3. Sincroniza procedimentos e executores
    
    Args:
        record_id: ID do registro no REDCap
        event_name: Nome do evento no REDCap
        visit_config: Configuração da visita
        redcap: Cliente do REDCap
        polotrial: Cliente da PoloTrial
        protocol_nickname: Apelido do protocolo
    """
    
    # 1. Get participant info from PoloTrial
    redcap_payload = redcap.export_record_eav(
        record_id,
        event_name,
        repeat_instance=repeat_instance,
    )
    
    # 2. Identificar tipo de visita e data
    # Pode ser coleta ou form_medico
    visit_type_coleta = str(redcap_payload.get("coleta_visita") or "").strip()
    visit_type_medico = str(redcap_payload.get("form_medico_visita") or "").strip()
    
    date_coleta = str(redcap_payload.get("coleta_dt_visita") or "").strip()
    date_medico = str(redcap_payload.get("form_medico_dt_visita") or "").strip()
    
    # Determinar qual campo está preenchido
    is_vnp_coleta = "não programada" in visit_type_coleta.lower()
    is_vnp_medico = "não programada" in visit_type_medico.lower()
    
    if not (is_vnp_coleta or is_vnp_medico):
        logger.warning(
            "VNP: Neither coleta_visita nor form_medico_visita indicates 'Visita não programada'. "
            "coleta_visita=%r, form_medico_visita=%r. Skipping.",
            visit_type_coleta,
            visit_type_medico
        )
        return
    
    # Usar a data apropriada
    visit_date = date_coleta if is_vnp_coleta and date_coleta else date_medico
    
    if not visit_date:
        logger.info(
            "VNP: No visit date found (coleta_dt_visita=%r, form_medico_dt_visita=%r). Skipping sync",
            date_coleta,
            date_medico
        )
        return
    
    logger.info(
        "VNP: Processing unscheduled visit for record_id=%s, visit_date=%s",
        record_id,
        visit_date
    )
    
    # 3. Get participant ID
    info = get_participant_info(
        record_id=record_id,
        redcap=redcap,
        polotrial=polotrial,
        protocol_nickname=protocol_nickname,
    )
    
    # 4. Verificar se já existe uma VNP com a mesma data
    participant_visit_id = _find_or_create_vnp(
        co_participante=info["co_participante"],
        co_protocolo=info["co_protocolo"],
        visit_date=visit_date,
        polotrial=polotrial,
    )
    
    # 5. Sync procedures
    sync_procedures(
        participante_visita_id=participant_visit_id,
        co_protocolo=info["co_protocolo"],
        procedures_map=visit_config.procedures_map,
        redcap_payload=redcap_payload,
        polotrial=polotrial,
        visit_label=visit_config.polotrial_visit_name,
    )
    
    # 6. Sync executor
    if visit_config.executor_config:
        # Load merged_procedures_df
        pvp = polotrial.list_participant_visit_procedures(
            co_participante_visita=participant_visit_id
        )
        proto_proc = polotrial.list_protocol_procedures(
            co_protocolo=info["co_protocolo"]
        )
        pvp_df = pd.DataFrame(pvp)
        proto_df = pd.DataFrame(proto_proc)[["id", "co_procedimento", "nome_procedimento_estudo"]].rename(
            columns={"id": "co_protocolo_procedimento"}
        )
        merged = pd.merge(pvp_df, proto_df, on='co_protocolo_procedimento', how='left')
        
        sync_executor(
            merged_procedures_df=merged,
            redcap_payload=redcap_payload,
            executor_field=visit_config.executor_config["field"],
            executor_date_field=visit_config.executor_config["date_field"],
            procedure_pattern=visit_config.executor_config["procedure_pattern"],
            polotrial=polotrial,
            visit_label=visit_config.polotrial_visit_name,
        )
    
    logger.info(
        "VNP: Successfully synced participant visit id=%s for record=%s. "
        "This visit was created or updated; see the creation/update log above.",
        participant_visit_id,
        record_id,
    )


def _find_or_create_vnp(
    *,
    co_participante: int,
    co_protocolo: int,
    visit_date: str,
    polotrial: PoloTrialClient,
) -> int:
    """
    Procura uma Visita Não Programada existente com a mesma data.
    Se encontrar, atualiza; se não, cria uma nova.
    
    Args:
        co_participante: Código do participante
        co_protocolo: Código do protocolo
        visit_date: Data da visita no formato YYYY-MM-DD
        polotrial: Cliente da PoloTrial
    
    Returns:
        ID da visita (co_participante_visita)
    """
    
    # Buscar todas as visitas do participante
    visits = polotrial.list_participant_visits(co_participante=co_participante)
    
    # Filtrar VNPs
    vnps = [
        v for v in visits 
        if v.get("nome_tarefa") == config.VNP_POLOTRIAL_EVENT_NAME
    ]
    
    # Verificar se já existe uma VNP com a mesma data
    target_date = str(visit_date)[:10]  # Normalizar para YYYY-MM-DD
    
    for vnp in vnps:
        existing_date = str(vnp.get("data_realizada", ""))[:10]
        
        if existing_date == target_date:
            participant_visit_id = int(vnp["id"])
            logger.info(
                "VNP: Found existing visit with matching date (id=%s, date=%s). Updating.",
                participant_visit_id,
                target_date
            )
            
            # Atualizar status se necessário
            desired = {
                "data_realizada": visit_date,
                "status": 20  # 20 = Completed (realizada)
            }
            
            current = polotrial.get_participant_visit(participant_visit_id)
            logger.info(
                "VNP: Existing visit details id=%s, co_participante=%s, "
                "co_protocolo=%s, co_tarefa=%s, nome_tarefa=%s, "
                "data_estimada=%s, data_realizada=%s, status=%s",
                participant_visit_id,
                current.get("co_participante"),
                current.get("co_protocolo"),
                current.get("co_tarefa"),
                current.get("nome_tarefa"),
                current.get("data_estimada"),
                current.get("data_realizada"),
                current.get("status"),
            )
            if (
                str(current.get("data_realizada", ""))[:10] == target_date and
                int(current.get("status", -1)) == desired["status"]
            ):
                logger.info("VNP: Visit %s already up to date", participant_visit_id)
            else:
                polotrial.update_participant_visit(participant_visit_id, desired)
                logger.info("VNP: Updated visit %s", participant_visit_id)
            
            return participant_visit_id
    
    # Não encontrou VNP com a mesma data - criar nova
    logger.info(
        "VNP: No existing visit found for date %s. Creating new visit.",
        target_date
    )
    
    # Preserve the task and procedure template from a previous VNP when the
    # API does not materialize the flowchart automatically for a new visit.
    template_visit = vnps[0] if vnps else None
    template_procedures = []
    if template_visit:
        template_procedures = polotrial.list_participant_visit_procedures(
            co_participante_visita=int(template_visit["id"])
        )

    # The API requires data_estimada on creation. For an unscheduled visit,
    # the actual date is already known, so use it only as a technical value.
    payload = {
        "co_participante": co_participante,
        "co_protocolo": co_protocolo,
        "nome_tarefa": config.VNP_POLOTRIAL_EVENT_NAME,
        "data_estimada": visit_date,
        "data_realizada": visit_date,
        "status": 20,  # 20 = Completed (realizada)
    }
    if template_visit and template_visit.get("co_tarefa") is not None:
        payload["co_tarefa"] = template_visit["co_tarefa"]
    
    created_visit = polotrial.create_participant_visit(payload)
    participant_visit_id = int(created_visit["id"])
    created_procedures = polotrial.list_participant_visit_procedures(
        co_participante_visita=participant_visit_id
    )
    if not created_procedures and template_procedures:
        logger.info(
            "VNP: New visit %s has no procedures; copying %d procedures from visit %s",
            participant_visit_id,
            len(template_procedures),
            template_visit["id"],
        )
        for procedure in template_procedures:
            procedure_payload = {
                "co_participante_visita": participant_visit_id,
                "co_protocolo_procedimento": procedure["co_protocolo_procedimento"],
            }
            polotrial.create_participant_visit_procedure(procedure_payload)
    
    logger.info(
        "VNP: Created new visit (id=%s, date=%s)",
        participant_visit_id,
        visit_date
    )
    
    return participant_visit_id
