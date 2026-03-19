from __future__ import annotations

from typing import Dict, Any, Optional
import os
import dotenv

from integracao.config import config

V3_EVENT = config.V3_EVENT_NAME
V4_EVENT = config.V4_EVENT_NAME
V5_EVENT = config.V5_EVENT_NAME
PRE_INSERTION_EVENT = config.PRE_INSERTION_EVENT_NAME
PARTICIPANT_STATUS_EVENT = config.PARTICIPANT_STATUS_EVENT_NAME
H24_EVENT = config.H24_EVENT_NAME
W1_EVENT = config.W1_EVENT_NAME
W2_EVENT = config.W2_EVENT_NAME
W3_EVENT = config.W3_EVENT_NAME
W4_EVENT = config.W4_EVENT_NAME
W8_EVENT = config.W8_EVENT_NAME
W12_EVENT = config.W12_EVENT_NAME
W16_EVENT = config.W16_EVENT_NAME
W20_EVENT = config.W20_EVENT_NAME
W24_EVENT = config.W24_EVENT_NAME
VISITA_NAO_PROGRAMADA_EVENT = config.NP_EVENT_NAME


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
    V3_EVENT: VisitConfig(
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
    V4_EVENT: VisitConfig(
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
    V5_EVENT: VisitConfig(
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
    PRE_INSERTION_EVENT: VisitConfig(
        redcap_event_name = PRE_INSERTION_EVENT,
        polotrial_visit_name = "Pré-inserção",
        date_field = "sub_pk_dt_visita",
        procedures_map = PK_PRE_INSERCAO_PROCEDURES_MAP, # No procedures to sync
        requires_pk=None,
        executor_config={
            "field": "consulta_nome_medico",
            'date_field': 'consulta_dt',
            "procedure_pattern": r"^Consulta M[eéEÉ]dica$"
        },        
    ),

    # H24_EVENT
    H24_EVENT: VisitConfig(
        redcap_event_name = H24_EVENT,
        polotrial_visit_name = "H24_POLOTRIAL_EVENT_NAME",
        date_field = "sub_pk_dt_visita",
        procedures_map = PK_24H_PROCEDURES_MAP, # No procedures to sync
        requires_pk=None,
        executor_config={
            "field": "consulta_nome_medico",
            'date_field': 'consulta_dt',
            "procedure_pattern": r"^Consulta M[eéEÉ]dica$"
        },        
    ),
    
    # W1_EVENT_NAME
    W1_EVENT: VisitConfig(
        redcap_event_name = W1_EVENT,
        polotrial_visit_name = "W1_POLOTRIAL_EVENT_NAME",
        date_field = "sub_pk_dt_visita",
        procedures_map = PK_1_SEMANA_PROCEDURES_MAP, # No procedures to sync
        requires_pk=None,
        executor_config={
            "field": "consulta_nome_medico",
            'date_field': 'consulta_dt',
            "procedure_pattern": r"^Consulta M[eéEÉ]dica$"
        },        
    ),
    
    # W2_EVENT_NAME
    W2_EVENT: VisitConfig(
        redcap_event_name = W2_EVENT,
        polotrial_visit_name = "W2_POLOTRIAL_EVENT_NAME",
        date_field = "sub_pk_dt_visita",
        procedures_map = PK_2_SEMANAS_PROCEDURES_MAP, # No procedures to sync
        requires_pk=None,
        executor_config={
            "field": "consulta_nome_medico",
            'date_field': 'consulta_dt',
            "procedure_pattern": r"^Consulta M[eéEÉ]dica$"
        },        
    ),
    
    # W3_EVENT_NAME
    W3_EVENT: VisitConfig(
        redcap_event_name = W3_EVENT,
        polotrial_visit_name = "W3_POLOTRIAL_EVENT_NAME",
        date_field = "sub_pk_dt_visita",
        procedures_map = PK_3_SEMANAS_PROCEDURES_MAP, # No procedures to sync
        requires_pk=None,
        executor_config={
            "field": "consulta_nome_medico",
            'date_field': 'consulta_dt',
            "procedure_pattern": r"^Consulta M[eéEÉ]dica$"
        },        
    ),
    
    # W4_EVENT_NAME
    W4_EVENT: VisitConfig(
        redcap_event_name = W4_EVENT,
        polotrial_visit_name = "W4_POLOTRIAL_EVENT_NAME",
        date_field = "sub_pk_dt_visita",
        procedures_map = PK_4_SEMANAS_PROCEDURES_MAP, # No procedures to sync
        requires_pk=None,
        executor_config={
            "field": "consulta_nome_medico",
            'date_field': 'consulta_dt',
            "procedure_pattern": r"^Consulta M[eéEÉ]dica$"
        },        
    ),
    
    # W8_EVENT_NAME
    W8_EVENT: VisitConfig(
        redcap_event_name = W8_EVENT,
        polotrial_visit_name = "W8_POLOTRIAL_EVENT_NAME",
        date_field = "sub_pk_dt_visita",
        procedures_map = PK_8_SEMANAS_PROCEDURES_MAP, # No procedures to sync
        requires_pk=None,
        executor_config={
            "field": "consulta_nome_medico",
            'date_field': 'consulta_dt',
            "procedure_pattern": r"^Consulta M[eéEÉ]dica$"
        },        
    ),
    
    # W12_EVENT_NAME
    W12_EVENT: VisitConfig(
        redcap_event_name = W12_EVENT,
        polotrial_visit_name = "W12_POLOTRIAL_EVENT_NAME",
        date_field = "sub_pk_dt_visita",
        procedures_map = PK_12_SEMANAS_PROCEDURES_MAP, # No procedures to sync
        requires_pk=None,
        executor_config={
            "field": "consulta_nome_medico",
            'date_field': 'consulta_dt',
            "procedure_pattern": r"^Consulta M[eéEÉ]dica$"
        },        
    ),
    
    # W16_EVENT_NAME
    W16_EVENT: VisitConfig(
        redcap_event_name = W16_EVENT,
        polotrial_visit_name = "W16_POLOTRIAL_EVENT_NAME",
        date_field = "sub_pk_dt_visita",
        procedures_map = PK_16_SEMANAS_PROCEDURES_MAP, # No procedures to sync
        requires_pk=None,
        executor_config={
            "field": "consulta_nome_medico",
            'date_field': 'consulta_dt',
            "procedure_pattern": r"^Consulta M[eéEÉ]dica$"
        },        
    ),
    
    # W20_EVENT_NAME
    W20_EVENT: VisitConfig(
        redcap_event_name = W20_EVENT,
        polotrial_visit_name = "W20_POLOTRIAL_EVENT_NAME",
        date_field = "sub_pk_dt_visita",
        procedures_map = PK_20_SEMANAS_PROCEDURES_MAP, # No procedures to sync
        requires_pk=None,
        executor_config={
            "field": "consulta_nome_medico",
            'date_field': 'consulta_dt',
            "procedure_pattern": r"^Consulta M[eéEÉ]dica$"
        },        
    ),
    
    # W24_EVENT_NAME
    W24_EVENT: VisitConfig(
        redcap_event_name = W24_EVENT,
        polotrial_visit_name = "W24_POLOTRIAL_EVENT_NAME",
        date_field = "sub_pk_dt_visita",
        procedures_map = PK_24_SEMANAS_PROCEDURES_MAP, # No procedures to sync
        requires_pk=None,
        executor_config={
            "field": "consulta_nome_medico",
            'date_field': 'consulta_dt',
            "procedure_pattern": r"^Consulta M[eéEÉ]dica$"
        },        
    ),



    # Unscheduled Visit
    VISITA_NAO_PROGRAMADA_EVENT: VisitConfig(
        redcap_event_name = VISITA_NAO_PROGRAMADA_EVENT,
        polotrial_visit_name= "VNP_POLOTRIAL_EVENT_NAME",
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
