from django.contrib import admin
from prepa import models



class GeneracionAdmin(admin.ModelAdmin):
     list_display = ('id', 'generacion')

class EscuelaAdmin(admin.ModelAdmin):
     list_display = ('id', 'generacion', 'nombre', 'ciudad')

class GrupoAdmin(admin.ModelAdmin):
     list_display = ('id', 'escuela', 'grupo', 'postales')

class AlumnoAdmin(admin.ModelAdmin):
     list_display = ('id', 'grupo', 'nombre', 'tipo_moldura', 'tipo_placa', 'folio')


# Register your models here.

     
admin.site.register(models.Generacion, GeneracionAdmin)
admin.site.register(models.Escuela, EscuelaAdmin)
admin.site.register(models.Grupo, GrupoAdmin)
admin.site.register(models.Alumno, AlumnoAdmin)
admin.site.register(models.Pago)
admin.site.register(models.Control)