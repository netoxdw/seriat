# Generated by Django 3.2.12 on 2022-02-13 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prepa', '0003_alumno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='color_placa',
            field=models.IntegerField(choices=[(1, 'CAFE'), (1, 'NEGRO'), (1, 'ROJO'), (1, 'AZUL'), (1, 'VERDE'), (1, 'PLATA')], default=1, null=True),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='tipo_placa',
            field=models.IntegerField(choices=[(1, 'MEDITERRANEA'), (2, '4 PIEZAS'), (3, 'PELLISCO'), (4, 'PLANA'), (5, 'CORTE PLANO'), (6, 'CORAZON'), (7, 'PALERMO'), (8, 'PERGAMINO'), (9, 'COLUMNAS'), (10, 'CIRCULO'), (11, 'piramide')], default=1, null=True),
        ),
    ]
