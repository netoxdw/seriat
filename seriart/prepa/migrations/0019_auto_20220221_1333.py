# Generated by Django 3.2.12 on 2022-02-21 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prepa', '0018_auto_20220221_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='color_placa',
            field=models.CharField(choices=[(7, '---'), (1, 'CAFE'), (2, 'NEGRO'), (3, 'ROJO'), (4, 'AZUL'), (5, 'VERDE'), (6, 'PLATA')], default=1, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='tipo_moldura',
            field=models.CharField(choices=[(1, 'PIRAMIDAL NEGRO'), (2, 'PIRAMIDAL VINO'), (3, 'PIRAMIDAL CAFE'), (4, 'ROLEX CAFE'), (5, 'ROLEX NEGRO'), (6, 'ROLEX VINO'), (9, 'CRISTAL GRANDE'), (10, 'MERCURIO'), (11, 'CORONA'), (12, 'ESTRELLA'), (14, 'MARIPOSA'), (15, 'ROMANA'), (16, 'MONACO'), (17, 'ANUBIS'), (18, 'ESLOVENIA'), (19, 'INGLESA'), (20, 'BERLIN'), (21, 'FLORENCIA'), (22, 'RESINA'), (23, 'CRISTAL CHICO')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='tipo_placa',
            field=models.CharField(choices=[(12, '---'), (1, 'MEDITERRANEA'), (2, '4 PIEZAS'), (3, 'PELLISCO'), (4, 'PLANA'), (5, 'CORTE PLANO'), (6, 'CORAZON'), (7, 'PALERMO'), (8, 'PERGAMINO'), (9, 'COLUMNAS'), (10, 'CIRCULO'), (11, 'piramide')], default=1, max_length=20, null=True),
        ),
    ]