from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('bienvenida/', views.bienvenida, name='bienvenida'),
    path('listarTareas', views.listar_tareas, name='listarTareas'),
    path('listarTareasCompletadas', views.listar_tareas_completadas, name='listarTareasCompletadas'),
    # path('listarTarea/<int:id>', views.listar_tarea, name='listarTarea'),
    path('listarTareasMejorado/<int:id>', views.listar_tareas_mejorado, name='listarTareasMejorado'),
    path('crearTareas', views.crear_tareas, name='crearTareas'),
    path('crearProgramador', views.crear_programador, name='crearProgramador'),
    path('crearEtiquetas', views.crear_etiquetas, name='crearEtiquetas'),
]
