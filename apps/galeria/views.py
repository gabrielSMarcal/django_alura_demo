from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .models import Fotografia
from .forms import NovaImagemForms

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
    
    return render(request, 'galeria/index.html', {'cards': fotografias})

def nova_image(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Efetue Login para ter acesso')
        return redirect('login')
    
    form = NovaImagemForms
    if request.method == 'POST':
        form = NovaImagemForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Nova imagem salva!')
            return redirect('index')
    
    return render(request, 'galeria/nova_imagem.html', {'form': form})

def editar_imagem(request, foto_id):
    fotografia = Fotografia.objects.get(id=foto_id)
    form = NovaImagemForms(instance=fotografia)
        
    
    if request.method == "POST":
        form = NovaImagemForms(request.POST, request.FILES, instance=fotografia)
        if form.is_valid():
            form.save()
            messages.success(request, 'Fotografia editada com sucesso!')
            return redirect('index')
    
    return render(request, 'galeria/editar_imagem.html', {'form': form, 'foto_id': foto_id})

def deletar_imagem(request, foto_id):
    fotografia = Fotografia.objects.get(id=foto_id)
    fotografia.delete()
    messages.success(request, 'Fotografia excluída com sucesso')
        
    return redirect('index')

def filtro(request, categoria):
    fotografias = Fotografia.objects.order_by('-data_foto').filter(publicada=True, categoria=categoria)
    return render(request, 'galeria/index.html', {'cards': fotografias})