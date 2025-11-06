from django.shortcuts import render
from .logic.cotizacion import crear_cotizacion
from django.http import JsonResponse
import json

# Create your views here.
def cotizar(request):
    body = json.loads(request.body)
    peso = int(body.get("peso"))
    cotizacion = crear_cotizacion(peso)
    return JsonResponse(cotizacion,safe=False)