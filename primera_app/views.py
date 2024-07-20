from django.http import HttpResponse
from django.shortcuts import render

def inicio(request):
    return render(request, "primera_app/index.html")

def cursos(request):
    return render(request, "primera_app/cursos.html")

def profesores(request):
    return render(request, "primera_app/entregables.html")

def estudiantes(request):
    return render(request, "primera_app/estudiantes.html")

def entregables(request):
    return render(request, "primera_app/profesores.html")