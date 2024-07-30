
from django.contrib import admin
from estudiante.models import Curso, Estudiante
# Register your models here.
modelos = [Curso, Estudiante]

admin.site.register(modelos)