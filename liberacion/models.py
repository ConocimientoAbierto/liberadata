from __future__ import unicode_literals

from django.db import models
from django.conf import settings
import zipfile
import os

# Create your models here.
class SalesforceBackup(models.Model):
    backup_file = models.FileField(upload_to=settings.FILES_ROOT)
    last_update = models.DateTimeField(auto_now=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    instagram_user = models.IntegerField(null=True)


    def parse(this):
        # print zipfile.ZipFile
        zf = zipfile.ZipFile(this.backup_file,"r")
        files = zf.namelist()
        for filename in files:
            try:
                csvdata = zf.read(filename)
            except KeyError:
                print 'ERROR: Did not find %s in zip file' % filename
            else:
                this.csv_to_db(this.clean_name(this.backup_file.path),this.clean_name(filename),csvdata)
        return True;

    def csv_to_db(this,backup,tablename,data):
        path = settings.FILES_ROOT+"/"+backup+"/";
        if not os.path.exists(path):
            os.makedirs(path)

        with (open(path+tablename+".csv","w+")) as f:
            f.write(data);
        return True;

    def clean_name(this,filename):
        return filename.split("/")[-1].split(".")[0];
