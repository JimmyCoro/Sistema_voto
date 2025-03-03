# Generated by Django 5.0.7 on 2024-07-14 05:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidato', '0001_initial'),
        ('listas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidato',
            name='lista',
        ),
        migrations.RemoveField(
            model_name='dignidad',
            name='nombre',
        ),
        migrations.AddField(
            model_name='candidato',
            name='listas',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='listas.listas'),
        ),
        migrations.AddField(
            model_name='dignidad',
            name='dignidad',
            field=models.CharField(choices=[('Presidente', 'presidente'), ('Vicepresidente', 'vicepresidente'), ('Secretario/a', 'secretario/a'), ('Tesorero/a', 'tesorero/a')], default='Presidente', max_length=30),
        ),
        migrations.DeleteModel(
            name='Lista',
        ),
    ]
