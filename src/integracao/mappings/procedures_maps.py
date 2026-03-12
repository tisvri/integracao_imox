from typing import List, Dict, Optional

V1_POLOTRIAL_PROCEDURES_MAP: List[Dict[str, Optional[str]]] = [
    {
        "procedure_name": "Teste de gravidez",
        # "co_procedimento": "175",
        "redcap_check_field": "coleta_gravidez",
        "redcap_date_field": "coleta_dt_visita"
    },
    
    {
        "procedure_name": r"Exame f[iÍ]sico",
        # "co_procedimento": "76", 
        "redcap_check_field": "form_medico_ex_fisico_q0",
        "redcap_date_field": "form_medico_dt_visita"
    },
    {
        "procedure_name": r"Consulta M[eéEÉ]dica",
        # "co_procedimento": "70",
        # Neste caso, a data de checagem é a própria data de visita.
        "redcap_check_field": "form_medico_dt_rubrica",
        "redcap_date_field": "form_medico_dt_rubrica"

    },
    {
        "procedure_name": r"Hist[oóOÓ]ria M[éeEÉ]dica",
        # "co_procedimento": "4", 
        "redcap_check_field": "form_medico_revisao6",
        "redcap_date_field": "form_medico_dt_visita"
    },
    { # regex Registro de uso de medicações pré-estudo e concomitantes - ok
        "procedure_name": r"Registro de uso de Medicações Pr[éÉ]-Estudo e Concomitantes",
        # "co_procedimento": "144", 
        "redcap_check_field": "form_medico_revisao4",
        "redcap_date_field": "form_medico_dt_visita"
    },
    {
        "procedure_name": r"Sinais vitais",
        # "co_procedimento": "7", 
        "redcap_check_field": "form_medico_sv1",
        "redcap_date_field": "form_medico_dt_visita"
    },
    {
        "procedure_name": r"Dados demogr[aáàâãäå]ficos",
        # "co_procedimento": "61", 
        "redcap_check_field": "demografia_dt_visita",
        "redcap_date_field": "demografia_dt_visita"
    },
    {
        "procedure_name": r"Termo de consentimento Livre e Esclarecido",
        # "co_procedimento": "1", 
        "redcap_check_field": "tcle_pergunta_c",
        "redcap_date_field": "tcle_dt_visita_aplicacao"
    },
    {
        "procedure_name": r"Avalia[cç][aã]o dos crit[eé]rios de inclus[aã]o/exclus[aã]o",
        # "co_procedimento": "2", 
        "redcap_check_field": "form_medico_revisao",
        "redcap_date_field": "form_medico_dt_visita"
    },
    {
        "procedure_name": r"Orienta[cç][oõ]es para programa fisioter[aá]pico para reabilita[cç][aã]o p[oó]s-operat[oó]ria",
        "redcap_check_field": "rando_q1_v2",
        "redcap_date_field": "revisao_dt_visita"
    },
    {
        "procedure_name": r"Monitoramento de eventos adversos",
        "redcap_check_field": "form_medico_revisao7",
        "redcap_date_field": "form_medico_dt_visita"
    },
    {
        "procedure_name": r"Orienta[cç][oõ]es para uso de m[eé]todos contraceptivos",
        "redcap_check_field": "form_medico_gravidez_q3",
        "redcap_date_field": "form_medico_dt_visita"
    },
    {
        "procedure_name": r"Dispensa[cç][aã]o de medica[cç][aã]o para tromboprofilaxia p[oó]s-cirurgica",
        # "co_procedimento": "250", 
        "redcap_check_field": "form_medico_revisao1",
        "redcap_date_field": "form_medico_dt_visita"
    },
    {
        "procedure_name": r"Question[aá]rio IPAQ",
        # "co_procedimento": "59", 
        "redcap_check_field": "ipaq_dt_visita",
        "redcap_date_field": "ipaq_dt_visita"
    },
    {
        "procedure_name": r"Globulina Ligadora De Hormonios Sexuais",
        # "co_procedimento": "298", 
        "redcap_check_field": "lab_shbg",
        "redcap_date_field": "lab_dt_visita"
    },
    {
        "procedure_name": r"Hemograma completo-sangue",
        # "co_procedimento": "298", 
        "redcap_check_field": "lab_hematocrito",
        "redcap_date_field": "hematocrito_dt"
    },
    {
        "procedure_name": r"Creatinina sérica-sangue",
        "redcap_check_field": "lab_creatinina",
        "redcap_date_field": "lab_dt_visita"
    },
    {
        "procedure_name": r"Bilirrubina s[eé]rica \(total\)-sangue",
        "redcap_check_field": "lab_bilirrubina",
        "redcap_date_field": "lab_dt_visita"
    },
    {
        "procedure_name": r"Transaminase glut[aâ]mico pir[uú]vica/alanina aminotransferase \(TGP/ALT\)-sangue",
        "redcap_check_field": "lab_tgp",
        "redcap_date_field": "lab_dt_visita"
    },
    {
        "procedure_name": r"Albumina-Sangue",
        "redcap_check_field": "lab_albumina",
        "redcap_date_field": "lab_dt_visita"
    },
    {
        "procedure_name": r"Ant[ií]geno prost[aá]tico espec[ií]fico livre \(PSA\)-sangue",
        "redcap_check_field": "lab_psa",
        "redcap_date_field": "lab_dt_visita"
    },
    

]

V2_POLOTRIAL_PROCEDURES_MAP: List[Dict[str, Optional[str]]] = [
    {
        "procedure_name": r"Avalia[cç][aã]o dos crit[eé]rios de inclus[aã]o/exclus[aã]o",
        "co_procedimento": "2",
        "redcap_check_field": "form_medico_revisao",
        "redcap_date_field": "form_medico_dt_visita"
    },
    
    {
        "procedure_name": r"Exame f[ií]sico",
        "co_procedimento": "76",
        "redcap_check_field": "form_medico_ex_fisico_q0",
        "redcap_date_field": "form_medico_dt_visita"
    },
    
    {
        "procedure_name": r"Sinais vitais",
        "co_procedimento": "7",
        "redcap_check_field": "form_medico_sv1",
        "redcap_date_field": "form_medico_dt_visita"
    },
    
    {
        "procedure_name": r"Registro de uso de medica[cç][oõ]es pr[eé]-estudo e concomitantes",
        "co_procedimento": "144",
        "redcap_check_field": "form_medico_revisao4",
        "redcap_date_field": "form_medico_dt_visita"
    },
        
    {
        "procedure_name": r"Teste de gravidez",
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
        "procedure_name": r"Monitoramento de eventos adversos",
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
        "procedure_name": r"Consulta M[eé]dica",
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
    }
]

V3_PROCEDURES_MAP: List[Dict[str, Optional[str]]] = [
    {
        "procedure_name": r"Exame f[ií]sico",
        "co_procedimento": "76",
        "redcap_check_field": "form_medico_ex_fisico_q0",
        "redcap_date_field": "form_medico_dt_visita"
    },
    
    {
        "procedure_name": r"Sinais vitais",
        "co_procedimento": "7",
        "redcap_check_field": "form_medico_sv1",
        "redcap_date_field": "form_medico_dt_visita"
    },
    
    {
        "procedure_name": r"Registro de uso de medica[cç][oõ]es pr[eé]-estudo e concomitantes",
        "co_procedimento": "144",
        "redcap_check_field": "form_medico_revisao4",
        "redcap_date_field": "form_medico_dt_visita"
    },
    
    {
        "procedure_name": r"Hemograma completo-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_hematocrito",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Creatinina sérica-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_creatinina",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Ureia s[eé]rica-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_ureia",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Bilirrubina s[eé]rica (total)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_bilirrubina",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Transaminase glut[aâ]mico oxalac[eé]tica/aspartato aminotransferase (TGO/AST)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_tgo",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Transaminase glut[aâ]mico pir[uú]vica/alanina aminotransferase (TGP/ALT)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_tgp",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Fosfatase alcalina (FA)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_fa",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Gama glutamil transferase (GGT)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_ggt",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Creatinina quinase ou Creatinina fosfoquinase (CK ou CPK)- sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_cpk",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Antígeno prost[aá]tico espec[ií]fico livre (PSA)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_psa",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Colesterol- sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_colesterol",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Low-density lipoprotein (LDL)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_ldl",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"High-density lipoprotein (HDL)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_hdl",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Lipoproteína a - sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_lipoproteina",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Testosterona total",
        "co_procedimento": "298",
        "redcap_check_field": "lab_testo_total",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Testosterona livre sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_testo_livre",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Horm[oô]nio fol[ií]culo-estimulante (FSH)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_fsh",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Horm[oô]nio luteinizante (LH)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_lh",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"D[íi]mero D-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_dd",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Prote[ií]na S livre-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_prot_s",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Globulina Ligadora De Horm[oô]nios Sexuais (SHBG)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_shbg",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Teste de gravidez",
        "co_procedimento": "175",
        "redcap_check_field": "coleta_gravidez",
        "redcap_date_field": "coleta_dt_visita"
    },
    
    {
        "procedure_name": r"Orienta[cç][oõ]es para programa fisioter[aá]pico para reabilita[cç][aã]o p[oó]s-operat[oó]ria",
        "co_procedimento": "319",
        "redcap_check_field": "rando_q1_v2",
        "redcap_date_field": "revisao_dt_visita"
    },
    
    {
        "procedure_name": r"Orienta[cç][oõ]es para uso de m[ée]todos contraceptivos",
        "co_procedimento": "327",
        "redcap_check_field": "form_medico_gravidez_q3",
        "redcap_date_field": "form_medico_dt_visita"
    },
    
    {
        "procedure_name": r"Monitoramento de eventos adversos",
        "co_procedimento": "86", 
        "redcap_check_field": "form_medico_revisao7",
        "redcap_date_field": "form_medico_dt_visita"
    },
    
    {
        "procedure_name": r"Consulta M[eé]dica",
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
        "procedure_name": r"Exame f[ií]sico",
        "co_procedimento": "76",
        "redcap_check_field": "form_medico_ex_fisico_q0",
        "redcap_date_field": "form_medico_dt_visita"
    },
    
    {
        "procedure_name": r"Sinais vitais",
        "co_procedimento": "7",
        "redcap_check_field": "form_medico_sv1",
        "redcap_date_field": "form_medico_dt_visita"
    },
    
    {
        "procedure_name": r"Registro de uso de medica[cç][oõ]es pr[eé]-estudo e concomitantes",
        "co_procedimento": "144",
        "redcap_check_field": "form_medico_revisao4",
        "redcap_date_field": "form_medico_dt_visita"
    },
    
    {
        "procedure_name": r"Hemograma completo-sangue",
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
        "procedure_name": r"Ureia s[eé]rica-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_ureia",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Bilirrubina s[eé]rica (total)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_bilirrubina",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Transaminase glut[aâ]mico oxalac[eé]tica/aspartato aminotransferase (TGO/AST)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_tgo",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Transaminase glut[aâ]mico pir[uú]vica/alanina aminotransferase (TGP/ALT)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_tgp",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Fosfatase alcalina (FA)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_fa",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Gama glutamil transferase (GGT)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_ggt",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Creatinina quinase ou Creatinina fosfoquinase (CK ou CPK)- sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_cpk",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Antígeno prost[aá]tico espec[ií]fico livre (PSA)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_psa",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Colesterol- sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_colesterol",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Low-density lipoprotein (LDL)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_ldl",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"High-density lipoprotein (HDL)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_hdl",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Lipoproteína a - sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_lipoproteina",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Testosterona total",
        "co_procedimento": "298",
        "redcap_check_field": "lab_testo_total",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Testosterona livre sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_testo_livre",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Horm[oô]nio fol[ií]culo-estimulante (FSH)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_fsh",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Horm[oô]nio luteinizante (LH)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_lh",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"D[íi]mero D-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_dd",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Prote[ií]na S livre-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_prot_s",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Globulina Ligadora De Horm[oô]nios Sexuais (SHBG)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_shbg",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Teste de gravidez",
        "co_procedimento": "175",
        "redcap_check_field": "coleta_gravidez",
        "redcap_date_field": "coleta_dt_visita"
    },
    
    {
        "procedure_name": r"Orienta[cç][oõ]es para programa fisioter[aá]pico para reabilita[cç][aã]o p[oó]s-operat[oó]ria",
        "co_procedimento": "319",
        "redcap_check_field": "rando_q1_v2",
        "redcap_date_field": "revisao_dt_visita"
    },
    
    {
        "procedure_name": r"Orienta[cç][oõ]es para uso de m[ée]todos contraceptivos",
        "co_procedimento": "327",
        "redcap_check_field": "form_medico_gravidez_q3",
        "redcap_date_field": "form_medico_dt_visita"
    },
    
    {
        "procedure_name": r"Monitoramento de eventos adversos",
        "co_procedimento": "86", 
        "redcap_check_field": "form_medico_revisao7",
        "redcap_date_field": "form_medico_dt_visita"
    },
    
    {
        "procedure_name": r"Consulta M[eé]dica",
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
        "procedure_name": r"Exame f[ií]sico",
        "co_procedimento": "76",
        "redcap_check_field": "form_medico_ex_fisico_q0",
        "redcap_date_field": "form_medico_dt_visita"
    },
    
    {
        "procedure_name": r"Sinais vitais",
        "co_procedimento": "7",
        "redcap_check_field": "form_medico_sv1",
        "redcap_date_field": "form_medico_dt_visita"
    },
    
    {
        "procedure_name": r"Registro de uso de medica[cç][oõ]es pr[eé]-estudo e concomitantes",
        "co_procedimento": "144",
        "redcap_check_field": "form_medico_revisao4",
        "redcap_date_field": "form_medico_dt_visita"
    },
    
    {
        "procedure_name": r"Hemograma completo-sangue",
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
        "procedure_name": r"Ureia s[eé]rica-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_ureia",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Bilirrubina s[eé]rica (total)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_bilirrubina",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Transaminase glut[aâ]mico oxalac[eé]tica/aspartato aminotransferase (TGO/AST)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_tgo",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Transaminase glut[aâ]mico pir[uú]vica/alanina aminotransferase (TGP/ALT)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_tgp",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Fosfatase alcalina (FA)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_fa",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Gama glutamil transferase (GGT)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_ggt",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Creatinina quinase ou Creatinina fosfoquinase (CK ou CPK)- sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_cpk",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Antígeno prost[aá]tico espec[ií]fico livre (PSA)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_cpk",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Colesterol- sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_colesterol",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Low-density lipoprotein (LDL)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_ldl",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"High-density lipoprotein (HDL)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_hdl",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Lipoproteína a - sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_lipoproteina",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Testosterona total",
        "co_procedimento": "298",
        "redcap_check_field": "lab_testo_total",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Testosterona livre sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_testo_livre",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Horm[oô]nio fol[ií]culo-estimulante (FSH)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_fsh",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Horm[oô]nio luteinizante (LH)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_lh",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"D[íi]mero D-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_dd",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Prote[ií]na S livre-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_prot_s",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Globulina Ligadora De Horm[oô]nios Sexuais (SHBG)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_shbg",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Teste de gravidez",
        "co_procedimento": "175",
        "redcap_check_field": "coleta_gravidez",
        "redcap_date_field": "coleta_dt_visita"
    },
    
    {
        "procedure_name": r"Orienta[cç][oõ]es para programa fisioter[aá]pico para reabilita[cç][aã]o p[oó]s-operat[oó]ria",
        "co_procedimento": "319",
        "redcap_check_field": "rando_q1_v2",
        "redcap_date_field": "revisao_dt_visita"
    },
    
    {
        "procedure_name": r"Orienta[cç][oõ]es para uso de m[ée]todos contraceptivos",
        "co_procedimento": "327",
        "redcap_check_field": "form_medico_gravidez_q3",
        "redcap_date_field": "form_medico_dt_visita"
    },
    
    {
        "procedure_name": r"Monitoramento de eventos adversos",
        "co_procedimento": "86", 
        "redcap_check_field": "form_medico_revisao7",
        "redcap_date_field": "form_medico_dt_visita"
    },
    
    {
        "procedure_name": r"Consulta M[eé]dica",
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
        "procedure_name": r"Concentra[cç][aã]'o s[eé]rica de oxandrolona e farmacocin[eé]tica",
        "co_procedimento": "129",
        "redcap_check_field": "",
        "redcap_date_field": ""
    },
    
    {
        "procedure_name": r"Monitoramento de eventos adversos",
        "co_procedimento": "86", 
        "redcap_check_field": "form_medico_revisao7",
        "redcap_date_field": "form_medico_dt_visita"
    },
    
    { # regex Registro de uso de medicações pré-estudo e concomitantes - ok
        "procedure_name": r"Registro de uso de Medicações Pr[éÉ]-Estudo e Concomitantes",
        "co_procedimento": "144", 
        "redcap_check_field": "form_medico_revisao4",
        "redcap_date_field": "form_medico_dt_visita"
    }
    
]

PK_24H_PROCEDURES_MAP: List[Dict[str, Optional[str]]] = [
    {
        "procedure_name": r"Concentra[cç][aã]'o s[eé]rica de oxandrolona e farmacocin[eé]tica",
        "co_procedimento": "129",
        "redcap_check_field": "",
        "redcap_date_field": ""
    },
    
    {
        "procedure_name": r"Monitoramento de eventos adversos",
        "co_procedimento": "86", 
        "redcap_check_field": "form_medico_revisao7",
        "redcap_date_field": "form_medico_dt_visita"
    },
    
    { # regex Registro de uso de medicações pré-estudo e concomitantes - ok
        "procedure_name": r"Registro de uso de Medicações Pr[éÉ]-Estudo e Concomitantes",
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
        "procedure_name": r"Concentra[cç][aã]'o s[eé]rica de oxandrolona e farmacocin[eé]tica",
        "co_procedimento": "129",
        "redcap_check_field": "",
        "redcap_date_field": ""
    },
    
    {
        "procedure_name": r"Monitoramento de eventos adversos",
        "co_procedimento": "86", 
        "redcap_check_field": "form_medico_revisao7",
        "redcap_date_field": "form_medico_dt_visita"
    },
    
    { # regex Registro de uso de medicações pré-estudo e concomitantes - ok
        "procedure_name": r"Registro de uso de Medicações Pr[éÉ]-Estudo e Concomitantes",
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
        "procedure_name": r"Concentra[cç][aã]'o s[eé]rica de oxandrolona e farmacocin[eé]tica",
        "co_procedimento": "129",
        "redcap_check_field": "",
        "redcap_date_field": ""
    },
    
    {
        "procedure_name": r"Monitoramento de eventos adversos",
        "co_procedimento": "86", 
        "redcap_check_field": "form_medico_revisao7",
        "redcap_date_field": "form_medico_dt_visita"
    },
    
    { # regex Registro de uso de medicações pré-estudo e concomitantes - ok
        "procedure_name": r"Registro de uso de Medicações Pr[éÉ]-Estudo e Concomitantes",
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
        "procedure_name": r"Concentra[cç][aã]'o s[eé]rica de oxandrolona e farmacocin[eé]tica",
        "co_procedimento": "129",
        "redcap_check_field": "",
        "redcap_date_field": ""
    },
    
    {
        "procedure_name": r"Monitoramento de eventos adversos",
        "co_procedimento": "86", 
        "redcap_check_field": "form_medico_revisao7",
        "redcap_date_field": "form_medico_dt_visita"
    },
    
    { # regex Registro de uso de medicações pré-estudo e concomitantes - ok
        "procedure_name": r"Registro de uso de Medicações Pr[éÉ]-Estudo e Concomitantes",
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
        "procedure_name": r"Concentra[cç][aã]'o s[eé]rica de oxandrolona e farmacocin[eé]tica",
        "co_procedimento": "129",
        "redcap_check_field": "",
        "redcap_date_field": ""
    },
    
    {
        "procedure_name": r"Monitoramento de eventos adversos",
        "co_procedimento": "86", 
        "redcap_check_field": "form_medico_revisao7",
        "redcap_date_field": "form_medico_dt_visita"
    },
    
    { # regex Registro de uso de medicações pré-estudo e concomitantes - ok
        "procedure_name": r"Registro de uso de Medicações Pr[éÉ]-Estudo e Concomitantes",
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
        "procedure_name": r"Concentra[cç][aã]'o s[eé]rica de oxandrolona e farmacocin[eé]tica",
        "co_procedimento": "129",
        "redcap_check_field": "",
        "redcap_date_field": ""
    },
    
    {
        "procedure_name": r"Monitoramento de eventos adversos",
        "co_procedimento": "86", 
        "redcap_check_field": "form_medico_revisao7",
        "redcap_date_field": "form_medico_dt_visita"
    },
    
    { # regex Registro de uso de medicações pré-estudo e concomitantes - ok
        "procedure_name": r"Registro de uso de Medicações Pr[éÉ]-Estudo e Concomitantes",
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
        "procedure_name": r"Concentra[cç][aã]'o s[eé]rica de oxandrolona e farmacocin[eé]tica",
        "co_procedimento": "129",
        "redcap_check_field": "",
        "redcap_date_field": ""
    },
    
    {
        "procedure_name": r"Monitoramento de eventos adversos",
        "co_procedimento": "86", 
        "redcap_check_field": "form_medico_revisao7",
        "redcap_date_field": "form_medico_dt_visita"
    },
    
    { # regex Registro de uso de medicações pré-estudo e concomitantes - ok
        "procedure_name": r"Registro de uso de Medicações Pr[éÉ]-Estudo e Concomitantes",
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
        "procedure_name": r"Concentra[cç][aã]'o s[eé]rica de oxandrolona e farmacocin[eé]tica",
        "co_procedimento": "129",
        "redcap_check_field": "",
        "redcap_date_field": ""
    },
    
    {
        "procedure_name": r"Monitoramento de eventos adversos",
        "co_procedimento": "86", 
        "redcap_check_field": "form_medico_revisao7",
        "redcap_date_field": "form_medico_dt_visita"
    },
    
    { # regex Registro de uso de medicações pré-estudo e concomitantes - ok
        "procedure_name": r"Registro de uso de Medicações Pr[éÉ]-Estudo e Concomitantes",
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
        "procedure_name": r"Exame f[ií]sico",
        "co_procedimento": "76",
        "redcap_check_field": "form_medico_ex_fisico_q0",
        "redcap_date_field": "form_medico_dt_visita"
    },
    
    {
        "procedure_name": r"Sinais vitais",
        "co_procedimento": "7",
        "redcap_check_field": "form_medico_sv1",
        "redcap_date_field": "form_medico_dt_visita"
    },
    
    {
        "procedure_name": r"Registro de uso de medica[cç][oõ]es pr[eé]-estudo e concomitantes",
        "co_procedimento": "144",
        "redcap_check_field": "form_medico_revisao4",
        "redcap_date_field": "form_medico_dt_visita"
    },
    
    {
        "procedure_name": r"Hemograma completo-sangue",
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
        "procedure_name": r"Ureia s[eé]rica-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_ureia",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Bilirrubina s[eé]rica (total)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_bilirrubina",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Transaminase glut[aâ]mico oxalac[eé]tica/aspartato aminotransferase (TGO/AST)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_tgo",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Transaminase glut[aâ]mico pir[uú]vica/alanina aminotransferase (TGP/ALT)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_tgp",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Fosfatase alcalina (FA)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_fa",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Gama glutamil transferase (GGT)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_ggt",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Creatinina quinase ou Creatinina fosfoquinase (CK ou CPK)- sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_cpk",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Antígeno prost[aá]tico espec[ií]fico livre (PSA)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_psa",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Colesterol- sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_colesterol",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Low-density lipoprotein (LDL)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_ldl",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"High-density lipoprotein (HDL)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_hdl",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Lipoproteína a - sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_lipoproteina",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Testosterona total",
        "co_procedimento": "298",
        "redcap_check_field": "lab_testo_total",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Testosterona livre sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_testo_livre",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Horm[oô]nio fol[ií]culo-estimulante (FSH)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_fsh",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Horm[oô]nio luteinizante (LH)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_lh",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"D[íi]mero D-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_dd",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Prote[ií]na S livre-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_prot_s",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Globulina Ligadora De Horm[oô]nios Sexuais (SHBG)-sangue",
        "co_procedimento": "298",
        "redcap_check_field": "lab_shbg",
        "redcap_date_field": "lab_dt_visita"
    },
    
    {
        "procedure_name": r"Teste de gravidez",
        "co_procedimento": "175",
        "redcap_check_field": "coleta_gravidez",
        "redcap_date_field": "coleta_dt_visita"
    },
    
    {
        "procedure_name": r"Orienta[cç][oõ]es para programa fisioter[aá]pico para reabilita[cç][aã]o p[oó]s-operat[oó]ria",
        "co_procedimento": "319",
        "redcap_check_field": "rando_q1_v2",
        "redcap_date_field": "revisao_dt_visita"
    },
    
    {
        "procedure_name": r"Orienta[cç][oõ]es para uso de m[ée]todos contraceptivos",
        "co_procedimento": "327",
        "redcap_check_field": "form_medico_gravidez_q3",
        "redcap_date_field": "form_medico_dt_visita"
    },
    
    {
        "procedure_name": r"Monitoramento de eventos adversos",
        "co_procedimento": "86", 
        "redcap_check_field": "form_medico_revisao7",
        "redcap_date_field": "form_medico_dt_visita"
    },
    
    {
        "procedure_name": r"Consulta M[eé]dica",
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