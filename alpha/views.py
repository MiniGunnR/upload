from django.shortcuts import render
from django.views.generic.edit import CreateView

from .models import Image

class FileUpload(CreateView):
    model = Image
    template_name = 'alpha/upload.html'
    success_url = '/success/'
    fields = ['file']
