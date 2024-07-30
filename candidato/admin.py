
from django.contrib import admin
from candidato.models import *
# Register your models here.
modelos = [Listas, Dignidad, Candidato]

admin.site.register(modelos)