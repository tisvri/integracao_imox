from __future__ import annotations

import logging
from typing import Any, Dict, Optional

import pandas as pd
import re
from datetime import datetime

from integracao.polotrial_client import PoloTrialClient
from integracao.redcap_client import RedcapClient
from integracao.mappings.procedures_maps import V2_POLOTRIAL_PROCEDURES_MAP
from integracao.mappings.site_code_maps import SITE_CODE_MAPPING
from integracao.utils import get_date_from_redcap

logger = logging.getLogger(__name__)

# ── Constants ──────────────────────────────────────────────────────────
V1_EVENT = "vsv1_arm_1"
CENTER_FIELD = "dados_pessoais_site"

V2_EVENT = "vrv2_arm_1"
V2_DATE_FIELD = "revisao_dt_visita"

RANDOMIZATION_FIELD = "randomizacao_q3"

ARM_MAPPING: Dict[str, int] = {
    "1": 1,
    "grupo 1 - sérum ultra repositor": 1,
    "2": 2,
    "grupo 2 - hidratante ultra refrescante e hidratante íntimo": 2,
    "3": 3,
    "grupo 3 - tratamento intensivo noturno": 3,
}

ARM_POLOTRIAL_PATTERNS: Dict[int, Dict[str, str]] = {
    1: {
        "pattern": r"Grupo.*S[eé]rum Ultra Repositor",
        "label": "Grupo 1 - Sérum Ultra Repositor",
    },
    2: {
        "pattern": r"Grupo.*Hidra.*Ultra Refres.*Hidra.*[IÍií]ntimo",
        "label": "Grupo 2 - Hidratante Ultra Refrescante e Hidratante Íntimo",
    },
    3: {
        "pattern": r"Grupo.*Trat.*Intensivo Noturno",
        "label": "Grupo 3 - Tratamento Intensivo Noturno",
    },
}


# ── Helpers ────────────────────────────────────────────────────────────
def parse_randomization_group(value: Any) -> Optional[int]:
    """
    Interpreta o campo randomizacao_q3 do REDCap.

    Retorna 1, 2 ou 3 conforme o grupo, ou None se ainda vazio.
    """
    if value is None:
        return None

    s = str(value).strip().lower()
    if not s:
        return None

    group = ARM_MAPPING.get(s)
    if group is not None:
        return group

    logger.warning(
        "V2: Unexpected randomization value for %s: %r",
        RANDOMIZATION_FIELD, value,
    )
    return None


# ── Main sync function ─────────────────────────────────────────────────
def sync_v2_randomization(
    *,
    record_id: str,
    event_name: str,
    redcap: RedcapClient,
    polotrial: PoloTrialClient,
    protocol_nickname: str,
    v2_date_field: str,
) -> Optional[int]:
    """
    Synchronizes Visit 2 (Randomization) in PoloTrial.

    Steps:
        1. Export REDCap data for record + V2 event.
        2. Determine randomization group from randomizacao_q3.
        3. Recover co_centro from V1 event (needed to locate participant).
        4. Locate volunteer → protocol → participant in PoloTrial.
        5. Update VR/V2 visit date and status.
        6. Sync procedure executed dates.
        7. Sync 'Consulta Médica' executor.
        8. Update participant arm based on randomization group.

    Returns:
        The group number (1, 2 or 3), or None if not yet filled.
    """
    if event_name != V2_EVENT:
        raise ValueError(
            f"sync_v2_randomization called with unexpected {event_name=}"
        )

    # ── 1. REDCap data (V2 event) ─────────────────────────────────────
    redcap_payload = redcap.export_record_eav(
        record_id=record_id, event_name=event_name,
    )
    logger.debug(
        "V2: Full REDCap payload for record_id=%s, event=%s: %s",
        record_id, event_name, redcap_payload,
    )

    # ── 2. Randomization group ────────────────────────────────────────
    randomization_group = parse_randomization_group(
        redcap_payload.get(RANDOMIZATION_FIELD),
    )
    if randomization_group is None:
        logger.info(
            "V2: %s not yet filled for record %s. "
            "Continuing sync of VR/V2 visit anyway.",
            RANDOMIZATION_FIELD, record_id,
        )
    else:
        logger.info(
            "V2: record %s -> randomization_group=%s",
            record_id, randomization_group,
        )

    # ── 3. co_centro from V1 ──────────────────────────────────────────
    v1_payload = redcap.export_record_eav(
        record_id=record_id, event_name=V1_EVENT,
    )
    co_centro_raw = str(v1_payload.get(CENTER_FIELD) or "").strip()
    co_centro = SITE_CODE_MAPPING.get(co_centro_raw)
    if not co_centro:
        raise RuntimeError(
            f"V2: Could not map {CENTER_FIELD}={co_centro_raw!r} "
            "to PoloTrial site code"
        )
    logger.debug(
        "V2: Mapped %s=%r -> co_centro=%s", CENTER_FIELD, co_centro_raw, co_centro,
    )

    # ── 4. Locate participant in PoloTrial ────────────────────────────
    volunteer = polotrial.find_volunteer_by_name(record_id)
    if not volunteer:
        raise RuntimeError(
            f"Volunteer not found in PoloTrial for record_id={record_id}. "
            "Cannot sync V2 randomization."
        )
    co_voluntario = int(volunteer["id"])

    protocol = polotrial.get_protocol(
        co_centro=co_centro, apelido_protocolo=protocol_nickname,
    )
    if not protocol:
        raise RuntimeError(
            f"V2: Protocol {protocol_nickname} not found for site {co_centro}"
        )
    co_protocolo = int(protocol["id"])

    participant = polotrial.find_participant(
        co_voluntario=co_voluntario, co_protocolo=co_protocolo,
    )
    if not participant:
        raise RuntimeError(
            f"V2: Participant not found for volunteer={co_voluntario} "
            f"protocol={co_protocolo}"
        )
    co_participante = int(participant["id"])
    logger.debug(
        "V2: co_voluntario=%s co_protocolo=%s co_participante=%s",
        co_voluntario, co_protocolo, co_participante,
    )

    # ── 5. Update VR/V2 visit status and date ─────────────────────────
    v2_date = str(redcap_payload.get(v2_date_field) or "").strip()
    if not v2_date:
        logger.info(
            "V2: date field %s is empty. Not updating visit for participant %s.",
            v2_date_field, co_participante,
        )
        return randomization_group

    visits = polotrial.list_participant_visits(co_participante=co_participante)
    v2_visit = next(
        (v for v in visits if v.get("nome_tarefa") == "VR/V2"), None,
    )
    if not v2_visit:
        raise RuntimeError(
            f"V2: Visit 'VR/V2' not found in PoloTrial for "
            f"participant {co_participante}"
        )
    participante_visita_id = int(v2_visit["id"])

    desired = {"data_realizada": v2_date, "status": 20}
    current = polotrial.get_participant_visit(participante_visita_id)

    if (
        str(current.get("data_realizada", ""))[:10] == str(desired["data_realizada"])[:10]
        and int(current.get("status", -1)) == desired["status"]
    ):
        logger.info(
            "V2: VR/V2 already up to date (id=%s). No update needed.",
            participante_visita_id,
        )
    else:
        polotrial.update_participant_visit(participante_visita_id, desired)
        logger.info("V2: VR/V2 updated (id=%s).", participante_visita_id)

    # ── 6. Sync procedure executed dates ──────────────────────────────
    merged = _build_procedures_dataframe(
        participante_visita_id=participante_visita_id,
        co_protocolo=co_protocolo,
        polotrial=polotrial,
    )

    total = _sync_procedures(
        merged_df=merged,
        redcap_payload=redcap_payload,
        record_id=record_id,
        polotrial=polotrial,
    )
    logger.info("VR/V2 procedures synchronized: %d", total)

    # ── 7. Sync 'Consulta Médica' executor ────────────────────────────
    sync_consulta_medica_executor(
        merged_procedures_df=merged,
        volunteer_payload=redcap_payload,
        polotrial=polotrial,
    )

    # ── 8. Update arm ─��───────────────────────────────────────────────
    if randomization_group is not None:
        update_participant_arm_if_needed(
            randomization_group=randomization_group,
            co_participante=co_participante,
            co_protocolo=co_protocolo,
            polotrial=polotrial,
        )
    else:
        logger.info(
            "VR/V2: randomization_group not yet defined for record %s. "
            "Arm will not be updated at this time.",
            record_id,
        )

    return randomization_group


# ── Procedures helpers ─────────────────────────────────────────────────
def _build_procedures_dataframe(
    *,
    participante_visita_id: int,
    co_protocolo: int,
    polotrial: PoloTrialClient,
) -> pd.DataFrame:
    """
    Builds a merged DataFrame of participant-visit-procedures
    enriched with protocol procedure names.
    """
    pvp_raw = polotrial.list_participant_visit_procedures(
        co_participante_visita=participante_visita_id,
    )
    pvp_df = pd.DataFrame(pvp_raw)

    # Try nested dict first; fallback to join via protocol procedures
    if "dados_protocolo_procedimento" in pvp_df.columns:
        pvp_df["nome_procedimento_estudo"] = pvp_df[
            "dados_protocolo_procedimento"
        ].apply(
            lambda x: x.get("nome_procedimento_estudo")
            if isinstance(x, dict)
            else None
        )
    else:
        logger.warning(
            "dados_protocolo_procedimento not in response; "
            "fetching from /protocolo_procedimento"
        )
        proto_proc = polotrial.list_protocol_procedures(
            co_protocolo=co_protocolo,
        )
        proto_df = (
            pd.DataFrame(proto_proc)[["id", "nome_procedimento_estudo"]]
            .rename(columns={"id": "co_protocolo_procedimento"})
        )
        pvp_df = pd.merge(
            pvp_df, proto_df, on="co_protocolo_procedimento", how="left",
        )

    return pvp_df


def _sync_procedures(
    *,
    merged_df: pd.DataFrame,
    redcap_payload: Dict[str, Any],
    record_id: str,
    polotrial: PoloTrialClient,
) -> int:
    """
    For each procedure in V2_POLOTRIAL_PROCEDURES_MAP, finds the matching
    row in merged_df and updates data_executada in PoloTrial.

    Returns the number of procedures successfully synchronized.
    """
    total = 0

    for cfg in V2_POLOTRIAL_PROCEDURES_MAP:
        pattern = cfg["procedure_name"]
        check_field = cfg["redcap_check_field"]
        date_field = cfg["redcap_date_field"]

        if not (pattern and check_field and date_field):
            logger.warning("Invalid procedure config: %s. Skipping.", cfg)
            continue

        to_sync = merged_df[
            merged_df["nome_procedimento_estudo"].str.contains(
                pattern, regex=True, na=False, flags=re.IGNORECASE,
            )
            & (
                merged_df["data_executada"].isna()
                | (merged_df["data_executada"] == "")
            )
        ]

        if to_sync.empty:
            logger.info(
                "No procedure to sync for pattern %r (record=%s)",
                pattern, record_id,
            )
            continue

        if len(to_sync) > 1:
            logger.warning(
                "Multiple procedures matched %r; using first (id=%s)",
                pattern, to_sync["id"].iloc[0],
            )

        procedure_id = int(to_sync["id"].iloc[0])

        redcap_date = get_date_from_redcap(
            redcap_payload, check_field, date_field,
        )
        if not redcap_date:
            logger.info(
                "No date in REDCap for %r (record=%s)", pattern, record_id,
            )
            continue

        # Normalise — handles both "YYYY-MM-DD" and "YYYY-MM-DD HH:MM"
        redcap_date = str(redcap_date).strip()
        date_match = re.match(r"(\d{4}-\d{2}-\d{2})", redcap_date)
        if not date_match:
            logger.error(
                "Could not extract date from %r for %r", redcap_date, pattern,
            )
            continue

        formatted_date = date_match.group(1)
        try:
            datetime.strptime(formatted_date, "%Y-%m-%d")
        except ValueError:
            logger.error(
                "Invalid date %r for %r (expected YYYY-MM-DD)",
                formatted_date, pattern,
            )
            continue

        polotrial.update_participant_visit_procedure(
            procedure_id, {"data_executada": formatted_date},
        )
        logger.info(
            "Procedure updated: id=%s date=%s", procedure_id, formatted_date,
        )
        total += 1

    return total


# ── Consulta Médica executor ──────────────────────────────────────────
def sync_consulta_medica_executor(
    *,
    merged_procedures_df: pd.DataFrame,
    volunteer_payload: Dict[str, Any],
    polotrial: PoloTrialClient,
) -> None:
    """
    Links the executor to the 'Consulta Médica' procedure based on
    the consulta_nome_medico field in REDCap.
    """
    executor_name = str(
        volunteer_payload.get("consulta_nome_medico") or "",
    ).strip()
    if not executor_name:
        logger.info(
            "VR/V2: consulta_nome_medico empty; skipping executor sync."
        )
        return

    data_realizada = str(
        volunteer_payload.get("consulta_dt") or "",
    ).strip()
    if not data_realizada:
        logger.info("VR/V2: consulta_dt empty; skipping executor sync.")
        return

    cm = merged_procedures_df[
        merged_procedures_df["nome_procedimento_estudo"]
        .astype(str)
        .str.contains(r"Consulta [mM][eéEÉ]dica", regex=True, na=False)
    ]
    if cm.empty:
        logger.warning(
            "VR/V2: 'Consulta Médica' procedure not found in visit."
        )
        return

    procedure_id = int(cm["id"].iloc[0])
    if len(cm) > 1:
        logger.warning(
            "VR/V2: multiple 'Consulta Médica' found; using id=%s",
            procedure_id,
        )

    # find_person_by_name returns a dict, not a DataFrame
    person = polotrial.find_person_by_name(executor_name)
    if not person:
        logger.error(
            "VR/V2: executor %r not found in PoloTrial /pessoas.",
            executor_name,
        )
        return
    executor_id = int(person["id"])

    existing_links = polotrial.list_procedure_executors(procedure_id)
    if any(int(x.get("executor", -1)) == executor_id for x in existing_links):
        logger.info(
            "VR/V2: executor already linked. procedure=%s executor=%s",
            procedure_id, executor_id,
        )
        return

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
        "VR/V2: executor linked to Consulta Médica. "
        "procedure=%s executor=%s response_id=%s",
        procedure_id, executor_id, created.get("id"),
    )


# ── Arm update ─────────────────────────────────────────────────────────
def update_participant_arm_if_needed(
    *,
    randomization_group: int,
    co_participante: int,
    co_protocolo: int,
    polotrial: PoloTrialClient,
) -> None:
    """
    Moves the participant to the correct arm after V2 randomization.

        randomizacao_q3 == 1 → Grupo 1 - Sérum Ultra Repositor
        randomizacao_q3 == 2 → Grupo 2 - Hidratante Ultra Refrescante e Hidratante Íntimo
        randomizacao_q3 == 3 → Grupo 3 - Tratamento Intensivo Noturno
    """
    arm_info = ARM_POLOTRIAL_PATTERNS.get(randomization_group)
    if not arm_info:
        raise ValueError(
            f"Unknown randomization_group={randomization_group}. "
            "Expected 1, 2 or 3."
        )

    target_arm_pattern = arm_info["pattern"]
    arm_label = arm_info["label"]

    all_arms = polotrial.list_arms()
    protocol_arms = [
        a for a in all_arms
        if int(a.get("co_protocolo", -1)) == co_protocolo
    ]
    if not protocol_arms:
        raise RuntimeError(
            f"No arms found for protocol {co_protocolo}"
        )

    target_arm = next(
        (
            a for a in protocol_arms
            if re.search(target_arm_pattern, str(a.get("nome", "")), re.IGNORECASE)
        ),
        None,
    )
    if not target_arm:
        raise RuntimeError(
            f"Target arm {arm_label!r} not found for protocol {co_protocolo}. "
            f"Available: {[a.get('nome') for a in protocol_arms]}"
        )

    co_braco_desired = int(target_arm["id"])

    participant = polotrial.get_participant(co_participante)
    current_arm_id = int(participant.get("co_braco", -1))

    if current_arm_id == co_braco_desired:
        logger.info(
            "VR/V2: participant %s already in arm %s (%s). No update.",
            co_participante, co_braco_desired, arm_label,
        )
        return

    polotrial.update_participant(
        co_participante,
        {"co_braco": co_braco_desired, "atualizar_agenda": "1"},
    )
    logger.info(
        "VR/V2: participant %s arm updated %s → %s (%s).",
        co_participante, current_arm_id, co_braco_desired, arm_label,
    )