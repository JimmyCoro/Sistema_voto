from django.urls import path
from .views import listas

urlpatterns = [
    path('listas/', listas, name='listas')

]
