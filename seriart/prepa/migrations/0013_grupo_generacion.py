# Generated by Django 3.2.12 on 2022-02-16 03:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prepa', '0012_alter_alumno_taza'),
    ]

    operations = [
        migrations.AddField(
            model_name='grupo',
            name='generacion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='grupo', to='prepa.generacion'),
        ),
    ]
