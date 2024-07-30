from django.db import models
from estudiante.models import Estudiante
from listas.models import Listas

DIGNIDADES = (
    ('Presidente', 'presidente'),
    ('Vicepresidente', 'vicepresidente'),
    ('Secretario/a', 'secretario/a'),
    ('Tesorero/a', 'tesorero/a'),
)

class Dignidad(models.Model):
    dignidad = models.CharField(default='Presidente', choices=DIGNIDADES, null=False, blank=False, max_length=30)

    def __str__ (self) -> str:
        return f'{self.dignidad}'
class Candidato(models.Model):
    listas = models.ForeignKey(Listas, on_delete=models.CASCADE, null=False, blank=False)
    candidato = models.ForeignKey(Estudiante, on_delete=models.PROTECT, null=True, blank=True)
    foto = models.ImageField(default='', upload_to='candidatos')
    dignidad = models.ForeignKey(Dignidad, on_delete=models.CASCADE, null=True, blank=True)

    def __str__ (self) -> str:
        return f'{self.listas.numero}-{self.listas.nombre}'