# Generated by Django 3.2.12 on 2022-02-13 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prepa', '0005_alter_generacion_generacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto', models.FloatField(max_length=10)),
                ('nombre', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='anticipo', to='prepa.alumno')),
            ],
        ),
    ]