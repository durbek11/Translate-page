from django.shortcuts import render, get_object_or_404
from .models import TranslatePage

def home(request):
    return render (request, 'home.html')

def malumot(request, slug):
    malumot = get_object_or_404(TranslatePage, slug=slug)
    contex = {
        'malumot':malumot
    }
    return render(request, 'malumot.html', contex)
