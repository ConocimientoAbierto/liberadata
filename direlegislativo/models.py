#coding=utf-8

from __future__ import unicode_literals
from django.db import models

class Person(models.Model):
    #Acá van los nombres de archivo dentro del ZIP que se importan a este modelo
    source_files = ["Contact","test"]

    #Acá van los campos que están en los CSV pero no se importan a la DB
    exclude_fields = ["Id","IsDeleted","MasterRecordId","AccountId","Salutation","RecordTypeId","OtherStreet",
    "OtherCity","OtherState","OtherPostalCode","OtherCountry","OtherLatitude","OtherLongitude",
    "OtherGeocodeAccuracy","MailingStreet","MailingCity","MailingState","MailingPostalCode",
    "MailingCountry","MailingLatitude","MailingLongitude","MailingGeocodeAccuracy","Phone",
    "Fax","MobilePhone","HomePhone","OtherPhone","AssistantPhone","ReportsToId","Email",
    "Title","Department","AssistantName","LeadSource","Birthdate",
    "Description","OwnerId","HasOptedOutOfEmail","HasOptedOutOfFax",
    "DoNotCall","CreatedDate","CreatedById","LastModifiedDate","LastModifiedById",
    "SystemModstamp","LastActivityDate","LastCURequestDate","LastCUUpdateDate",
    "EmailBouncedReason","EmailBouncedDate","Jigsaw","JigsawContactId",
    "C_mara__c","Estado_del_Mandato__c","Razones_de_Interrumpido__c",
    "Fecha_de_Ingreso__c","C_digo_Postal__c","Lugar_de_nacimiento__c",
    "Estado_Civil__c","Nombre_del_C_nyuge__c","Fecha_de_egreso__c",
    "Asesor_de_prensa__c","P_gina_web__c","Email_2__c","Bloque__c",
    "Razones_de_Ingreso__c","Provincia_de_Nacimiento__c","Cargo_Universal__c","A_o__c",
    "Especializaci_n__c","A_o_2__c","Cuenta_de_Twitter__c","Documento_de_Identidad__c",
    "Otros__c","Secretario_a__c","Celular_del_secretario_a__c","Distrito__c",
    "Correo_electr_nico_personal__c","Nivel_de_Gobierno__c","Interno__c","Tel_fono_Directo__c",
    "Sexo__c","Especializaci_n_del_T_tulo_Acad_mico__c","Especializaci_n_del_T_tulo_Acad_mico_2__c",
    "T_tulo_Acad_mico__c","Otro_t_tulo_acad_mico__c","Celular_del_diputado__c","Foto__c",
    "Correo_electr_nico_alternativo__c","Pa_s_de_nacimiento__c","Instituci_n__c","Instituci_n_2__c",
    "Provincia_del_Legislador__c","Especificaci_n_del_Cargo_Universal__c","Ubicaci_n_en_la_voleta__c",
    "Estado_del_Ingreso__c","Proyectos_Presentados__c","Correo_electr_nico_del_Asesor_de_prensa__c",
    "Correo_electr_nico_de_la_secretaria__c","Lista__c","Bloque_Estado__c","Piso__c","Bloque_Fecha_de_alta__c"
    ,"Provincia__c","Oficina__c","Asesor_a_de_prensa_2__c","Cantidad_de_Hijos__c","Bloque_Fecha_de_baja__c",
    "Bloque_Comentarios__c","Secci_n_Departamento__c","Empleados_a_cargo__c","Ingreso_Fecha_de_inicio__c",
    "Ingreso_Fecha_de_baja__c","Salario_del_legislador__c","Iniciativas_Transparentes1__c","Ciudad__c",
    "Direcci_n__c","Numero_de_lista__c","C_omisiones_a_las_que_pertenece__c","Contacto__c","Mandato__c",
    "Cobra_desarraigo__c","T_tulo_Acad_mico_3__c","Especializaci_n_del_T_tulo_Acad_mico_3__c","A_o_3__c",
    "Instituci_n_3__c","Celular_personal__c","Clasificaci_n_del_contacto__c","E_mail_personal__c",
    "Estado_del_contacto_general__c","N_mero_del_Contacto__c","C_mara_s_lo_para_info__c","Eje_tem_tico__c",
    "Cargo_del_contacto__c","TIMBASURVEYS__Survey__c","Link_al_DL_online__c",
    "Integrante_de_espacios_de_FDL__c","MC4SF__MC_Subscriber__c","Contest_la_ficha__c"]

    #Esto determina si este modelo se exporta a CSV para descargar, luego de la importación
    export_csv = True

    #Campos que si se importan y el tipo de campo
    FirstName = models.CharField(max_length=255)
    LastName = models.CharField(max_length=255)

    #TODO: Campos relacionados
