from django.urls import path
from .views import cotizar
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('cotizar/', csrf_exempt(cotizar), name='crear_cotizacion'),
]
