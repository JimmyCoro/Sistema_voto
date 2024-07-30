from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio_login, name = 'inicio_login'),
]
