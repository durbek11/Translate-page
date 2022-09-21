from django.shortcuts import render

def home(request, slug):
    return render (request, 'home.html')
