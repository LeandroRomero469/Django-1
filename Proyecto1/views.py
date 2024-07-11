from django.http import HttpResponse
from datetime import datetime as dt
# Agregamos al encabezado del archivo el import de Template y de Context
from django.template import Template, Context


def saludo(request):
    return HttpResponse("Hola mundo!, hola Coder!")

def mostrar_nombre(request):
    texto = "Soy Leandro Romero<br>Cursando Python"
    return HttpResponse(texto)

def dia_de_hoy(request):
    dia = dt.now()
    texto = f"Hoy es:<br>{dia}"
    return HttpResponse(texto)

def probando_template(request):

    nombre = "Adrian"
    apellido = "Holovaty"
    diccionario = {"nombre": nombre, "apellido": apellido, "notas": [4, 8, 9, 10, 7, 8]}

# Abrimos el archivo html
    mi_html = open('./Proyecto1/plantillas/index.html')

    # Creamos el template haciendo uso de la clase Template
    plantilla = Template(mi_html.read())

# Cerramos el archivo previamente abierto, ya que lo tenemos cargado en la variable plantilla
    mi_html.close()

# Creamos un contexto con los datos del diccionario
    mi_contexto = Context(diccionario)

    # Terminamos de construír el template renderizándolo con su contexto
    documento = plantilla.render(mi_contexto)

    return HttpResponse(documento)
