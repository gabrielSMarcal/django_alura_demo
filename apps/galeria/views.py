from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .models import Fotografia

def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Efetue Login para ter acesso')
        return redirect('login')
    
    fotografias = Fotografia.objects.order_by('-data_foto').filter(publicada=True)
    return render(request, 'galeria/index.html', {'cards': fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {'fotografia': fotografia})

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Efetue Login para ter acesso')
        return redirect('login')
    
    fotografias = Fotografia.objects.order_by('-data_foto').filter(publicada=True)
    if 'buscar' in request.GET:
        nome_buscado = request.GET['buscar']
        if nome_buscado:
            fotografias = fotografias.filter(nome__icontains=nome_buscado)
    
    return render(request, 'galeria/buscar.html', {'cards': fotografias})

def nova_image(request):
    return render(request, 'galeria/nova_imagem.html')

def editar_image(request):
    pass

def deletar_image(request):
    pass