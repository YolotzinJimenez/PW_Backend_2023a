from django.shortcuts import render
# Se importa HttpResponse
from django.http import HttpResponse

# Create your views here.
def index(request):
 return HttpResponse("Hola desde mi primera vista 💫")

def author(request):
 return HttpResponse("Autor: Dira Jimenez🫠")

def author(request):
    return HttpResponse("Hello Author 👨‍🎤")

def greet(request, name):
    return HttpResponse(f"Hello, {name}!!!")
