from urllib import request

from django.shortcuts import render

# Create your views here.

def mostrar_home(request):
    return render(request, "index.html")

def mostrar_servicios(request):
    return render(request, "about.html")