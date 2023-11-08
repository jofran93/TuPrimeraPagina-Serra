from django.shortcuts import render

from django.http import HttpResponse
import datetime

def saludo(request):
    return HttpResponse("Hola Django - Coder")

def dia_de_hoy(request):
    dia = datetime.datetime.now()
    documentoDeTexto = f"Hoy es dia: <br> {dia}"
    return HttpResponse(documentoDeTexto)

# Create your views here.
