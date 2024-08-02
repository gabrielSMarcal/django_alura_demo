from django.urls import path

from . import views

 

urlpatterns = [
    path('', views.index, name='index'),
    path('imagem/<int:foto_id>', views.imagem, name='imagem'),
    path('buscar/', views.buscar, name='buscar'),
    path('nova-imagem/', views.nova_image, name='nova_imagem'),
    path('editar-imagem/<int:foto_id>', views.editar_imagem, name='editar_imagem'),
    path('deletar-imagem/<int:foto_id>', views.deletar_imagem, name='deletar_imagem'),
    path('filtro/<str:categoria>', views.filtro, name='filtro'),
]


