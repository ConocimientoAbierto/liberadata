from __future__ import unicode_literals
from django.db import models

class Person(models.Model):
    source_files = ["Contact","test"]
    export_csv = True

    FirstName = models.CharField(max_length=255)
    LastName = models.CharField(max_length=255)
