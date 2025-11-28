from django.urls import path

from . import views

urlpatterns = [
    path('', views.lista_tareas, name='lista'),
    path('crear/', views.crear_tarea, name='crear'),
    path('<int:id>/editar/', views.editar_tarea, name='editar'),  # Ruta dinámica
    path('<int:id>/eliminar/', views.eliminar_tarea, name='eliminar'),  # Ruta dinámica
]
