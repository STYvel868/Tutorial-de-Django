from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def post_list(request):
    return HttpResponse("¡Hola Ibai! Bienvenido a tu primer proyecto Django 😎")
