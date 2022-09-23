from django.urls import path
from .views import *

app_name = "translate"

urlpatterns = [
    path("", home, name="home"),
    path("<slug:slug>", malumot, name="mulomot")
]