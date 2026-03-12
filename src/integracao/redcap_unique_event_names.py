import os
import requests
from dotenv import load_dotenv

load_dotenv(override=True)

url = os.getenv("REDCAP_API_URL")
token = os.getenv("REDCAP_API_KEY")
print(url)
print(token)

if not url or not token:
    raise ValueError("REDCAP_API_URL ou REDCAP_API_KEY não estão definidos no .env")

headers = {
    "User-Agent": "Mozilla/5.0 (compatible; redcap-client/1.0)",
    "Accept": "application/json",
}

data = {
    'token': f'{token}',
    'content': 'event',
    'format': 'json',
    'returnFormat': 'json'
}

try:
    redcap_request = requests.post(url, data=data, headers=headers, timeout=30)
    print("HTTP Status:", redcap_request.status_code)
    print(redcap_request.text)  # melhor que redcap_request.json() para debug inicial
    redcap_request.raise_for_status()
    print(redcap_request.json())
except requests.exceptions.Timeout:
    print("Timeout: o servidor não respondeu em 30s.")
except requests.exceptions.RequestException as e:
    print("Erro na requisição:", e)
    

unique_event_names = set()
try:
    events = redcap_request.json()
    for event in events:
        event_name = event.get('event_name')
        if event_name:
            unique_event_names.add(event_name)
    print("Unique Event Names:", unique_event_names)
except ValueError:
    print("Erro ao processar a resposta JSON.")



