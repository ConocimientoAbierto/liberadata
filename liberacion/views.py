from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.http import HttpResponse,HttpResponseRedirect
from liberacion.forms import CSVUploadForm
from django.apps import apps
from django.conf import settings

# Create your views here.
def CSVUpload(request):
    form = CSVUploadForm()


    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            sfb = form.save()
            sfb.parse()
            sfb.export()
            sfb.save()
            return HttpResponseRedirect("/upload?done=true")

    return render(request, 'csvupload.html', {'form': form})

def home(request):
    sources = get_sources()
    return render(request, 'home.html', {'sources': sources})


def get_sources():
    sources = []

    # Usa introspeccion para ver todas las apps que hay, excluye las que son internas y genera el listado
    for app_label in apps.app_configs:
        app = apps.get_app_config(app_label)
        if "." not in app.name and app.name not in settings.EXCLUDED_APPS:
            csvs = []
            models = app.models
            for n in models:
                m = app.models[n]
                if m.__dict__["export_csv"] == True:
                    csvs.append({"name": m._meta.verbose_name,"download_url": "/static/csvs/"+m._meta.label+".csv", "size": "kb" })
                    print m
            source = { "name": app.verbose_name, "api_url": app.name+"/", "license": "OdBL", "last_update": "", "count": "", "csvs": csvs }
            sources.append(source)
    return sources
