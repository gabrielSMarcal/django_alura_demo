from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('imagem/<int:foto_id>', views.imagem, name='imagem'),
    path('buscar/', views.buscar, name='buscar'),
    path('nova-imagem/', views.nova_image, name='nova_imagem'),
    path('editar-imagem/', views.editar_image, name='editar_imagem'),
    path('deletar-imagem/', views.deletar_image, name='deletar_imagem'),
]


