from urllib import request

from django.shortcuts import render

# Create your views here.

def mostrar_home():
    return render(request,'index.html')

def mostrar_