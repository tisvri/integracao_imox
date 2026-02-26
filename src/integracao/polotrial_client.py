from __future__ import annotations # For Python 3.7 compatibility

import logging
from typing import Any, Dict, Optional
from urllib.parse import urljoin
import requests

logger = logging.getLogger(__name__) # Set up module-level logger

class PoloTrialClient:
    """
    Client for interacting with the PoloTrial API.
    """
    def __init__(self, base_url: str, username: str, password: str, timeout: int = 30):
        self.base_url = base_url.rstrip("/") + "/"
        self.username = username
        self.password = password
        self.timeout = timeout
        self.session = requests.Session() # Use a session for connection pooling
        self._authed = False # Track authentication state
    
    def _login(self) -> None:
        """
        Authenticate with the PoloTrial API.
        """
        session_url = urljoin(self.base_url, "sessions")
        print(session_url)
        payload = {
            "nome": self.username,
            "password": self.password
        }
        headers = {
            "Content-Type": "application/json"
        }
        
        polotrial_request = self.session.post(session_url, json = payload, headers = headers, timeout = self.timeout)
        if polotrial_request.status_code not in (200, 201):
            raise RuntimeError(f"Polotrial login failed: {polotrial_request.status_code} - {polotrial_request.text}")
        
        #cookie userId comes in the response
        if not self.session.cookies.get("userId"):
            raise RuntimeError("Polotrial login failed: userId cookie not found")
        
        self._authed = True
        logger.info("Polotrial: authentication successful")
    
    def _request(self, method:str, path: str, *, params = None, json = None) -> requests.Response:
        """
        Make an authenticated request to the PoloTrial API.
        """
        if not self._authed:
            self._login()
        
        url = urljoin(self.base_url, path.lstrip("/"))
        polotrial_response = self.session.request(method, url, params = params, json = json, timeout = self.timeout)
        
        # If session expired, re-authenticate and retry once
        if polotrial_response.status_code in (401, 403):
            logger.warning("Polotrial: auth failed (%s). Retrying login once...", polotrial_response.status_code)
            self._authed = False
            self._login()
            polotrial_response = self.session.request(method, url, params = params, json = json, timeout = self.timeout)
        
        return polotrial_response
    
    # -------------------------------------------
    # Integration methods
    #--------------------------------------------
    
    def find_volunteer_by_name(self, name: str) -> Optional[Dict[str, Any]]:
        """
        Search in Polotrial /voluntario endpoint for a volunteer in name field.
        """
        
        volunteer_request = self._request("GET", "/voluntarios", params={"nome": name})
        if volunteer_request.status_code != 200:
            raise RuntimeError(f"Error querying volunteer: {volunteer_request.status_code} - {volunteer_request.text}")
        data = volunteer_request.json()
        return data[0] if isinstance(data, list) and data else None
    
    def create_volunteer(self, payload: Dict[str, Any]) -> Dict[str,Any]:
        """
        Create a new volunteer in Polotrial /voluntario endpoint.
        """
        volunteer_request = self._request("POST", "/voluntarios", json=payload)
        
        # API bug: sometimes returns 500 but creates the volunteer.
        if volunteer_request.status_code in (200, 201):
            return volunteer_request.json()
        
        # If there was an error, check if the volunteer was created anyway.
        if volunteer_request.status_code == 500:
            logger.warning("Polotrial returned 500 when creating volunteer. Checking if it was created anyway...")
            
            # Try to find the volunteer by name.
            existing = self.find_volunteer_by_name(payload["nome"])
            if existing:
                logger.info("Volunteer was created despite 500 error. %s", existing["id"])
                return existing
            
            # If not found, raise the original error.
        raise RuntimeError(f"Error creating volunteer: {volunteer_request.status_code} - {volunteer_request.text}")
    
    def get_protocol(self, *, co_centro: str, apelido_protocolo: str) -> Optional[Dict[str, Any]]:
        """
        Get protocolo by co_centro and apelido_protocolo.
        """
        protocolo_request = self._request("GET", "/protocolo", params={"co_centro": co_centro, "apelido_protocolo": apelido_protocolo})
        if protocolo_request.status_code != 200:
            raise RuntimeError(f"Error querying protocolo: {protocolo_request.status_code} - {protocolo_request.text}")
        data = protocolo_request.json()
        return data[0] if isinstance(data, list) and data else None
    
    def list_arms(self, co_protocolo: int) -> list[Dict[str, Any]]:
        """
        List all arms from Polotrial /braco endpoint.
        
        :param self: Description
        :param co_protocolo: Description
        :type co_protocolo: int        
        :return: Description
        :rtype: list[Dict[str, Any]]
        """
        arm_request = self._request("GET", "braco", params={"co_protocolo": str(co_protocolo),})
        print(f'lista de braços: {arm_request}')
        
        if arm_request.status_code == 200:
            data = arm_request.json()
            return data if isinstance(data, list) else []
        
        # Try without nested parameter
        if arm_request.status_code == 500:
            logger.warning("Error 500 with nested=True, trying without nested parameter...")
            arm_request = self._request("GET", "braco", params={"co_protocolo": str(co_protocolo)})
            
            if arm_request.status_code == 200:
                data = arm_request.json()
                return data if isinstance(data, list) else []
            
        raise RuntimeError(f"Error fetching arms: {arm_request.status_code} - {arm_request.text}")
    
    def find_participant(self, *, co_voluntario: int, co_protocolo: int) -> Optional[Dict[str,Any]]:
        """
        Find participant in polotrial /participantes endpoint by co_voluntario and co_protocolo.
        
        :param self: Description
        :param co_voluntario: Description
        :type co_voluntario: int
        :param co_protocolo: Description
        :type co_protocolo: int
        :return: Description
        :rtype: Dict[str, Any] | None
        """
        
        participant_request = self._request("GET", "/participantes", params={"co_voluntario": co_voluntario, "co_protocolo": co_protocolo})
        if participant_request.status_code != 200:
            raise RuntimeError(f"Error querying participant: {participant_request.status_code} - {participant_request.text}")
        data = participant_request.json()
        return data[0] if isinstance(data, list) and data else None
    
    def get_participant(self, participant_id: int) -> Dict[str, Any]:
        """
        Get participant in polotrial /participantes/{id} endpoint by co_voluntario.
        
        
        :param self: Description
        :param participant_id: Description
        :type participant_id: int
        :return: Description
        :rtype: Dict[str, Any]
        """
        
        request = self._request("GET", f"/participantes/{participant_id}")
        if request.status_code != 200:
            raise RuntimeError(f"Error getting participant {participant_id}: {request.status_code} - {request.text}")
        return request.json()
    
    def create_participant(self, payload: Dict[str, Any]) -> Dict[str,Any]:
        """
        If no participant found, create a new participant in polotrial protocol /participantes endpoint.
        
        :param self: Description
        :param payload: Description
        :type payload: Dict[str, Any]
        :return: Description
        :rtype: Dict[str, Any]
        """
        participant_request = self._request("POST", "/participantes", json=payload)
        
        # API bug: sometimes returns 500 but creates the participant.
        if participant_request.status_code in (200, 201):
            return participant_request.json()
        
        # If there was an error, check if the participant was created anyway.
        if participant_request.status_code == 500:
            logger.warning("Polotrial returned 500 when creating participant. Checking if it was created anyway...")
            
            # Try to find the participant by co_voluntario and co_protocolo.
            co_voluntario = payload.get("co_voluntario")
            co_protocolo = payload.get("co_protocolo")
            
            if co_voluntario and co_protocolo:
                existing = self.find_participant(co_voluntario=co_voluntario, co_protocolo=co_protocolo)
                if existing:
                    logger.info("Participant was created despite 500 error: %s", existing["id"])
                    return existing
            # If not found, raise the original error.
        raise RuntimeError(f"Error creating participant: {participant_request.status_code} - {participant_request.text}")
                    
    
    def list_participant_visits(self, *, co_participante: int) -> list[Dict[str, Any]]:
        """
        List all visits for a participant from polotrial /participante_visita endpoint.
        
        :param self: Description
        :param co_participante: Description
        :type co_participante: int
        :return: Description
        :rtype: list[Dict[str, Any]]
        """
        visits_request = self._request("GET", "/participante_visita", params={"co_participante": co_participante})
        if visits_request.status_code != 200:
            raise RuntimeError(f"Error fetching participant visits: {visits_request.status_code} - {visits_request.text}")
        data = visits_request.json()
        return data if isinstance(data, list) else []
    
    def get_participant_visit(self, participante_visita_id: int) -> Dict[str, Any]:
        """
        Get a specific visit for a participant from polotrial /participante_visita endpoint.
        
        :param self: Description
        :param co_participante: Description
        :type co_participante: int
        :param co_visita: Description
        :type co_visita: int
        :return: Description
        :rtype: Dict[str, Any] | None
        """
        visit_request = self._request("GET", f"/participante_visita/{participante_visita_id}")
        if visit_request.status_code != 200:
            raise RuntimeError(f"Error fetching participant visit: {visit_request.status_code} - {visit_request.text}")
        return visit_request.json()
    
    def list_participant_visit_procedures(self, *, co_participante_visita: int) -> list[Dict[str, Any]]:
        """
        List all procedures for a participant visit from polotrial /participante_visita_procedimento endpoint.
        
        :param self: Description
        :param co_participante_visita: Description
        :type co_participante_visita: int
        :return: Description
        :rtype: list[Dict[str, Any]]
        """
        procedures_request = self._request(
            "GET", 
            "/participante_visita_procedimento", 
            params={
                "co_participante_visita": co_participante_visita,
                "nested": "true" # Try to get nested procedure data in the same requests
            
            }
        )
        if procedures_request.status_code != 200:
            raise RuntimeError(f"Error fetching participant visit procedures: {procedures_request.status_code} - {procedures_request.text}")
        data = procedures_request.json()
        return data if isinstance(data, list) else []
    
    def list_protocol_procedures(self, *, co_protocolo: int) -> list[Dict[str, Any]]:
        """
        List all procedures for a protocol from polotrial /protocolo_procedimento endpoint.
        
        :param self: Description
        :param co_protocolo: Description
        :type co_protocolo: int
        :return: Description
        :rtype: list[Dict[str, Any]]
        """
        procedures_request = self._request("GET", "/protocolo_procedimento", params={"co_protocolo": co_protocolo})
        if procedures_request.status_code != 200:
            raise RuntimeError(f"Error fetching protocol procedures: {procedures_request.status_code} - {procedures_request.text}")
        data = procedures_request.json()
        return data if isinstance(data, list) else []
    
    def  update_participant_visit_procedure(self, procedure_id: int, payload: Dict[str, Any]) -> Dict[str,Any]:
        """
        Update a specific procedure for a participant visit in polotrial /participante_visita_procedimento endpoint.
        
        :param self: Description
        :param procedure_id: Description
        :type procedure_id: int
        :param payload: Description
        :type payload: Dict[str, Any]
        :return: Description
        :rtype: Dict[str, Any]
        """
        procedure_request = self._request("PUT", f"/participante_visita_procedimento/{procedure_id}", json=payload)
        if procedure_request.status_code != 200:
            raise RuntimeError(f"Error updating participant visit procedure: {procedure_request.status_code} - {procedure_request.text}")
        return procedure_request.json()
    
    def find_person_by_name(self, ds_nome: str) -> Optional[Dict[str, Any]]:
        """
        Search in Polotrial /pessoa?ds_nome=... endpoint for a person in ds_nome field.
        """
        
        person_request = self._request("GET", "/pessoas", params={"ds_nome": ds_nome})
        if person_request.status_code != 200:
            raise RuntimeError(f"Error querying person: {person_request.status_code} - {person_request.text}")
        data = person_request.json()
        return data[0] if isinstance(data, list) and data else None
    
    def create_procedure_executor(self, payload: Dict[str, Any]) -> Dict[str,Any]:
        """
        Create a new procedure executor in Polotrial /participante_visita_procedimento_executor endpoint.
        """
        executor_request= self._request("POST", "/participante_visita_procedimento_executor", json = payload)
        if executor_request.status_code not in (200, 201):
            raise RuntimeError(f"Error creating procedure executor: {executor_request.status_code} - {executor_request.text}")
        return  executor_request.json()
    
    def list_procedure_executors(self, co_participante_visita_procedimento: int) -> list[Dict[str, Any]]:
        """
        GET /participante_visita_procedimento_executor?co_participante_visita_procedimento=...

        Returns a list of executors already linked to the procedure.
        """
        
        r = self._request(
            "GET",
            "/participante_visita_procedimento_executor",
            params = {
                "co_participante_visita_procedimento": co_participante_visita_procedimento
            },
        )
        if r.status_code != 200:
            raise RuntimeError(f"Error querying procedure executors: {r.status_code} - {r.text}")
        data = r.json()
        return data if isinstance(data, list) else []
    
    def update_participant(self, participant_id: int, payload: Dict[str, Any]) -> Dict[str,Any]:
        """
        PUT /participantes/{id}
        Update participant data (ex: co_braco, atualizar_agenda)
        """
        request = self._request("PUT", f"/participantes/{participant_id}", json=payload)
        if request.status_code != 200:
            raise RuntimeError(f"Error updating participant {participant_id}: {request.status_code} {request.text}")
        return request.json()
    
    def update_participant_visit(self, participante_visita_id: int, payload: Dict[str, Any]) -> Dict[str, Any]:
        """
        PUT /participante_visita/{id}
        Update participant visit data (ex: date, status etc.)
        
        :param participante_visita_id: ID of the participant visit to update
        :param payload: Data to update the participant visit with
        :return: Updated participant visit data
        :rtype: Dict[str, Any]
        
        """
        request = self._request("PUT", f"/participante_visita/{participante_visita_id}", json=payload)
        if request.status_code != 200:
            raise RuntimeError(f"Error updating participant visit {participante_visita_id}: {request.status_code} {request.text}")
        return request.json()