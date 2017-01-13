#encoding=UTF-8

from __future__ import unicode_literals

from django.db import models
from django.conf import settings
import zipfile
import os
from django.apps import apps
from django.utils.encoding import smart_text,force_text
import chardet
from kitchen.text.converters import to_unicode,to_bytes
from adaptor.model import CsvModel,CsvDbModel

# Create your models here.
class SalesforceBackup(models.Model):
    backup_file = models.FileField(upload_to=settings.FILES_ROOT)
    last_update = models.DateTimeField(auto_now=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    app_name = models.CharField(null=True,max_length=255)


    def parse(this):
        #Abre para lectura el zip
        zf = zipfile.ZipFile(this.backup_file,"r")

        #Toma la lista de archivos
        files = zf.namelist()

        for filename in files:
            try:
                #Lee datos directo del zip, no extrae
                csvdata = zf.read(filename)
                #Intenta corregir el encoding, aparentemente tiene que ser ascii, pero esta rompe todos los caracteres especiales
                csvdata = to_bytes(to_unicode(csvdata), encoding='ascii')
                #Separa en líneas y elimina la última línea porque viene vacía (verificar)
                csvdata = csvdata.split("\n")[:-1]

            except KeyError:
                print 'ERROR: Did not find %s in zip file' % filename
            else:
                #Crea los objetos en la base de datos
                this.csv_to_db(this.app_name,this.clean_name(this.backup_file.path),this.clean_name(filename),csvdata)
        return True;

    def csv_to_db(this,appname,backup,tablename,data):

        ## Filename to model mapping
        # Cada app model tiene que tener source_files que digan qué archivos se cargan ahí
        model = this.get_model(appname,tablename)

        #Creación dinámica de modelo importador de adaptor
        importer = this.get_importer(model)

        #Importar datos
        importer.import_data(data=data)

        return True;

    def clean_name(this,filename):
        return filename.split("/")[-1].split(".")[0];

    def get_model(this,appname,tablename):
        appConfig = apps.get_app_config(appname)

        #Procesar todos los modelos de la app para ver cuál tiene entre sus source_files el tablename que estamos procesando
        for n in appConfig.models:
            m = appConfig.models[n]
            f= m.__dict__["source_files"];
            print f
            if tablename in f:
                return m

    def get_importer(model):
        importerMeta = type(str("Meta"),(),{"delimiter": str(','),"has_header": True,"dbModel": model })
        importer = type(str("importer"),(CsvDbModel,),{"Meta": importerMeta})
        return importer
