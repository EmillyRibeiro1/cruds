from django.shortcuts import render, redirect
from .models import Filmes, Comentario
from .forms import FilmesForm, ComentarioForm 

def filmes_listar(request):
    filmes = Filmes.objects.all()
    contexto = {
        'listar': filmes
    }
    return render(request, 'cruds.html', contexto)

def filmes_cadastro(request):
    form = FilmesForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('filmes_listar')
    contexto = {
        'form_filme': form
    }
    return render(request, 'cadastrar.html', contexto)

def editar_filme(request, id):
    filme = Filmes.objects.get(pk=id)

    form = FilmesForm(request.POST or None, instance=filme)

    if form.is_valid():
        form.save()
        return redirect('filmes_listar')

    contexto={
        'form_filme': form
    }
    return render(request, 'cadastrar.html', contexto)

def remover_filme(request, id):
    filme = Filmes.objects.get(pk=id)
    filme.delete()
    return redirect('filmes_listar')

def coments(request):
    form = ComentarioForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('')
    contexto = {
        'emi': form
    }
    return render(request, '', contexto)

def listar_coments(request):
    lista = Comentario.objects.all()
    contexto = {
        'listar': lista
    }
    return render(request, 'coments.html', contexto)




