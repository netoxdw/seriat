from prepa.models import Generacion, Escuela, Grupo, Alumno
from rest_framework import serializers

class GeneracionSerialazer(serializers.ModelSerializer):
    class Meta:
        model = Generacion
        fields = ('id', 'generacion')

class EscuelaSerialazer(serializers.ModelSerializer):
    class Meta:
        model = Escuela
        fields = ('id', 'generacion', 'nombre')

class GrupoSerialazer(serializers.ModelSerializer):
    class Meta:
        model = Grupo
        fields = ('id', 'escuela', 'grupo')

class AlumnoSerialazer(serializers.ModelSerializer):
    class Meta:      
        model = Alumno
        fields = ('id', 'grupo', 'nombre', 'get_tipo_moldura_display')
        