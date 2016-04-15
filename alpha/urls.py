from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^upload/$', views.FileUpload.as_view(), name='upload'),
]