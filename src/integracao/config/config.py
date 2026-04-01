# Visitas REDCAP:
V1_EVENT_NAME="visita_1__screenin_arm_1"
V2_EVENT_NAME="visita_2__randomiz_arm_1"
V3_EVENT_NAME="visita_3_arm_1"
V4_EVENT_NAME="visita_4_arm_1"
V5_EVENT_NAME="visita_5_arm_1"
PRE_INSERTION_EVENT_NAME="visita_prinsero_arm_1"
PARTICIPANT_STATUS_EVENT_NAME="status_do_particip_arm_1"
H24_EVENT_NAME="24_horas_arm_1"
W1_EVENT_NAME="1_semana_arm_1"
W2_EVENT_NAME="2_semanas_arm_1"
W3_EVENT_NAME="3_semanas_arm_1"
W4_EVENT_NAME="4_semanas_arm_1"
W8_EVENT_NAME="8_semanas_arm_1"
W12_EVENT_NAME="12_semanas_arm_1"
W16_EVENT_NAME="16_semanas_arm_1"
W20_EVENT_NAME="20_semanas_arm_1"
W24_EVENT_NAME="24_semanas_arm_1"
NP_EVENT_NAME="visita_no_programa_arm_1"
CIRURGIA_LCA_REDCAP_EVENT_NAME="visita_1__screenin_arm_1"



# Visitas Polotrial:
V1_POLOTRIAL_EVENT_NAME="VS/V1"
V2_POLOTRIAL_EVENT_NAME="VR/V2"
V3_POLOTRIAL_EVENT_NAME="V3"
V4_POLOTRIAL_EVENT_NAME="V4"
V5_POLOTRIAL_EVENT_NAME="V5/VF"
VNP_POLOTRIAL_EVENT_NAME="Não Programada"
PRE_INSERTION_POLOTRIAL_EVENT_NAME="Pré-inserção do implante de oxandrolona"
H24_POLOTRIAL_EVENT_NAME="24H após a inserção do implante de oxandrolona" 	
W1_POLOTRIAL_EVENT_NAME="1 Semana após a inserção do implante de oxandrolona"
W2_POLOTRIAL_EVENT_NAME="2 semanas após a inserção do implante de oxandrolona"
W3_POLOTRIAL_EVENT_NAME="3 semanas após a inserção do implante de oxandrolona"
W4_POLOTRIAL_EVENT_NAME="4 semanas após a inserção do implante de oxandrolona"
W8_POLOTRIAL_EVENT_NAME="8 semanas após a inserção do implante de oxandrolona"
W12_POLOTRIAL_EVENT_NAME="12 semanas após a inserção do implante de oxandrolona"
W16_POLOTRIAL_EVENT_NAME="16 semanas após a inserção do implante de oxandrolona"
W20_POLOTRIAL_EVENT_NAME="20 semanas após a inserção do implante de oxandrolona"
W24_POLOTRIAL_EVENT_NAME="24 semanas após a inserção do implante de oxandrolona"
CIRURGIA_DT_EVENT_NAME="Data da Cirurgia de LCA"



# Braços Polotrial:
TRIAGEM_ARM_NAME ="IMOX Versão nº1 - TRIAGEM"
OTHER_ARM_NAME ="IMOX Versão nº1"
PK_ARM_NAME ="IMOX Versão nº1 - SUBGRUPO PK"

# Mapeamento de randomização (chave:grupo_int)
ARM_MAPPING="1:1,Não alocado:1,2:2,Alocado:2"

# Padrões de braços PoloTrial
ARM_1_PATTERN_ENV="OTHER_ARM_NAME"
ARM_1_LABEL="Não alocado"
ARM_2_PATTERN_ENV="PK_ARM_NAME"
ARM_2_LABEL="Alocado"



#VARIÁVEIS REDCAP
NOME="record_id"
INICIAIS="demografia_iniciais"
DT_NASCIMENTO="demografia_data_nascimento"
# EMAIL=""
DT_INCLUSAO="revisao_dt_visita"
PARTICIPANT_ID="record_id"
NUMERO_SCREENING="record_id"
DATA_ESTIMADA_VISITA="revisao_dt_visita"
DATA_REALIZADA_VISITA="revisao_dt_visita"
GENERO="demografia_sexo"
RACA="demografia_raca"
CENTRO="demografia_centro"
DT_VISITA="revisao_dt_visita"
RANDOMIZACAO="randomizacao_alocacao_pk"
DT_RANDOMIZACAO="randomizacao_dt_visita"
PARTICIPANT_STATUS="status_pp_status"
CIRURGIA_LCA_DT_FIELD = "form_medico_ruptura_lca_q4"