from django.urls import path
from .views import *

app_name = "translate"

urlpatterns = [
    path("home/", home, name="home"),
    path("malumot/", malumot, name="mulomot")
]
