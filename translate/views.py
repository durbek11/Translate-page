from django.shortcuts import render, get_object_or_404
from .models import TranslatePage


def home(request):
    
    return render(request, "home.html")

def malumot(request):
    malumot = get_object_or_404(TranslatePage)
    return render(request, "malumot.html", {"malumot":malumot})