from typing import List, Dict, Optional

V1_POLOTRIAL_PROCEDURES_MAP: List[Dict[str, Optional[str]]] = [
    {
        "procedure_name": r"Teste\s+de\s+gravidez",
        # "co_procedimento": "175",
        "redcap_check_field": "coleta_gravidez",
        "redcap_date_field": "coleta_dt_visita"
    },
    
    {
        "procedure_name": r"Exame\s+f[ií]sico",
        # "co_procedimento": "76", 
        "redcap_check_field": "form_medico_ex_fisico_q0",
        "redcap_date_field": "form_medico_dt_visita"
    },
    {
        "procedure_name": r"Consulta\s+M[eéEÉ]dica",
        # "co_procedimento": "70",
        # Neste caso, a data de checagem é a própria data de visita.
        "redcap_check_field": "form_medico_dt_rubrica",
        "redcap_date_field": "form_medico_dt_rubrica"

    },
    {
        "procedure_name": r"Hist[oóOÓ]ria\s+M[éeEÉ]dica",
        # "co_procedimento": "4", 
        "redcap_check_field": "form_medico_revisao6",
        "redcap_date_field": "form_medico_dt_visita"
    },
    { # regex Registro de uso de medicações pré-estudo e concomitantes - ok
        "procedure_name": r"Registro\s+de\s+uso\s+de\s+Medicações\s+Pr[éÉ]-Estudo\s+e\s+Concomitantes",
        # "co_procedimento": "144", 
        "redcap_check_field": "form_medico_revisao4",
        "redcap_date_field": "form_medico_dt_visita"
    },
    {
        "procedure_name": r"Sinais\s+vitais",
        # "co_procedimento": "7", 
        "redcap_check_field": "form_medico_sv1",
        "redcap_date_field": "form_medico_dt_visita"
    },
    {
        "procedure_name": r"Dados\s+demogr[aáàâãäå]ficos",
        # "co_procedimento": "61", 
        "redcap_check_field": "demografia_dt_visita",
        "redcap_date_field": "demografia_dt_visita"
    },
    {
        "procedure_name": r"Termo\s+de\s+consentimento\s+Livre\s+e\s+Esclarecido",
        # "co_procedimento": "1", 
        "redcap_check_field": "tcle_pergunta_c",
        "redcap_date_field": "tcle_dt_visita_aplicacao"
    },
    {
        "procedure_name": r"Avalia[cç][aã]o\s+dos\s+crit[eé]rios\s+de\s+inclus[aã]o/exclus[aã]o",
        # "co_procedimento": "2", 
        "redcap_check_field": "form_medico_revisao",
        "redcap_date_field": "form_medico_dt_visita"
    },
    {
        "procedure_name": r"Orienta[cç][oõ]es\s+para\s+programa\s+fisioter[aá]pico\s+para\s+reabilita[cç][aã]o\s+p[oó]s-operat[oó]ria",
        "redcap_check_field": "rando_q1_v2",
        "redcap_date_field": "revisao_dt_visita"
    },
    {
        "procedure_name": r"Monitoramento\s+de\s+eventos\s+adversos",
        "redcap_check_field": "form_medico_revisao7",
        "redcap_date_field": "form_medico_dt_visita"
    },
    {
        "procedure_name": r"Orienta[cç][oõ]es\s+para\s+uso\s+de\s+m[eé]todos\s+contraceptivos",
        "redcap_check_field": "form_medico_gravidez_q3",
        "redcap_date_field": "form_medico_dt_visita"
    },
    {
        "procedure_name": r"Dispensa[cç][aã]o\s+de\s+medica[cç][aã]o\s+para\s+tromboprofilaxia\s+p[oó]s-cirurgica",
        # "co_procedimento": "250", 
        "redcap_check_field": "form_medico_revisao1",
        "redcap_date_field": "form_medico_dt_visita"
    },
    {
        "procedure_name": r"Question[aá]rio\s+IPAQ",
        # "co_procedimento": "59", 
        "redcap_check_field": "ipaq_dt_visita",
        "redcap_date_field": "ipaq_dt_visita"
    },
    {
        "procedure_name": r"Globulina\s+Ligadora\s+De\s+Hormonios\s+Sexuais",
        # "co_procedimento": "298", 
        "redcap_check_field": "lab_shbg",
        "redcap_date_field": "lab_dt_visita"
    },
    {
        "procedure_name": r"Hemograma\s+completo-sangue",
        # "co_procedimento": "298", 
        "redcap_check_field": "lab_hematocrito",
        "redcap_date_field": "hematocrito_dt"
    },
    {
        "procedure_name": r"Creatinina\s+sérica-sangue",
        "redcap_check_field": "lab_creatinina",
        "redcap_date_field": "lab_dt_visita"
    },
    {
        "procedure_name": r"Bilirrubina\s+s[eé]rica\s+\(total\)-sangue",
        "redcap_check_field": "lab_bilirrubina",
        "redcap_date_field": "lab_dt_visita"
    },
    {
        "procedure_name": r"Transaminase\s+glut[aâ]mico\s+pir[uú]vica/alanina\s+aminotransferase\s+\(TGP/ALT\)-sangue",
        "redcap_check_field": "lab_tgp",
        "redcap_date_field": "lab_dt_visita"
    },
    {
        "procedure_name": r"Albumina-Sangue",
        "redcap_check_field": "lab_albumina",
        "redcap_date_field": "lab_dt_visita"
    },
    {
        "procedure_name": r"Ant[ií]geno\s+prost[aá]tico\s+espec[ií]fico\s+livre\s+\(PSA\)-sangue",
        "redcap_check_field": "lab_psa",
        "redcap_date_field": "lab_dt_visita"
    },

    {
        "procedure_name": r"Concentra[cç][aã]'o\s+s[eé]rica\s+de\s+oxandrolona\s+e\s+farmacocin[eé]tica",
        "co_procedimento": "129",
        "redcap_check_field": "",
        "redcap_date_field": ""
    }
    

]

V2_POLOTRIAL_PROCEDURES_MAP: List[Dict[str, Optional[str]]] = [
    {
        "procedure_name": r"Avalia[cç][aã]o\s+dos\s+crit[eé]rios\s+de\s+inclus[aã]o/exclus[aã]o",
        "co_procedimento": "2",
        "redcap_check_field": "form_medico_revisao",
        "redcap_date_field": "form_medico_dt_visita"
    },
    
    {
        "procedure_name": r"Exame\s+f[ií]sico",
        "co_procedimento": "76",
        "redcap_check_field": "form_medico_ex_fisico_q0",
        "redcap_date_field": "form_medico_dt_visita"
    },
    
    {
        "procedure_name": r"Sinais\s+vitais",
        "co_procedimento": "7",
        "redcap_check_field": "form_medico_sv1",
        "redcap_date_field": "form_medico_dt_visita"
    },
    
    {
        "procedure_name": r"Registro\s+de\s+uso\s+de\s+medica[cç][oõ]es\s+pr[eé]-estudo\s+e\s+concomitantes",
        "co_procedimento": "144",
        "redcap_check_field": "form_medico_revisao4",
        "redcap_date_field": "form_medico_dt_visita"
    },
        
    {
        "procedure_name": r"Teste\s+de\s+gravidez",
        "co_procedimento": "175",
        "redcap_check_field": "coleta_gravidez",
        "redcap_date_field": "coleta_dt_visita"
    },
        
    {
        "procedure_name": r"Orienta[çc][õo]es para programa fisioter[aá]pico para reabilita[cç][aã]o p[oó]s-operat[oó]ria",
        "co_procedimento": "319",
        "redcap_check_field": "rando_q1_v2",
        "redcap_date_field": "revisao_dt_visita"
    },
    
    {
        "procedure_name": r"Orienta[çc][õo]es para uso de m[eé]todos contraceptivos",
        "co_procedimento": "327",
        "redcap_check_field": "form_medico_gravidez_q3",
        "redcap_date_field": "form_medico_dt_visita"
    },
    
    {
        "procedure_name": r"Monitoramento\s+de\s+eventos\s+adversos",
        "co_procedimento": "86",
        "redcap_check_field": "form_medico_revisao7",
        "redcap_date_field": "form_medico_dt_visita"
    },
    
    {
        "procedure_name": r"Inserç[aã]o subd[eé]rmica do implante absorv[ií]vel",
        "co_procedimento": "326",
        "redcap_check_field": "form_medico_rando_dth_pellet",
        "redcap_date_field": "form_medico_rando_dth_pellet"
    },
    
    {
        "procedure_name": r"Bioimped[aâ]ncia",
        "co_procedimento": "325",
        "redcap_check_field": "aval_corp_bioimpedancia",
        "redcap_date_field": "aval_corp_dt_visita"
    },
    
    {
        "procedure_name": r"Dinamometria isom[eé]trica",
        "co_procedimento": "323",
        "redcap_check_field": "fisio_isometria_q5",
        "redcap_date_field": "fisio_dt_visita"
    },
    
    {
        "procedure_name": r"Question[aá]rio IPAQ (International Phyisical Ativity Questionnaire)",
        "co_procedimento": "59",
        "redcap_check_field": "rando_q2_v2",
        "redcap_date_field": "revisao_dt_visita"
    },
    
    {
        "procedure_name": r"Question[aá]rio Lysholm Knee Scoring Scale",
        "co_procedimento": "59",
        "redcap_check_field": "rando_q3_v2",
        "redcap_date_field": "revisao_dt_visita"
    },
    
    {
        "procedure_name": r"Question[aá]rio Short Form-12 (SF-36SF-36)",
        "co_procedimento": "59",
        "redcap_check_field": "rando_q4_v2",
        "redcap_date_field": "revisao_dt_visita"
    },
    
    {
        "procedure_name": r"Question[aá]rio GAD-7",
        "co_procedimento": "59",
        "redcap_check_field": "rando_q5_v2",
        "redcap_date_field": "revisao_dt_visita"
    },
    
    {
        "procedure_name": r"Question[aá]rio PHQ9",
        "co_procedimento": "59",
        "redcap_check_field": "rando_q6_v2",
        "redcap_date_field": "revisao_dt_visita"
    },
    
    {
        "procedure_name": r"Question[aá]rio Patient Acceptable Symptom State (PAS)",
        "co_procedimento": "59",
        "redcap_check_field": "rando_q7_v2",
        "redcap_date_field": "revisao_dt_visita"
    },
    
    {
        "procedure_name": r"Consulta\s+M[eé]dica",
        "co_procedimento": "70",
        "redcap_check_field": "form_medico_rubrica",
        "redcap_date_field": "form_medico_dt_rubrica"
    },
    
    {
        "procedure_name": r"Consulta Fisioterapeuta",
        "co_procedimento": "320",
        "redcap_check_field": "fisio_dt_visita",
        "redcap_date_field": "fisio_dt_visita"
    },
    
    {
        "procedure_name": r"Reconsentimento",
        "co_procedimento": "1",
        "redcap_check_field": "tcle_reconcentimento",
        "redcap_date_field": "tcle_dt_visita_aplicacao"
    },
    {
        "procedure_name": r"Hemograma\s+completo-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_hematocrito",
        "redcap_date_field": "lab_dt_visita"
    },
    {
        "procedure_name": r"Creatinina\s+sérica-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_creatinina",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Ureia\s+s[eé]rica-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_ureia",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Bilirrubina\s+s[eé]rica\s+(total)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_bilirrubina",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Transaminase\s+glut[aâ]mico\s+oxalac[eé]tica/aspartato\s+aminotransferase\s+(TGO/AST)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_tgo",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Transaminase\s+glut[aâ]mico\s+pir[uú]vica/alanina\s+aminotransferase\s+(TGP/ALT)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_tgp",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Fosfatase\s+alcalina\s+(FA)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_fa",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Gama\s+glutamil\s+transferase\s+(GGT)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_ggt",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Creatinina\s+quinase\s+ou\s+Creatinina\s+fosfoquinase\s+(CK\s+ou\s+CPK)-\s+sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_cpk",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Antígeno\s+prost[aá]tico\s+espec[ií]fico\s+livre\s+(PSA)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_psa",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Colesterol-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_colesterol",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Low-density\s+lipoprotein\s+(LDL)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_ldl",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"High-density\s+lipoprotein\s+(HDL)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_hdl",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Lipoproteína\s+a\s+-\s+sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_lipoproteina",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Testosterona\s+total",
        "co_procedimento": "298",
        "redcap_check_field": "lab_testo_total",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Testosterona\s+livre\s+sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_testo_livre",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Horm[oô]nio\s+fol[ií]culo-estimulante\s+(FSH)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_fsh",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Horm[oô]nio\s+luteinizante\s+(LH)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_lh",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"D[íi]mero\s+D-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_dd",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Prote[ií]na\s+S\s+livre-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_prot_s",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Globulina\s+Ligadora\s+De\s+Horm[oô]nios\s+Sexuais\s+(SHBG)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_shbg",
        "redcap_date_field": "lab_dt_visita"
    }
]

V3_PROCEDURES_MAP: List[Dict[str, Optional[str]]] = [
    {
        "procedure_name": r"Exame\s+f[ií]sico",
        "co_procedimento": "76",
        "redcap_check_field": "form_medico_ex_fisico_q0",
        "redcap_date_field": "form_medico_dt_visita"
    },
    
    {
        "procedure_name": r"Sinais\s+vitais",
        "co_procedimento": "7",
        "redcap_check_field": "form_medico_sv1",
        "redcap_date_field": "form_medico_dt_visita"
    },
    
    {
        "procedure_name": r"Registro\s+de\s+uso\s+de\s+medica[cç][oõ]es\s+pr[eé]-estudo\s+e\s+concomitantes",
        "co_procedimento": "144",
        "redcap_check_field": "form_medico_revisao4",
        "redcap_date_field": "form_medico_dt_visita"
    },
    
    {
        "procedure_name": r"Hemograma\s+completo-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_hematocrito",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Creatinina\s+sérica-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_creatinina",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Ureia\s+s[eé]rica-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_ureia",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Bilirrubina\s+s[eé]rica\s+(total)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_bilirrubina",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Transaminase\s+glut[aâ]mico\s+oxalac[eé]tica/aspartato\s+aminotransferase\s+(TGO/AST)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_tgo",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Transaminase\s+glut[aâ]mico\s+pir[uú]vica/alanina\s+aminotransferase\s+(TGP/ALT)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_tgp",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Fosfatase\s+alcalina\s+(FA)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_fa",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Gama\s+glutamil\s+transferase\s+(GGT)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_ggt",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Creatinina\s+quinase\s+ou\s+Creatinina\s+fosfoquinase\s+(CK\s+ou\s+CPK)-\s+sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_cpk",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Antígeno\s+prost[aá]tico\s+espec[ií]fico\s+livre\s+(PSA)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_psa",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Colesterol-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_colesterol",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Low-density\s+lipoprotein\s+(LDL)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_ldl",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"High-density\s+lipoprotein\s+(HDL)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_hdl",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Lipoproteína\s+a\s+-\s+sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_lipoproteina",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Testosterona\s+total",
        "co_procedimento": "298",
        "redcap_check_field": "lab_testo_total",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Testosterona\s+livre\s+sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_testo_livre",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Horm[oô]nio\s+fol[ií]culo-estimulante\s+(FSH)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_fsh",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Horm[oô]nio\s+luteinizante\s+(LH)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_lh",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"D[íi]mero\s+D-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_dd",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Prote[ií]na\s+S\s+livre-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_prot_s",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Globulina\s+Ligadora\s+De\s+Horm[oô]nios\s+Sexuais\s+(SHBG)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_shbg",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Teste\s+de\s+gravidez",
        "co_procedimento": "175",
        "redcap_check_field": "coleta_gravidez",
        "redcap_date_field": "coleta_dt_visita"
    },
    
    {
        "procedure_name": r"Orienta[cç][oõ]es\s+para\s+programa\s+fisioter[aá]pico\s+para\s+reabilita[cç][aã]o\s+p[oó]s-operat[oó]ria",
        "co_procedimento": "319",
        "redcap_check_field": "rando_q1_v2",
        "redcap_date_field": "revisao_dt_visita"
    },
    
    {
        "procedure_name": r"Orienta[cç][oõ]es\s+para\s+uso\s+de\s+m[ée]todos\s+contraceptivos",
        "co_procedimento": "327",
        "redcap_check_field": "form_medico_gravidez_q3",
        "redcap_date_field": "form_medico_dt_visita"
    },
    
    {
        "procedure_name": r"Monitoramento\s+de\s+eventos\s+adversos",
        "co_procedimento": "86", 
        "redcap_check_field": "form_medico_revisao7",
        "redcap_date_field": "form_medico_dt_visita"
    },
    
    {
        "procedure_name": r"Consulta\s+M[eé]dica",
        "co_procedimento": "70",
        "redcap_check_field": "form_medico_rubrica",
        "redcap_date_field": "form_medico_dt_rubrica"
    },
        
            
    {
        "procedure_name": r"Reconsentimento",
        "co_procedimento": "1",
        "redcap_check_field": "tcle_reconcentimento",
        "redcap_date_field": "tcle_dt_visita_aplicacao"
    }   
]

V4_PROCEDURES_MAP: List[Dict[str, Optional[str]]] = [
    {
        "procedure_name": r"Exame\s+f[ií]sico",
        "co_procedimento": "76",
        "redcap_check_field": "form_medico_ex_fisico_q0",
        "redcap_date_field": "form_medico_dt_visita"
    },
    
    {
        "procedure_name": r"Sinais\s+vitais",
        "co_procedimento": "7",
        "redcap_check_field": "form_medico_sv1",
        "redcap_date_field": "form_medico_dt_visita"
    },
    
    {
        "procedure_name": r"Registro\s+de\s+uso\s+de\s+medica[cç][oõ]es\s+pr[eé]-estudo\s+e\s+concomitantes",
        "co_procedimento": "144",
        "redcap_check_field": "form_medico_revisao4",
        "redcap_date_field": "form_medico_dt_visita"
    },
    
    {
        "procedure_name": r"Hemograma\s+completo-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_hematocrito",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Creatinina s[eé]rica-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_creatinina",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Ureia\s+s[eé]rica-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_ureia",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Bilirrubina\s+s[eé]rica\s+(total)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_bilirrubina",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Transaminase\s+glut[aâ]mico\s+oxalac[eé]tica/aspartato\s+aminotransferase\s+(TGO/AST)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_tgo",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Transaminase\s+glut[aâ]mico\s+pir[uú]vica/alanina\s+aminotransferase\s+(TGP/ALT)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_tgp",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Fosfatase\s+alcalina\s+(FA)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_fa",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Gama\s+glutamil\s+transferase\s+(GGT)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_ggt",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Creatinina\s+quinase\s+ou\s+Creatinina\s+fosfoquinase\s+(CK\s+ou\s+CPK)-\s+sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_cpk",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Antígeno\s+prost[aá]tico\s+espec[ií]fico\s+livre\s+(PSA)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_psa",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Colesterol-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_colesterol",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Low-density\s+lipoprotein\s+(LDL)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_ldl",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"High-density\s+lipoprotein\s+(HDL)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_hdl",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Lipoproteína\s+a\s+-\s+sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_lipoproteina",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Testosterona\s+total",
        "co_procedimento": "298",
        "redcap_check_field": "lab_testo_total",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Testosterona\s+livre\s+sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_testo_livre",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Horm[oô]nio\s+fol[ií]culo-estimulante\s+(FSH)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_fsh",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Horm[oô]nio\s+luteinizante\s+(LH)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_lh",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"D[íi]mero\s+D-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_dd",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Prote[ií]na\s+S\s+livre-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_prot_s",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Globulina\s+Ligadora\s+De\s+Horm[oô]nios\s+Sexuais\s+(SHBG)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_shbg",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Teste\s+de\s+gravidez",
        "co_procedimento": "175",
        "redcap_check_field": "coleta_gravidez",
        "redcap_date_field": "coleta_dt_visita"
    },
    
    {
        "procedure_name": r"Orienta[cç][oõ]es\s+para\s+programa\s+fisioter[aá]pico\s+para\s+reabilita[cç][aã]o\s+p[oó]s-operat[oó]ria",
        "co_procedimento": "319",
        "redcap_check_field": "rando_q1_v2",
        "redcap_date_field": "revisao_dt_visita"
    },
    
    {
        "procedure_name": r"Orienta[cç][oõ]es\s+para\s+uso\s+de\s+m[ée]todos\s+contraceptivos",
        "co_procedimento": "327",
        "redcap_check_field": "form_medico_gravidez_q3",
        "redcap_date_field": "form_medico_dt_visita"
    },
    
    {
        "procedure_name": r"Monitoramento\s+de\s+eventos\s+adversos",
        "co_procedimento": "86", 
        "redcap_check_field": "form_medico_revisao7",
        "redcap_date_field": "form_medico_dt_visita"
    },
    
    {
        "procedure_name": r"Consulta\s+M[eé]dica",
        "co_procedimento": "70",
        "redcap_check_field": "form_medico_rubrica",
        "redcap_date_field": "form_medico_dt_rubrica"
    },
        
            
    {
        "procedure_name": r"Reconsentimento",
        "co_procedimento": "1",
        "redcap_check_field": "tcle_reconcentimento",
        "redcap_date_field": "tcle_dt_visita_aplicacao"
    },
    
    {
        "procedure_name": r"Bioimped[aâ]ncia",
        "co_procedimento": "325",
        "redcap_check_field": "aval_corp_bioimpedancia",
        "redcap_date_field": "aval_corp_dt_visita"
    },
    
    {
        "procedure_name": r"Resson[aâ]ncia magn[eé]tica por imagem da coxa",
        "co_procedimento": "324",
        "redcap_check_field": "form_medico_ex_imagem1",
        "redcap_date_field": "form_medico_dt_visita"
    },
    
    {
        "procedure_name": r"Dinamometria isom[eé]trica",
        "co_procedimento": "323",
        "redcap_check_field": "fisio_isometria_q5",
        "redcap_date_field": "fisio_dt_visita"
    },
    
    {
        "procedure_name": r"Y balance test",
        "co_procedimento": "322",
        "redcap_check_field": "fisio_teste_y",
        "redcap_date_field": "fisio_dt_visita"
    },
    
    {
        "procedure_name": r"Question[aá]rio Lysholm Knee Scoring Scale",
        "co_procedimento": "59",
        "redcap_check_field": "rando_q3_v2",
        "redcap_date_field": "revisao_dt_visita"
    },
    
    {
        "procedure_name": r"Question[aá]rio Short Form-12 (SF-36SF-36)",
        "co_procedimento": "59",
        "redcap_check_field": "rando_q4_v2",
        "redcap_date_field": "revisao_dt_visita"
    },
    
    {
        "procedure_name": r"Question[aá]rio GAD-7",
        "co_procedimento": "59",
        "redcap_check_field": "rando_q5_v2",
        "redcap_date_field": "revisao_dt_visita"
    },
    
    {
        "procedure_name": r"Question[aá]rio PHQ9",
        "co_procedimento": "59",
        "redcap_check_field": "rando_q6_v2",
        "redcap_date_field": "revisao_dt_visita"
    },
    
    {
        "procedure_name": r"Question[aá]rio Patient Acceptable Symptom State (PAS)",
        "co_procedimento": "59",
        "redcap_check_field": "rando_q7_v2",
        "redcap_date_field": "revisao_dt_visita"
    },
    
    {
        "procedure_name": r"Consulta Fisioterapeuta",
        "co_procedimento": "320",
        "redcap_check_field": "fisio_dt_visita",
        "redcap_date_field": "fisio_dt_visita"
    }
        
]

V5_PROCEDURES_MAP: List[Dict[str, Optional[str]]] = [
    {
        "procedure_name": r"Exame\s+f[ií]sico",
        "co_procedimento": "76",
        "redcap_check_field": "form_medico_ex_fisico_q0",
        "redcap_date_field": "form_medico_dt_visita"
    },
    
    {
        "procedure_name": r"Sinais\s+vitais",
        "co_procedimento": "7",
        "redcap_check_field": "form_medico_sv1",
        "redcap_date_field": "form_medico_dt_visita"
    },
    
    {
        "procedure_name": r"Registro\s+de\s+uso\s+de\s+medica[cç][oõ]es\s+pr[eé]-estudo\s+e\s+concomitantes",
        "co_procedimento": "144",
        "redcap_check_field": "form_medico_revisao4",
        "redcap_date_field": "form_medico_dt_visita"
    },
    
    {
        "procedure_name": r"Hemograma\s+completo-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_hematocrito",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Creatinina s[eé]rica-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_creatinina",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Ureia\s+s[eé]rica-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_ureia",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Bilirrubina\s+s[eé]rica\s+(total)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_bilirrubina",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Transaminase\s+glut[aâ]mico\s+oxalac[eé]tica/aspartato\s+aminotransferase\s+(TGO/AST)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_tgo",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Transaminase\s+glut[aâ]mico\s+pir[uú]vica/alanina\s+aminotransferase\s+(TGP/ALT)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_tgp",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Fosfatase\s+alcalina\s+(FA)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_fa",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Gama\s+glutamil\s+transferase\s+(GGT)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_ggt",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Creatinina\s+quinase\s+ou\s+Creatinina\s+fosfoquinase\s+(CK\s+ou\s+CPK)-\s+sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_cpk",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Antígeno\s+prost[aá]tico\s+espec[ií]fico\s+livre\s+(PSA)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_cpk",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Colesterol-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_colesterol",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Low-density\s+lipoprotein\s+(LDL)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_ldl",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"High-density\s+lipoprotein\s+(HDL)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_hdl",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Lipoproteína\s+a\s+-\s+sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_lipoproteina",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Testosterona\s+total",
        "co_procedimento": "298",
        "redcap_check_field": "lab_testo_total",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Testosterona\s+livre\s+sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_testo_livre",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Horm[oô]nio\s+fol[ií]culo-estimulante\s+(FSH)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_fsh",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Horm[oô]nio\s+luteinizante\s+(LH)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_lh",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"D[íi]mero\s+D-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_dd",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Prote[ií]na\s+S\s+livre-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_prot_s",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Globulina\s+Ligadora\s+De\s+Horm[oô]nios\s+Sexuais\s+(SHBG)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_shbg",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Teste\s+de\s+gravidez",
        "co_procedimento": "175",
        "redcap_check_field": "coleta_gravidez",
        "redcap_date_field": "coleta_dt_visita"
    },
    
    {
        "procedure_name": r"Orienta[cç][oõ]es\s+para\s+programa\s+fisioter[aá]pico\s+para\s+reabilita[cç][aã]o\s+p[oó]s-operat[oó]ria",
        "co_procedimento": "319",
        "redcap_check_field": "rando_q1_v2",
        "redcap_date_field": "revisao_dt_visita"
    },
    
    {
        "procedure_name": r"Orienta[cç][oõ]es\s+para\s+uso\s+de\s+m[ée]todos\s+contraceptivos",
        "co_procedimento": "327",
        "redcap_check_field": "form_medico_gravidez_q3",
        "redcap_date_field": "form_medico_dt_visita"
    },
    
    {
        "procedure_name": r"Monitoramento\s+de\s+eventos\s+adversos",
        "co_procedimento": "86", 
        "redcap_check_field": "form_medico_revisao7",
        "redcap_date_field": "form_medico_dt_visita"
    },
    
    {
        "procedure_name": r"Consulta\s+M[eé]dica",
        "co_procedimento": "70",
        "redcap_check_field": "form_medico_rubrica",
        "redcap_date_field": "form_medico_dt_rubrica"
    },
        
            
    {
        "procedure_name": r"Reconsentimento",
        "co_procedimento": "1",
        "redcap_check_field": "tcle_reconcentimento",
        "redcap_date_field": "tcle_dt_visita_aplicacao"
    },
    
    {
        "procedure_name": r"Bioimped[aâ]ncia",
        "co_procedimento": "325",
        "redcap_check_field": "aval_corp_bioimpedancia",
        "redcap_date_field": "aval_corp_dt_visita"
    },
    
    {
        "procedure_name": r"Dinamometria isom[eé]trica",
        "co_procedimento": "323",
        "redcap_check_field": "fisio_isometria_q5",
        "redcap_date_field": "fisio_dt_visita"
    },
    
    {
        "procedure_name": r"Y balance test",
        "co_procedimento": "322",
        "redcap_check_field": "fisio_teste_y",
        "redcap_date_field": "fisio_dt_visita"
    },
    
    {
        "procedure_name": r"Question[aá]rio Lysholm Knee Scoring Scale",
        "co_procedimento": "59",
        "redcap_check_field": "rando_q3_v2",
        "redcap_date_field": "revisao_dt_visita"
    },
    
    {
        "procedure_name": r"Question[aá]rio Short Form-12 (SF-36SF-36)",
        "co_procedimento": "59",
        "redcap_check_field": "rando_q4_v2",
        "redcap_date_field": "revisao_dt_visita"
    },
    
    {
        "procedure_name": r"Question[aá]rio GAD-7",
        "co_procedimento": "59",
        "redcap_check_field": "rando_q5_v2",
        "redcap_date_field": "revisao_dt_visita"
    },
    
    {
        "procedure_name": r"Question[aá]rio PHQ9",
        "co_procedimento": "59",
        "redcap_check_field": "rando_q6_v2",
        "redcap_date_field": "revisao_dt_visita"
    },
    
    {
        "procedure_name": r"Question[aá]rio Patient Acceptable Symptom State (PAS)",
        "co_procedimento": "59",
        "redcap_check_field": "rando_q7_v2",
        "redcap_date_field": "revisao_dt_visita"
    },
    
    {
        "procedure_name": r"Avalia[cç][aã]o da Satisfa[cç][aã]o do Participante",
        "co_procedimento": "321",
        "redcap_check_field": "form_medico_satisfacao",
        "redcap_date_field": "form_medico_dt_visita"
    },
    
    {
        "procedure_name": r"Consulta Fisioterapeuta",
        "co_procedimento": "320",
        "redcap_check_field": "fisio_dt_visita",
        "redcap_date_field": "fisio_dt_visita"
    }
    
]

PK_PRE_INSERCAO_PROCEDURES_MAP: List[Dict[str, Optional[str]]] = [
    {
        "procedure_name": r"Concentra[cç][aã]'o\s+s[eé]rica\s+de\s+oxandrolona\s+e\s+farmacocin[eé]tica",
        "co_procedimento": "129",
        "redcap_check_field": "",
        "redcap_date_field": ""
    },
    
    {
        "procedure_name": r"Monitoramento\s+de\s+eventos\s+adversos",
        "co_procedimento": "86", 
        "redcap_check_field": "form_medico_revisao7",
        "redcap_date_field": "form_medico_dt_visita"
    },
    
    { # regex Registro de uso de medicações pré-estudo e concomitantes - ok
        "procedure_name": r"Registro\s+de\s+uso\s+de\s+Medicações\s+Pr[éÉ]-Estudo\s+e\s+Concomitantes",
        "co_procedimento": "144", 
        "redcap_check_field": "form_medico_revisao4",
        "redcap_date_field": "form_medico_dt_visita"
    }
    
]

PK_24H_PROCEDURES_MAP: List[Dict[str, Optional[str]]] = [
    {
        "procedure_name": r"Concentra[cç][aã]'o\s+s[eé]rica\s+de\s+oxandrolona\s+e\s+farmacocin[eé]tica",
        "co_procedimento": "129",
        "redcap_check_field": "",
        "redcap_date_field": ""
    },
    
    {
        "procedure_name": r"Monitoramento\s+de\s+eventos\s+adversos",
        "co_procedimento": "86", 
        "redcap_check_field": "form_medico_revisao7",
        "redcap_date_field": "form_medico_dt_visita"
    },
    
    { # regex Registro de uso de medicações pré-estudo e concomitantes - ok
        "procedure_name": r"Registro\s+de\s+uso\s+de\s+Medicações\s+Pr[éÉ]-Estudo\s+e\s+Concomitantes",
        "co_procedimento": "144", 
        "redcap_check_field": "form_medico_revisao4",
        "redcap_date_field": "form_medico_dt_visita"
    },
    
    {
        "procedure_name": r"Reconsentimento",
        "co_procedimento": "1",
        "redcap_check_field": "tcle_reconcentimento",
        "redcap_date_field": "tcle_dt_visita_aplicacao"
    }
]

PK_1_SEMANA_PROCEDURES_MAP: List[Dict[str, Optional[str]]] = [
    {
        "procedure_name": r"Concentra[cç][aã]'o\s+s[eé]rica\s+de\s+oxandrolona\s+e\s+farmacocin[eé]tica",
        "co_procedimento": "129",
        "redcap_check_field": "",
        "redcap_date_field": ""
    },
    
    {
        "procedure_name": r"Monitoramento\s+de\s+eventos\s+adversos",
        "co_procedimento": "86", 
        "redcap_check_field": "form_medico_revisao7",
        "redcap_date_field": "form_medico_dt_visita"
    },
    
    { # regex Registro de uso de medicações pré-estudo e concomitantes - ok
        "procedure_name": r"Registro\s+de\s+uso\s+de\s+Medicações\s+Pr[éÉ]-Estudo\s+e\s+Concomitantes",
        "co_procedimento": "144", 
        "redcap_check_field": "form_medico_revisao4",
        "redcap_date_field": "form_medico_dt_visita"
    },
    
    {
        "procedure_name": r"Reconsentimento",
        "co_procedimento": "1",
        "redcap_check_field": "tcle_reconcentimento",
        "redcap_date_field": "tcle_dt_visita_aplicacao"
    }
]

PK_2_SEMANAS_PROCEDURES_MAP: List[Dict[str, Optional[str]]] = [
    {
        "procedure_name": r"Concentra[cç][aã]'o\s+s[eé]rica\s+de\s+oxandrolona\s+e\s+farmacocin[eé]tica",
        "co_procedimento": "129",
        "redcap_check_field": "",
        "redcap_date_field": ""
    },
    
    {
        "procedure_name": r"Monitoramento\s+de\s+eventos\s+adversos",
        "co_procedimento": "86", 
        "redcap_check_field": "form_medico_revisao7",
        "redcap_date_field": "form_medico_dt_visita"
    },
    
    { # regex Registro de uso de medicações pré-estudo e concomitantes - ok
        "procedure_name": r"Registro\s+de\s+uso\s+de\s+Medicações\s+Pr[éÉ]-Estudo\s+e\s+Concomitantes",
        "co_procedimento": "144", 
        "redcap_check_field": "form_medico_revisao4",
        "redcap_date_field": "form_medico_dt_visita"
    },
    
    {
        "procedure_name": r"Reconsentimento",
        "co_procedimento": "1",
        "redcap_check_field": "tcle_reconcentimento",
        "redcap_date_field": "tcle_dt_visita_aplicacao"
    }
]

PK_3_SEMANAS_PROCEDURES_MAP: List[Dict[str, Optional[str]]] = [
    {
        "procedure_name": r"",
        "co_procedimento": "",
        "redcap_check_field": "",
        "redcap_date_field": ""
    },
]

PK_4_SEMANAS_PROCEDURES_MAP: List[Dict[str, Optional[str]]] = [
    {
        "procedure_name": r"Concentra[cç][aã]'o\s+s[eé]rica\s+de\s+oxandrolona\s+e\s+farmacocin[eé]tica",
        "co_procedimento": "129",
        "redcap_check_field": "",
        "redcap_date_field": ""
    },
    
    {
        "procedure_name": r"Monitoramento\s+de\s+eventos\s+adversos",
        "co_procedimento": "86", 
        "redcap_check_field": "form_medico_revisao7",
        "redcap_date_field": "form_medico_dt_visita"
    },
    
    { # regex Registro de uso de medicações pré-estudo e concomitantes - ok
        "procedure_name": r"Registro\s+de\s+uso\s+de\s+Medicações\s+Pr[éÉ]-Estudo\s+e\s+Concomitantes",
        "co_procedimento": "144", 
        "redcap_check_field": "form_medico_revisao4",
        "redcap_date_field": "form_medico_dt_visita"
    },
    
    {
        "procedure_name": r"Reconsentimento",
        "co_procedimento": "1",
        "redcap_check_field": "tcle_reconcentimento",
        "redcap_date_field": "tcle_dt_visita_aplicacao"
    }
]

PK_8_SEMANAS_PROCEDURES_MAP: List[Dict[str, Optional[str]]] = [
    {
        "procedure_name": r"Concentra[cç][aã]'o\s+s[eé]rica\s+de\s+oxandrolona\s+e\s+farmacocin[eé]tica",
        "co_procedimento": "129",
        "redcap_check_field": "",
        "redcap_date_field": ""
    },
    
    {
        "procedure_name": r"Monitoramento\s+de\s+eventos\s+adversos",
        "co_procedimento": "86", 
        "redcap_check_field": "form_medico_revisao7",
        "redcap_date_field": "form_medico_dt_visita"
    },
    
    { # regex Registro de uso de medicações pré-estudo e concomitantes - ok
        "procedure_name": r"Registro\s+de\s+uso\s+de\s+Medicações\s+Pr[éÉ]-Estudo\s+e\s+Concomitantes",
        "co_procedimento": "144", 
        "redcap_check_field": "form_medico_revisao4",
        "redcap_date_field": "form_medico_dt_visita"
    },
    
    {
        "procedure_name": r"Reconsentimento",
        "co_procedimento": "1",
        "redcap_check_field": "tcle_reconcentimento",
        "redcap_date_field": "tcle_dt_visita_aplicacao"
    }
]

PK_12_SEMANAS_PROCEDURES_MAP: List[Dict[str, Optional[str]]] = [
    {
        "procedure_name": r"Concentra[cç][aã]'o\s+s[eé]rica\s+de\s+oxandrolona\s+e\s+farmacocin[eé]tica",
        "co_procedimento": "129",
        "redcap_check_field": "",
        "redcap_date_field": ""
    },
    
    {
        "procedure_name": r"Monitoramento\s+de\s+eventos\s+adversos",
        "co_procedimento": "86", 
        "redcap_check_field": "form_medico_revisao7",
        "redcap_date_field": "form_medico_dt_visita"
    },
    
    { # regex Registro de uso de medicações pré-estudo e concomitantes - ok
        "procedure_name": r"Registro\s+de\s+uso\s+de\s+Medicações\s+Pr[éÉ]-Estudo\s+e\s+Concomitantes",
        "co_procedimento": "144", 
        "redcap_check_field": "form_medico_revisao4",
        "redcap_date_field": "form_medico_dt_visita"
    },
    
    {
        "procedure_name": r"Reconsentimento",
        "co_procedimento": "1",
        "redcap_check_field": "tcle_reconcentimento",
        "redcap_date_field": "tcle_dt_visita_aplicacao"
    }
]

PK_16_SEMANAS_PROCEDURES_MAP: List[Dict[str, Optional[str]]] = [
    {
        "procedure_name": r"",
        "co_procedimento": "",
        "redcap_check_field": "",
        "redcap_date_field": ""
    },
]

PK_20_SEMANAS_PROCEDURES_MAP: List[Dict[str, Optional[str]]] = [
    {
        "procedure_name": r"Concentra[cç][aã]'o\s+s[eé]rica\s+de\s+oxandrolona\s+e\s+farmacocin[eé]tica",
        "co_procedimento": "129",
        "redcap_check_field": "",
        "redcap_date_field": ""
    },
    
    {
        "procedure_name": r"Monitoramento\s+de\s+eventos\s+adversos",
        "co_procedimento": "86", 
        "redcap_check_field": "form_medico_revisao7",
        "redcap_date_field": "form_medico_dt_visita"
    },
    
    { # regex Registro de uso de medicações pré-estudo e concomitantes - ok
        "procedure_name": r"Registro\s+de\s+uso\s+de\s+Medicações\s+Pr[éÉ]-Estudo\s+e\s+Concomitantes",
        "co_procedimento": "144", 
        "redcap_check_field": "form_medico_revisao4",
        "redcap_date_field": "form_medico_dt_visita"
    },
    
    {
        "procedure_name": r"Reconsentimento",
        "co_procedimento": "1",
        "redcap_check_field": "tcle_reconcentimento",
        "redcap_date_field": "tcle_dt_visita_aplicacao"
    }
]

PK_24_SEMANAS_PROCEDURES_MAP: List[Dict[str, Optional[str]]] = [
    {
        "procedure_name": r"Concentra[cç][aã]'o\s+s[eé]rica\s+de\s+oxandrolona\s+e\s+farmacocin[eé]tica",
        "co_procedimento": "129",
        "redcap_check_field": "",
        "redcap_date_field": ""
    },
    
    {
        "procedure_name": r"Monitoramento\s+de\s+eventos\s+adversos",
        "co_procedimento": "86", 
        "redcap_check_field": "form_medico_revisao7",
        "redcap_date_field": "form_medico_dt_visita"
    },
    
    { # regex Registro de uso de medicações pré-estudo e concomitantes - ok
        "procedure_name": r"Registro\s+de\s+uso\s+de\s+Medicações\s+Pr[éÉ]-Estudo\s+e\s+Concomitantes",
        "co_procedimento": "144", 
        "redcap_check_field": "form_medico_revisao4",
        "redcap_date_field": "form_medico_dt_visita"
    },
    
    {
        "procedure_name": r"Reconsentimento",
        "co_procedimento": "1",
        "redcap_check_field": "tcle_reconcentimento",
        "redcap_date_field": "tcle_dt_visita_aplicacao"
    }
]
    
VISITA_NAO_PROGRAMADA_PROCEDURES_MAP: List[Dict[str, Optional[str]]] = [
    {
        "procedure_name": r"Exame\s+f[ií]sico",
        "co_procedimento": "76",
        "redcap_check_field": "form_medico_ex_fisico_q0",
        "redcap_date_field": "form_medico_dt_visita"
    },
    
    {
        "procedure_name": r"Sinais\s+vitais",
        "co_procedimento": "7",
        "redcap_check_field": "form_medico_sv1",
        "redcap_date_field": "form_medico_dt_visita"
    },
    
    {
        "procedure_name": r"Registro\s+de\s+uso\s+de\s+medica[cç][oõ]es\s+pr[eé]-estudo\s+e\s+concomitantes",
        "co_procedimento": "144",
        "redcap_check_field": "form_medico_revisao4",
        "redcap_date_field": "form_medico_dt_visita"
    },
    
    {
        "procedure_name": r"Hemograma\s+completo-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_hematocrito",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Creatinina s[eé]rica-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_creatinina",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Ureia\s+s[eé]rica-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_ureia",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Bilirrubina\s+s[eé]rica\s+(total)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_bilirrubina",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Transaminase\s+glut[aâ]mico\s+oxalac[eé]tica/aspartato\s+aminotransferase\s+(TGO/AST)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_tgo",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Transaminase\s+glut[aâ]mico\s+pir[uú]vica/alanina\s+aminotransferase\s+(TGP/ALT)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_tgp",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Fosfatase\s+alcalina\s+(FA)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_fa",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Gama\s+glutamil\s+transferase\s+(GGT)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_ggt",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Creatinina\s+quinase\s+ou\s+Creatinina\s+fosfoquinase\s+(CK\s+ou\s+CPK)-\s+sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_cpk",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Antígeno\s+prost[aá]tico\s+espec[ií]fico\s+livre\s+(PSA)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_psa",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Colesterol-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_colesterol",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Low-density\s+lipoprotein\s+(LDL)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_ldl",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"High-density\s+lipoprotein\s+(HDL)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_hdl",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Lipoproteína\s+a\s+-\s+sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_lipoproteina",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Testosterona\s+total",
        "co_procedimento": "298",
        "redcap_check_field": "lab_testo_total",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Testosterona\s+livre\s+sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_testo_livre",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Horm[oô]nio\s+fol[ií]culo-estimulante\s+(FSH)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_fsh",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Horm[oô]nio\s+luteinizante\s+(LH)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_lh",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"D[íi]mero\s+D-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_dd",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Prote[ií]na\s+S\s+livre-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_prot_s",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Globulina\s+Ligadora\s+De\s+Horm[oô]nios\s+Sexuais\s+(SHBG)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_shbg",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Teste\s+de\s+gravidez",
        "co_procedimento": "175",
        "redcap_check_field": "coleta_gravidez",
        "redcap_date_field": "coleta_dt_visita"
    },
    
    {
        "procedure_name": r"Orienta[cç][oõ]es\s+para\s+programa\s+fisioter[aá]pico\s+para\s+reabilita[cç][aã]o\s+p[oó]s-operat[oó]ria",
        "co_procedimento": "319",
        "redcap_check_field": "rando_q1_v2",
        "redcap_date_field": "revisao_dt_visita"
    },
    
    {
        "procedure_name": r"Orienta[cç][oõ]es\s+para\s+uso\s+de\s+m[ée]todos\s+contraceptivos",
        "co_procedimento": "327",
        "redcap_check_field": "form_medico_gravidez_q3",
        "redcap_date_field": "form_medico_dt_visita"
    },
    
    {
        "procedure_name": r"Monitoramento\s+de\s+eventos\s+adversos",
        "co_procedimento": "86", 
        "redcap_check_field": "form_medico_revisao7",
        "redcap_date_field": "form_medico_dt_visita"
    },
    
    {
        "procedure_name": r"Consulta\s+M[eé]dica",
        "co_procedimento": "70",
        "redcap_check_field": "form_medico_rubrica",
        "redcap_date_field": "form_medico_dt_rubrica"
    },
        
            
    {
        "procedure_name": r"Reconsentimento",
        "co_procedimento": "1",
        "redcap_check_field": "tcle_reconcentimento",
        "redcap_date_field": "tcle_dt_visita_aplicacao"
    },
    
    {
        "procedure_name": r"Bioimped[aâ]ncia",
        "co_procedimento": "325",
        "redcap_check_field": "aval_corp_bioimpedancia",
        "redcap_date_field": "aval_corp_dt_visita"
    },
    
    {
        "procedure_name": r"Resson[aâ]ncia magn[eé]tica por imagem da coxa",
        "co_procedimento": "324",
        "redcap_check_field": "form_medico_ex_imagem1",
        "redcap_date_field": "form_medico_dt_visita"
    },
    
    {
        "procedure_name": r"Dinamometria isom[eé]trica",
        "co_procedimento": "323",
        "redcap_check_field": "fisio_isometria_q5",
        "redcap_date_field": "fisio_dt_visita"
    },
    
    {
        "procedure_name": r"Y balance test",
        "co_procedimento": "322",
        "redcap_check_field": "fisio_teste_y",
        "redcap_date_field": "fisio_dt_visita"
    },
    
    {
        "procedure_name": r"Question[aá]rio Lysholm Knee Scoring Scale",
        "co_procedimento": "59",
        "redcap_check_field": "rando_q3_v2",
        "redcap_date_field": "revisao_dt_visita"
    },
    
    {
        "procedure_name": r"Question[aá]rio Short Form-12 (SF-36SF-36)",
        "co_procedimento": "59",
        "redcap_check_field": "rando_q4_v2",
        "redcap_date_field": "revisao_dt_visita"
    },
    
    {
        "procedure_name": r"Question[aá]rio GAD-7",
        "co_procedimento": "59",
        "redcap_check_field": "rando_q5_v2",
        "redcap_date_field": "revisao_dt_visita"
    },
    
    {
        "procedure_name": r"Question[aá]rio PHQ9",
        "co_procedimento": "59",
        "redcap_check_field": "rando_q6_v2",
        "redcap_date_field": "revisao_dt_visita"
    },
    
    {
        "procedure_name": r"Question[aá]rio Patient Acceptable Symptom State (PAS)",
        "co_procedimento": "59",
        "redcap_check_field": "rando_q7_v2",
        "redcap_date_field": "revisao_dt_visita"
    },
    
    {
        "procedure_name": r"Consulta Fisioterapeuta",
        "co_procedimento": "320",
        "redcap_check_field": "fisio_dt_visita",
        "redcap_date_field": "fisio_dt_visita"
    }
]