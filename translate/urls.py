from django.urls import path
from .views import *
from django.conf import Settings

app_name = 'translate'

urlpatterns = [
    path('', home, name='home'),
    path('<slug:slug>', malumot, name='malumot')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)