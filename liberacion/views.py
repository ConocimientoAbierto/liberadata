from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.http import HttpResponse,HttpResponseRedirect
from liberacion.forms import CSVUploadForm
from django.apps import apps

# Create your views here.
def CSVUpload(request):
    form = CSVUploadForm()

    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            sfb = form.save()
            sfb.parse()
            sfb.save()
            return HttpResponseRedirect("/upload?done=true")

    return render(request, 'csvupload.html', {'form': form})

def home(request):
    sources = []

    # Usa introspeccion para ver todas las apps que hay, excluye las que son internas y genera el listado
    excluded_apps = ("rest_framework","django_extensions","liberacion")
    for app_label in apps.app_configs:
        app = apps.get_app_config(app_label)
        if "." not in app.name and app.name not in excluded_apps:
            csvs = []
            models = app.models
            for n in models:
                m = app.models[n]
                if m.__dict__["export_csv"] == True:
                    csvs.append(m)
            source = { "name": app.name, "api_url": app.name+"/", "csvs": csvs }
            sources.append(app)

    return render(request, 'home.html', {'sources': sources})
