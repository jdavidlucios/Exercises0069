from django.urls import path
from . import views  # Importa las vistas desde el archivo `views.py`

urlpatterns = [
    path('', views.index, name='index'),  # Ruta principal de la app
]
