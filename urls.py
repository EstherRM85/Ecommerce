from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path
from .views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns,static
from django.conf import settings
from django.contrib.auth.models import User


urlpatterns = [

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
