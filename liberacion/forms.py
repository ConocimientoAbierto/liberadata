from django.forms import ModelForm
from liberacion.models import SalesforceBackup
from django import forms
from django.conf import settings
from django.apps import apps

class CSVUploadForm(ModelForm):
    class Meta:
        model = SalesforceBackup
        fields = ["backup_file","app_name"]

    def get_sources_choices():
        sources = []

        # Usa introspeccion para ver todas las apps que hay, excluye las que son internas y genera el listado
        for app_label in apps.app_configs:
            app = apps.get_app_config(app_label)
            if "." not in app.name and app.name not in settings.EXCLUDED_APPS:
                source = (app.name, app.verbose_name )
                sources.append(source)

        return sources

    app_name = forms.ChoiceField()
    app_name.choices = get_sources_choices()
