from django.urls import path
from .views import *

urlpatterns = [
    path('voto/', voto, name='voto'),
    path('reporte/', reporte, name='reporte')


]
