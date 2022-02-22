
from cgitb import lookup
from django.urls import path, include
from prepa import views
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('generaciones', views.GeneracionView),
generaciones_router = routers.NestedDefaultRouter(router, 'generaciones', lookup= 'generacion')
generaciones_router.register('escuelas', views.GeneracionEscuelaView, basename='generacion-escuela')

router.register('escuelas', views.EscuelaView),

escuelas_router = routers.NestedDefaultRouter(router, 'escuelas', lookup= 'escuela')
escuelas_router.register('grupos', views.EscuelaGrupoView, basename='escuela-grupo')

router.register('grupos', views.GrupoView),

grupos_router = routers.NestedDefaultRouter(router, 'grupos', lookup= 'grupo')
grupos_router.register('alumnos', views.GrupoAlumnoView, basename='grupo-alumno')

router.register('alumnos', views.AlumnoView),


urlpatterns = [
    path('', include(router.urls)),
    path('', include(generaciones_router.urls)),
    path('', include(escuelas_router.urls)),
    path('', include(grupos_router.urls)),

]