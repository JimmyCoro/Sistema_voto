# Generated by Django 5.0.7 on 2024-07-14 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudiante', '0002_remove_estudiante_apellidos_remove_estudiante_cedula_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='nivel',
            field=models.IntegerField(default=1),
        ),
    ]
