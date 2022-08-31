from django.shortcuts import render, redirect
from .models import Filmes, Usuario
from .forms import FilmesForm, UsuarioForm

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

def usuario_listar(request):
    users = Usuario.objects.all()
    contexto = {
        'listar_user': users
    }
    return render(request, 'filmes_listar.html', contexto)


def cadastrar_usuario(request):
    form = UsuarioForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('usuario_listar')

    contexto = {
        'user': form
    }
    return render(request, 'cruds.html', contexto)


