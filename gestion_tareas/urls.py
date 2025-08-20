
from django.urls import path
from .views import lista_tareas, nueva_tarea

urlpatterns = [
    path("lista_tareas/", lista_tareas, name='lista_tareas'),
    path("nueva_tarea/", nueva_tarea, name='nueva_tarea'),
]
