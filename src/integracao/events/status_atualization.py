from __future__ import annotations

import logging
import json
from typing import Any, Dict, Optional

import pandas as pd
import re
from datetime import datetime
import time

from integracao.events.v2_randomizacao import CENTER_FIELD
from integracao.mappings.site_code_maps import SITE_CODE_MAPPING
from integracao.polotrial_client import PoloTrialClient
from integracao.redcap_client import RedcapClient

from integracao.mappings.status_maps import STATUS_CODE_MAPPING 

from integracao.sync_engine import V1_EVENT
from integracao.utils import get_date_from_redcap
import os
import dotenv


dotenv.load_dotenv(override=True)

logger = logging.getLogger(__name__)

#====================================================================================================
# Constants
#====================================================================================================

PARTICIPANT_STATUS_EVENT = os.getenv("PARTICIPANT_STATUS_EVENT_NAME")


#====================================================================================================
# Participant status update sync function
#====================================================================================================

def sync_participant_status_update(
    *,
    record_id: str,
    event_name: str,
    redcap: RedcapClient,
    polotrial: PoloTrialClient,
    protocol_nickname: str,
) -> None:

    """
    Sync participant status updates from REDCap to PoloTrial.
    This function retrieves participant status updates from REDCap, maps the status codes to PoloTrial's format,
    and updates the corresponding records in PoloTrial.
    Args:
        redcap (RedcapClient): An instance of the RedcapClient to interact with REDCap API.
        polotrial (PoloTrialClient): An instance of the PoloTrialClient to interact with PoloTrial API.
        protocol_nickname (str): The nickname of the protocol in PoloTrial.

    Steps:
        1. Retrieve participant status updates from REDCap using the specified event name.
        2. For each participant status update:
            a. Extract the participant ID and the new status code.
            b. Map the REDCap status code to the corresponding PoloTrial status code using STATUS_CODE_MAPPING.
            c. Update the participant's status in PoloTrial using the mapped status code.
    
    Returns:
        None
    """
    # Step 1: Get REDCap data from VS/V1
    redcap_payload = redcap.export_record_eav(record_id, event_name)
    logger.info(f"Retrieved REDCap data for record_id: {record_id}, event_name: {event_name}")

    v1_payload = redcap.export_record_eav(record_id, V1_EVENT)

    # Step 2: Mapping fields REDCap -> PoloTrial
    co_centro_raw = str(v1_payload.get(CENTER_FIELD) or "").strip()
    site_code = SITE_CODE_MAPPING.get(co_centro_raw)
    if not site_code:
        raise RuntimeError(
            f"V2: Could not map {CENTER_FIELD}={co_centro_raw!r} "
            "to PoloTrial site code"
        )
    
    # Step 3: Volunteer (presupposes V1 already ran)
    volunteer = polotrial.find_volunteer_by_name(record_id)
    if not volunteer:
        raise RuntimeError(
            f"Volunteer not found in PoloTrial for record_id={record_id}. "
            "Cannot sync V2 randomization."
        )
    co_voluntario = int(volunteer["id"])
    logger.info("Volunteer found: %s -> id=%s", record_id, co_voluntario)




    