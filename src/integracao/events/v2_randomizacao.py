from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import Any, Dict, List, Optional

import pandas as pd

from integracao.polotrial_client import PoloTrialClient
from integracao.redcap_client import RedcapClient
from integracao.mappings.procedures_maps import V2_POLOTRIAL_PROCEDURES_MAP
from integracao.mappings.site_code_maps import SITE_CODE_MAPPING
from integracao.utils import get_date_from_redcap

import re
from datetime import datetime

logger = logging.getLogger(__name__)

V1_EVENT = "vsv1_arm_1"
CENTER_FIELD = "demografia_centro"

V2_EVENT = "vrv2_arm_1"
V2_DATE_FIELD = "revisao_dt_visita"
PK_FIELD = "rando_q8_v2"



def parse_is_pk(value: Any) -> Optional[bool]:
    """
    REDCap can return as:
    - "1" / "Não"
    - "2" / "Sim"
    - vazio
    """
    
    if value is None:
        return None
    
    s = str(value).strip().lower()
    if not s:
        return None
    
    if s in ("1", "não", "nao", "no", "false"):
        return False
    if s in ("2", "sim", "yes", "true"):
        return True
    
    #Unexpected value
    logger.warning("V2: Unexpected PK value for %s: %r", PK_FIELD, value)
    return None

def sync_v2_randomizacao(
    *,
    record_id: str,
    event_name: str,
    redcap: RedcapClient,
    polotrial: PoloTrialClient,
    protocol_nickname: str,
    v2_date_field: str,
) -> Optional[bool]:
    """

    Synchronizes Visit 2 (Randomization) in PoloTrial.
    
    Args:
    - record_id: The REDCap record ID
    - event_name (str): The REDCap event name being processed
    - redcap: An instance of RedcapClient
    - polotrial: An instance of PoloTrialClient
    - protocol_nickname: The protocol nickname in PoloTrial
    - v2_date_field: The REDCap field name for Visit 2 date
    
    Raises:
    - ValueError: If called with an unexpected event_name
    -- Note: The use of {event_name!r} ensures the event name is shown with quotes in the error message.
    
    Returns:

    - True/False if it is already possible to determine the PK

    - None if it has not yet been filled (trigger may call before)

    """
    
    if event_name != V2_EVENT:
        raise ValueError(f"sync_v2_randomizacao called with unexpected event_name: {event_name=}")
    

    # 1. Get Redcap data (record and event)
    redcap_payload  = redcap.export_record_eav(
        record_id,
        event_name
        )
    
    # 1. If the participant will be realocated to PK arm
    is_pk = parse_is_pk(redcap_payload.get(PK_FIELD))
    if is_pk is None:
        logger.info("V2: %s not yet filled in for record %s. Continuing sync of VR/V2 visit anyway.", PK_FIELD, record_id)
    else:
        logger.info("V2: record %s -> is_pk=%s", record_id, is_pk)
    
    # 2. Recovering co_centro (essential to find the participant in PoloTrial)
    v1_payload = redcap.export_record_eav(record_id, V1_EVENT)
    co_centro_raw = str(v1_payload.get(CENTER_FIELD) or "").strip()
    co_centro = SITE_CODE_MAPPING.get(co_centro_raw)
    if not co_centro:
        raise RuntimeError(f"V2: Could not map {CENTER_FIELD}={co_centro_raw!r} to PoloTrial site code")
    
    # 3. Recovering volunteer/participant
    volunteer = polotrial.find_volunteer_by_name(record_id)
    if not volunteer:
        raise RuntimeError(f"Volunteer not found in PoloTrial for record_id={record_id}. Cannot sync V2 randomization.")
    co_voluntario = int(volunteer["id"])
    
    protocol = polotrial.get_protocol(co_centro=co_centro, apelido_protocolo=protocol_nickname)
    if not protocol:
        raise RuntimeError(f"V2: Protocol {protocol_nickname} not found for site {co_centro}")
    co_protocolo = int(protocol["id"])
    
    participant = polotrial.find_participant(co_voluntario = co_voluntario, co_protocolo = co_protocolo)
    if not participant:
        raise RuntimeError(f"V2: Participant not found in PoloTrial for volunteer {co_voluntario!r} and protocol {co_protocolo!r}")
    co_participante = int(participant["id"])
    
    # 4. Update V2 visit status and date
    v2_date = str(redcap_payload.get(v2_date_field) or "").strip()
    if not v2_date:
        logger.info("V2: date field %s is empty. Not updating V2 visit date for participant %s", v2_date_field, co_participante)
        return is_pk
    
    visits = polotrial.list_participant_visits(co_participante=co_participante)
    v2 = next((v for v in visits if v.get("nome_tarefa") == "VR/V2"), None)
    if not v2:
        raise RuntimeError(f"V2: Participant visit 'VR/V2' not found in Polotrial for participant {co_participante!r}")
    
    participante_visita_id = int(v2["id"])
    
    desired = {
        "data_realizada": v2_date,
        "status": 20,  # Realizada
    }
    
    current = polotrial.get_participant_visit(participante_visita_id)
    if (
        str(current.get("data_realizada", ""))[:10] == str(desired["data_realizada"])[:10]
        and int(current.get("status", -1)) == desired["status"]
    ):
        logger.info("V2: VR/V2 already up to date (id=%s). No update needed.", participante_visita_id)
    else:
        polotrial.update_participant_visit(participante_visita_id,desired)
        logger.info("V2: VR/V2 updated (id=%s).", participante_visita_id)
    
    # 5. Procedures: load participant visit procedure + names
    pvp = polotrial.list_participant_visit_procedures(co_participante_visita = participante_visita_id)
    proto_proc = polotrial.list_protocol_procedures(co_protocolo = co_protocolo)
    
    pvp_df = pd.DataFrame(pvp)
    proto_df = pd.DataFrame(proto_proc)[["id", "co_procedimento","nome_procedimento_estudo"]].rename(columns={"id":"co_protocolo_procedimento"})
    merged = pd.merge(
        pvp_df,
        proto_df,
        on="co_protocolo_procedimento",
        how="left"        
    )
    
    # 6. synchronize executed dates
    total = 0
    for cfg in V2_POLOTRIAL_PROCEDURES_MAP:
        pattern = cfg["procedure_name"]
        co_proc = cfg["co_procedimento"]
        check_field = cfg["redcap_check_field"]
        date_field = cfg["redcap_date_field"]
        
        if not (pattern and co_proc and check_field and date_field):
            logger.warning("Invalid procedure mapping config: %s. Skipping...", cfg)
            continue
        
        to_sync = merged[
            merged["nome_procedimento_estudo"].str.contains(pattern, regex = True, na = False, flags=re.IGNORECASE) 
            &  (merged["co_procedimento"].astype(str) == str(co_proc)) 
            & (merged["data_executada"].isna() | (merged["data_executada"] == ""))
        ]
        
        if to_sync.empty:
            logger.info("No procedure to sync for pattern %r and co_procedimento=%s", pattern, co_proc)
            continue
        
        procedure_id = int(to_sync["id"].iloc[0])
        redcap_date = get_date_from_redcap(redcap_payload , check_field, date_field)
        if not redcap_date:
            logger.info("No date to sync from REDCap for procedure %r (record_id=%s)", pattern, record_id)
            continue
        
        # a. validate the date format
        try:
            dt = datetime.strptime(redcap_date, "%Y-%m-%d")
        except ValueError:
            logger.error("Invalid date for %s: %r (expected YYYY-MM-DD)", pattern, redcap_date)
            continue
        
        polotrial.update_participant_visit_procedure(procedure_id, {"data_executada": dt.strftime("%Y-%m-%d")})
        total += 1
        
    logger.info("VR/V2 procedures synchronized: %d", total)
    
    # 7. Update Participant arm if PK is defined
    if is_pk is not None:
        update_participant_arm_if_needed(
            is_pk = is_pk,
            co_participante = co_participante,
            co_protocolo = co_protocolo,
            polotrial = polotrial,
        )
    else:
        logger.info("VR/V2: is_pk not yet defined for record %s. Arm will not be updated at this time.", record_id)
    
    return is_pk
    
    
def sync_consulta_medica_executor(
    *,
    merged_procedures_df: pd.DataFrame,
    volunteer_payload: Dict[str, Any],
    polotrial: PoloTrialClient,
) -> None:
    executor_name = str(volunteer_payload.get("form_medico_rubrica") or "").strip()
    if not executor_name:
        logger.info("VR/V2: form_medico_rubrica vazio; não é possível atribuir executor (Consulta Médica).")
        return

    data_realizada = str(volunteer_payload.get("form_medico_dt_rubrica") or "").strip()
    if not data_realizada:
        logger.info("VR/V2: form_medico_dt_rubrica vazio; não é possível atribuir executor (Consulta Médica).")
        return

    cm = merged_procedures_df[
        merged_procedures_df["nome_procedimento_estudo"]
        .astype(str)
        .str.contains(r"^Consulta M[eéEÉ]dica$", regex=True, na=False)
    ]
    if cm.empty:
        logger.warning("VR/V2: procedimento 'Consulta Médica' não encontrado na visita (PoloTrial).")
        return

    procedure_id = int(cm["id"].iloc[0])
    if len(cm) > 1:
        logger.warning("VR/V2: múltiplos 'Consulta Médica' encontrados; usando o primeiro id=%s", procedure_id)
    
    #1. locate the procedure "Consulta Médica"
    person = polotrial.find_person_by_name(executor_name)
    if not person:
        logger.error("VR/V2: executor não encontrado em /pessoas para ds_nome=%r", executor_name)
        return
    executor_id = int(person["id"])    
    
    #2. Find executor in Polotrial /pessoas endpoint
    existing_links = polotrial.list_procedure_executors(procedure_id)

    already_linked = any(int(x.get("executor", -1)) == executor_id for x in existing_links)
    if already_linked:
        logger.info(
            "VR/V2: executor já está vinculado à Consulta Médica. procedure_id=%s executor_id=%s",
            procedure_id,
            executor_id,
        )
        return
    
    #3. create executor link -> procedure
    payload = {
        "co_participante_visita_procedimento": procedure_id,
        "executor": executor_id,
        "data_realizada": data_realizada,
        "data_previsto_pagamento": "",
        "data_realizado_pagamento": "",
        "valor": "",
        "valor_total_procedimento": "",
        "observacoes": "",
    }

    created = polotrial.create_procedure_executor(payload)
    logger.info(
        "VR/V2: executor atribuído em Consulta Médica. procedure_id=%s executor_id=%s response_id=%s",
        procedure_id,
        executor_id,
        created.get("id"),
    )
    
def update_participant_arm_if_needed(
    *,
    is_pk: bool,
    co_participante: int,
    co_protocolo: int,
    polotrial: PoloTrialClient,
) -> None:
    """ 
    Update participant arm after v2 randomization
    
    if is_pk is True, set to "IMOX Versão n°1 - SUBGRUPO PK"
    if is_pk is False, set to "IMOX Versão n°1"
    
    Participants always start in "IMOX Versão n°1 - TRIAGEM" arm at V1 visit.
    
    """
    # 1. Get arms
    all_arms = polotrial.list_arms()
    protocol_arms = [ arm for arm in all_arms if int(arm.get("co_protocolo", -1)) == co_protocolo]
    
    if not protocol_arms:
        raise RuntimeError(f"Could not find any arms for protocol {co_protocolo}")
    
    # 2. Find desired arm
    if is_pk:
        # target arm is "IMOX Versão n°1 - SUBGRUPO PK"
        target_arm_pattern = r"^IMOX Vers[aã]o n[°º]1 - SUBGRUPO PK$"
        arm_label = "IMOX Versão n°1 - SUBGRUPO PK"
    else:
        # target arm is "IMOX Versão n°1"
        target_arm_pattern = r"^IMOX Vers[aã]o n[°º]1$"
        arm_label = "IMOX Versão n°1"
        
    target_arm = next(
        (arm for arm in protocol_arms if re.search(target_arm_pattern, str(arm.get("nome", "")), re.IGNORECASE)), 
        None,
    )
    
    if not target_arm:
        raise RuntimeError(f"Could not find target arm {arm_label!r} for protocol {co_protocolo}. " f"Available arms: {[arm.get('nome') for arm in protocol_arms]}")
    
    co_braco_desired = int(target_arm["id"])
    
    # 3. Check current arm
    participant = polotrial.get_participant(co_participante)
    current_arm_id = int(participant.get("co_braco", -1))
    
    if current_arm_id == co_braco_desired:
        logger.info(
            "VR/V2: participant %s already in desired arm %s (%s). No update needed.",
            co_participante,
            co_braco_desired,
            arm_label,
        )
        return
    
    # 4. Update arm
    payload = {
        "co_braco": co_braco_desired,
        "atualizar_agenda" : "1" # Update schedule
    }
    
    polotrial.update_participant(co_participante, payload)
    logger.info(
        "VR/V2: participant %s arm updated from %s to %s (%s).",
        co_participante,
        current_arm_id,
        co_braco_desired,
        arm_label,
    )
    