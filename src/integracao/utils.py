from typing import Any, Dict, Optional
import logging
from integracao.redcap_client import RedcapClient



logger = logging.getLogger(__name__)


def get_date_from_redcap(redcap_payload: Dict[str, Any], check_field: str, date_field: str)-> Optional[str]:
    if date_field in redcap_payload and redcap_payload.get(date_field):
        check_value = str(redcap_payload.get(check_field,"")).strip().lower()
        if check_field != date_field and check_value in (""): #, "1", "nao", "não"
            logger.warning(
                "Date exists (%s) but check field %s indicates not done (value = %r). Skipping....",
                date_field, check_field, check_value
            )
            return None
        return str(redcap_payload[date_field]).strip()
    return None