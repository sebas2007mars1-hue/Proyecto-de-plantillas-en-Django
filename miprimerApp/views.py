
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("¡Hola mundo desde Django!")

def instructor(request):
    return HttpResponse("Bienvenido al curso de Django - Instructor Jorge Coral")

def curso(request):
    return HttpResponse("Curso: Desarrollo Web con Django")

def ficha(request):
    return HttpResponse("Ficha ADSO: 3360426")

def centro(request):
    return HttpResponse("Centro de Teleinformática y Producción Industrial")



def inicio(request):

    contexto = {
        'aprendiz': 'Sebastián Martínez',
        'ficha': '3360426',
        'programa': 'Análisis y Desarrollo de Software',
        'framework': 'Django',
        'activo': True,
        'cursos': [
        'Python',
        'Django',
        'HTML',
        'CSS',
        'JavaScript',
],
    }

    return render(request, 'miprimerApp/inicio.html', contexto)

