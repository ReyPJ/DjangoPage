from django.urls import path
from . import views  # . es la carpeta donde me encuentro

app_name = 'productos'  # COMBENCION
urlpatterns = [  # SIEMPRE SEGUIR LA COMBENCION, # AQUI ESTAMOS MAPEANDO LA URL
    path('', views.index, name='index'),
    path('formulario', views.formulario, name='formulario'),
    path(
        # IMPORTANTE, lo que esta dentro de <> es el nombre del parametro de la funcion detalle
        '<int:producto_id>',
        views.detalle,
        name='detalle'
    ),
]
