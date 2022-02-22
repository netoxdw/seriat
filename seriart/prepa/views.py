
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# from rest_framework.response import Response
from prepa.serialazers import GeneracionSerialazer, EscuelaSerialazer, GrupoSerialazer, AlumnoSerialazer

from prepa.models import Generacion, Escuela, Grupo, Alumno




# from rest_framework.views import APIView

# Create your views here.
class GeneracionView(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Generacion.objects.all().order_by('id', 'generacion')
    serializer_class = GeneracionSerialazer

class EscuelaView(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Escuela.objects.all().order_by('id', 'generacion', 'nombre')
    serializer_class = EscuelaSerialazer

class GeneracionEscuelaView(ModelViewSet):
    serializer_class = EscuelaSerialazer
    def get_queryset(self):
        return Escuela.objects.filter(generacion= self.kwargs['generacion_pk'])



class GrupoView(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Grupo.objects.all().order_by('id', 'escuela', 'grupo')
    serializer_class = GrupoSerialazer

class EscuelaGrupoView(ModelViewSet):
    serializer_class = GrupoSerialazer
    def get_queryset(self):
        return Grupo.objects.filter(escuela= self.kwargs['escuela_pk'])



class AlumnoView(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Alumno.objects.all().order_by('id', 'grupo', 'nombre', 'tipo_moldura')
    serializer_class = AlumnoSerialazer
    
class GrupoAlumnoView(ModelViewSet):
    serializer_class = AlumnoSerialazer
    def get_queryset(self):
        return Alumno.objects.filter(grupo= self.kwargs['grupo_pk'])



