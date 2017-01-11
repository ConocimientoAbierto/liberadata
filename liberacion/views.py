from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.http import HttpResponse,HttpResponseRedirect
from liberacion.forms import CSVUploadForm

# Create your views here.
def CSVUpload(request):
    form = CSVUploadForm()

    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            sfb = form.save()
            sfb.parse()
            sfb.save()
            return HttpResponseRedirect("/a?upload=true")

    return render(request, 'csvupload.html', {'form': form})
