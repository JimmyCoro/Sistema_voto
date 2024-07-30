from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

CURSOS = (('Primero', 1),('Segundo', 2),('Tercero', 3),('Cuarto', 4),)
PARALELO = (('A', 'A'),('B', 'B'),('C', 'C'),('D', 'D'),)

class Curso(models.Model):
    nivel = models.IntegerField(default=1)
    paralelo = models.CharField(max_length=1, default='A')

    def __str__(self) -> str:
        return f'{self.nivel} - {self.paralelo}'


# Create your models here.
class Estudiante(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.user.first_name} - {self.curso}'