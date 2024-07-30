from django.db import models
from listas.models import Listas
from estudiante.models import Estudiante


class Voto(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, null=False, blank=False)
    listas = models.ForeignKey(Listas, on_delete=models.CASCADE, null=False, blank=False)
 