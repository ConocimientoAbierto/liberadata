from django.forms import ModelForm
from liberacion.models import SalesforceBackup

class CSVUploadForm(ModelForm):
    class Meta:
        model = SalesforceBackup
        fields = ["backup_file"]
