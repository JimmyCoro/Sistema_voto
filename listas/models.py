from django.db import models


class Listas(models.Model):
    numero = models.CharField(max_length=5, unique=True, blank=True, null=True)
    nombre = models.CharField(max_length=15, unique=True)
    propuesta = models.CharField(max_length=300, default='', blank=True, null=True)
    
    def total_votos(self):
        from voto.models import Voto
        votos = Voto.objects.filter(listas_id=self.id).count()
        return votos

    def __str__(self) -> str:
        return f'{self.numero}, {self.nombre}'
# Create your models here.
