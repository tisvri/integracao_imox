from __future__ import annotations

from typing import Dict, Any, Optional
import os
import dotenv

V3_EVENT = os.getenv("V3_EVENT_NAME")
V4_EVENT = os.getenv("V4_EVENT_NAME")
V5_EVENT = os.getenv("V5_EVENT_NAME")
PRE_INSERTION_EVENT = os.getenv("PRE_INSERTION_EVENT_NAME")
PARTICIPANT_STATUS_EVENT = os.getenv("PARTICIPANT_STATUS_EVENT_NAME")
H24_EVENT = os.getenv("H24_EVENT_NAME")
W1_EVENT = os.getenv("W1_EVENT_NAME")
W2_EVENT = os.getenv("W2_EVENT_NAME")
W3_EVENT = os.getenv("W3_EVENT_NAME")
W4_EVENT = os.getenv("W4_EVENT_NAME")
W8_EVENT = os.getenv("W8_EVENT_NAME")
W12_EVENT = os.getenv("W12_EVENT_NAME")
W16_EVENT = os.getenv("W16_EVENT_NAME")
W20_EVENT = os.getenv("W20_EVENT_NAME")
W24_EVENT = os.getenv("W24_EVENT_NAME")
VISITA_NAO_PROGRAMADA_EVENT = os.getenv("NP_EVENT_NAME")


# Importing procedure mapping from sync_engine to avoid circular dependency
from integracao.mappings.procedures_maps import (
    PK_12_SEMANAS_PROCEDURES_MAP,
    PK_16_SEMANAS_PROCEDURES_MAP,
    PK_1_SEMANA_PROCEDURES_MAP,
    PK_20_SEMANAS_PROCEDURES_MAP,
    PK_24_SEMANAS_PROCEDURES_MAP,
    PK_24H_PROCEDURES_MAP,
    PK_2_SEMANAS_PROCEDURES_MAP,
    PK_3_SEMANAS_PROCEDURES_MAP,
    PK_4_SEMANAS_PROCEDURES_MAP,
    PK_8_SEMANAS_PROCEDURES_MAP,
    PK_PRE_INSERCAO_PROCEDURES_MAP,
    V3_PROCEDURES_MAP,
    V4_PROCEDURES_MAP,
    V5_PROCEDURES_MAP,
    VISITA_NAO_PROGRAMADA_PROCEDURES_MAP,
)

class VisitConfig:
    """
    Configuring an generic visit
    """
    
    def __init__(
        self,
        *,
        redcap_event_name:str,
        polotrial_visit_name:str,
        date_field: str,
        procedures_map: list,
        requires_pk: Optional[Dict[str, Any]] = None,
        executor_config: Optional[Dict[str, Any]] = None
    ):
        self.redcap_event_name = redcap_event_name
        self.polotrial_visit_name = polotrial_visit_name
        self.date_field = date_field
        self.procedures_map = procedures_map
        self.requires_pk = requires_pk or {}
        self.executor_config = executor_config or {} # {field, date_field, procedure_pattern}
    
    
# Visits catalog
VISITS_CATALOG = {
    #V3
    # This code snippet is defining a specific configuration for a visit in the `VISITS_CATALOG`
    # dictionary within the `VisitConfig` class.
    "V3_EVENT": VisitConfig(
        redcap_event_name = V3_EVENT,
        polotrial_visit_name = "V3",
        date_field = "revisao_dt_visita",
        procedures_map = V3_PROCEDURES_MAP,
        requires_pk=None,
        executor_config={
            "field": "consulta_nome_medico",
            'date_field': 'consulta_dt',
            "procedure_pattern": r"^Consulta M[eéEÉ]dica$"
        },        
    ),
    #V4
    "V4_EVENT": VisitConfig(
        redcap_event_name = V4_EVENT,
        polotrial_visit_name = "V4",
        date_field = "revisao_dt_visita",
        procedures_map = V4_PROCEDURES_MAP,
        requires_pk=None,
        executor_config={
            "field": "consulta_nome_medico",
            'date_field': 'consulta_dt',
            "procedure_pattern": r"^Consulta M[eéEÉ]dica$"
        },        
    ),

    # V5
    "V5_EVENT": VisitConfig(
        redcap_event_name = V5_EVENT,
        polotrial_visit_name = "V5",
        date_field = "revisao_dt_visita",
        procedures_map = V5_PROCEDURES_MAP, # No procedures to sync
        requires_pk=None,
        executor_config={
            "field": "consulta_nome_medico",
            'date_field': 'consulta_dt',
            "procedure_pattern": r"^Consulta M[eéEÉ]dica$"
        },        
    ),

    # PRE_INSERTION_EVENT_NAME
    "PRE_INSERTION_EVENT": VisitConfig(
        redcap_event_name = PRE_INSERTION_EVENT,
        polotrial_visit_name = "Pré-inserção",
        date_field = "revisao_dt_visita",
        procedures_map = PK_PRE_INSERCAO_PROCEDURES_MAP, # No procedures to sync
        requires_pk=None,
        executor_config={
            "field": "consulta_nome_medico",
            'date_field': 'consulta_dt',
            "procedure_pattern": r"^Consulta M[eéEÉ]dica$"
        },        
    ),

    # H24_EVENT
    "H24_EVENT": VisitConfig(
        redcap_event_name = H24_EVENT,
        polotrial_visit_name = "H24",
        date_field = "revisao_dt_visita",
        procedures_map = PK_24H_PROCEDURES_MAP, # No procedures to sync
        requires_pk=None,
        executor_config={
            "field": "consulta_nome_medico",
            'date_field': 'consulta_dt',
            "procedure_pattern": r"^Consulta M[eéEÉ]dica$"
        },        
    ),
    
    # W1_EVENT_NAME
    "W1_EVENT": VisitConfig(
        redcap_event_name = W1_EVENT,
        polotrial_visit_name = "W1",
        date_field = "revisao_dt_visita",
        procedures_map = PK_1_SEMANA_PROCEDURES_MAP, # No procedures to sync
        requires_pk=None,
        executor_config={
            "field": "consulta_nome_medico",
            'date_field': 'consulta_dt',
            "procedure_pattern": r"^Consulta M[eéEÉ]dica$"
        },        
    ),
    
    # W2_EVENT_NAME
    "W2_EVENT": VisitConfig(
        redcap_event_name = W2_EVENT,
        polotrial_visit_name = "W2",
        date_field = "revisao_dt_visita",
        procedures_map = PK_2_SEMANAS_PROCEDURES_MAP, # No procedures to sync
        requires_pk=None,
        executor_config={
            "field": "consulta_nome_medico",
            'date_field': 'consulta_dt',
            "procedure_pattern": r"^Consulta M[eéEÉ]dica$"
        },        
    ),
    
    # W3_EVENT_NAME
    "W3_EVENT": VisitConfig(
        redcap_event_name = W3_EVENT,
        polotrial_visit_name = "W3",
        date_field = "revisao_dt_visita",
        procedures_map = PK_3_SEMANAS_PROCEDURES_MAP, # No procedures to sync
        requires_pk=None,
        executor_config={
            "field": "consulta_nome_medico",
            'date_field': 'consulta_dt',
            "procedure_pattern": r"^Consulta M[eéEÉ]dica$"
        },        
    ),
    
    # W4_EVENT_NAME
    "W4_EVENT": VisitConfig(
        redcap_event_name = W4_EVENT,
        polotrial_visit_name = "W4",
        date_field = "revisao_dt_visita",
        procedures_map = PK_4_SEMANAS_PROCEDURES_MAP, # No procedures to sync
        requires_pk=None,
        executor_config={
            "field": "consulta_nome_medico",
            'date_field': 'consulta_dt',
            "procedure_pattern": r"^Consulta M[eéEÉ]dica$"
        },        
    ),
    
    # W8_EVENT_NAME
    "W8_EVENT": VisitConfig(
        redcap_event_name = W8_EVENT,
        polotrial_visit_name = "W8",
        date_field = "revisao_dt_visita",
        procedures_map = PK_8_SEMANAS_PROCEDURES_MAP, # No procedures to sync
        requires_pk=None,
        executor_config={
            "field": "consulta_nome_medico",
            'date_field': 'consulta_dt',
            "procedure_pattern": r"^Consulta M[eéEÉ]dica$"
        },        
    ),
    
    # W12_EVENT_NAME
    "W12_EVENT": VisitConfig(
        redcap_event_name = W12_EVENT,
        polotrial_visit_name = "W12",
        date_field = "revisao_dt_visita",
        procedures_map = PK_12_SEMANAS_PROCEDURES_MAP, # No procedures to sync
        requires_pk=None,
        executor_config={
            "field": "consulta_nome_medico",
            'date_field': 'consulta_dt',
            "procedure_pattern": r"^Consulta M[eéEÉ]dica$"
        },        
    ),
    
    # W16_EVENT_NAME
    "W16_EVENT": VisitConfig(
        redcap_event_name = W16_EVENT,
        polotrial_visit_name = "W16",
        date_field = "revisao_dt_visita",
        procedures_map = PK_16_SEMANAS_PROCEDURES_MAP, # No procedures to sync
        requires_pk=None,
        executor_config={
            "field": "consulta_nome_medico",
            'date_field': 'consulta_dt',
            "procedure_pattern": r"^Consulta M[eéEÉ]dica$"
        },        
    ),
    
    # W20_EVENT_NAME
    "W20_EVENT": VisitConfig(
        redcap_event_name = W20_EVENT,
        polotrial_visit_name = "W20",
        date_field = "revisao_dt_visita",
        procedures_map = PK_20_SEMANAS_PROCEDURES_MAP, # No procedures to sync
        requires_pk=None,
        executor_config={
            "field": "consulta_nome_medico",
            'date_field': 'consulta_dt',
            "procedure_pattern": r"^Consulta M[eéEÉ]dica$"
        },        
    ),
    
    # W24_EVENT_NAME
    "W24_EVENT": VisitConfig(
        redcap_event_name = W24_EVENT,
        polotrial_visit_name = "W24",
        date_field = "revisao_dt_visita",
        procedures_map = PK_24_SEMANAS_PROCEDURES_MAP, # No procedures to sync
        requires_pk=None,
        executor_config={
            "field": "consulta_nome_medico",
            'date_field': 'consulta_dt',
            "procedure_pattern": r"^Consulta M[eéEÉ]dica$"
        },        
    ),



    # Unscheduled Visit
    "VISITA_NAO_PROGRAMADA_EVENT": VisitConfig(
        redcap_event_name = VISITA_NAO_PROGRAMADA_EVENT,
        polotrial_visit_name= "Não Programada",
        date_field = "form_medico_dt_visita",
        procedures_map = VISITA_NAO_PROGRAMADA_PROCEDURES_MAP,
        requires_pk=None,
        executor_config={
            "field": "consulta_nome_medico",
            'date_field': 'consulta_dt',
            "procedure_pattern": r"^Consulta M[eéEÉ]dica$"
        },        
    )
}
