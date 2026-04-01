
# Integração REDCap ↔ PoloTrial (IMOX)

Script para integração automatizada entre o sistema REDCap e PoloTrial, com ativação via webhook e CLI para sincronização de dados de participantes e eventos de estudo clínico.

## Sumário
- [Descrição](#descrição)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Instalação](#instalação)
- [Configuração](#configuração)
- [Execução](#execução)
- [Principais Módulos](#principais-módulos)
- [Fluxo de Integração](#fluxo-de-integração)
- [Exemplo de Uso](#exemplo-de-uso)
- [Contribuição](#contribuição)--
- [Contato](#contato)

---

## Descrição
Este projeto realiza a integração entre o REDCap (sistema de coleta de dados clínicos) e o PoloTrial (gestão de estudos), automatizando o envio de dados de participantes e eventos via API. Permite disparo por webhook (FastAPI) ou linha de comando (CLI), facilitando a interoperabilidade entre plataformas.

## Estrutura do Projeto

```
integracao_imox/
├── pyproject.toml
├── requirements.txt
├── run_webhook.py
├── src/
│   └── integracao/
│       ├── cli.py
│       ├── webhook.py
│       ├── dispatch.py
│       ├── sync_engine.py
│       ├── polotrial_client.py
│       ├── redcap_client.py
│       ├── config/
│       ├── events/
│       ├── mappings/
│       └── ...
└── ...
```

## Instalação
1. **Clone o repositório:**
	```bash
	git clone <repo_url>
	cd integracao_imox
	```
2. **Crie e ative um ambiente virtual:**
	```bash
	python3 -m venv .venv
	source .venv/bin/activate
	```
3. **Instale as dependências:**
	```bash
	pip install -r requirements.txt
	```

## Configuração
Crie um arquivo `.env` na raiz do projeto com as variáveis necessárias para acesso às APIs do REDCap e PoloTrial. Exemplo:

```
REDCAP_API_URL=https://<redcap_url>/api/
REDCAP_API_KEY=<seu_token_redcap>
POLOTRIAL_API_URL=https://<polotrial_url>/api/
POLOTRIAL_USERNAME=<usuario>
POLOTRIAL_PASSWORD=<senha>
PROTOCOL_NICKNAME=IMOX
```

Outras variáveis de configuração podem ser ajustadas em `src/integracao/config/config.py`.

## Execução

### 1. Webhook (API FastAPI)
Inicie o servidor para receber notificações do REDCap:

```bash
python run_webhook.py --host 0.0.0.0 --port 8000
```
O endpoint principal estará disponível em `/`.

### 2. Linha de Comando (CLI)
Execute a sincronização manual para um registro/evento específico:

```bash
python -m integracao.cli --record-id <ID> --event <EVENTO>
```

## Principais Módulos

- **webhook.py**: Inicializa a API FastAPI, gerencia ciclo de vida e dependências globais.
- **cli.py**: Interface de linha de comando para sincronização manual.
- **dispatch.py**: Roteia eventos do REDCap para funções de sincronização específicas.
- **redcap_client.py**: Cliente para comunicação com a API do REDCap.
- **polotrial_client.py**: Cliente para autenticação e envio de dados ao PoloTrial.
- **sync_engine.py**: Funções utilitárias para manipulação e transformação de dados.
- **config/**: Configurações de eventos, braços, variáveis e mapeamentos.
- **events/**: Implementações de sincronização para diferentes tipos de eventos.
- **mappings/**: Mapas de códigos e valores entre sistemas.

## Fluxo de Integração

1. O REDCap dispara um webhook para o endpoint FastAPI após atualização de registro/evento.
2. O sistema identifica o tipo de evento e roteia para a função de sincronização adequada.
3. Os dados são extraídos do REDCap, transformados e enviados para o PoloTrial via API.
4. Logs são gerados para auditoria e troubleshooting.

## Exemplo de Uso

**Webhook:**
1. Configure o REDCap para enviar notificações para `http://<host>:8000/`.
2. O sistema processará automaticamente os eventos recebidos.

**CLI:**
```bash
python -m integracao.cli --record-id <número do indivíduo no redcap> --event <redcap event_name>
```

## Contribuição
Contribuições são bem-vindas! Abra issues ou pull requests para sugerir melhorias ou reportar problemas.

## Contato
Dúvidas ou suporte: [Eduardo Augusto Rabelo Socca/eduardo.socca@svriglobal.com]

---