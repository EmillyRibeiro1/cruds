from django.shortcuts import render, redirect
from .models import Filmes, Usuario, Comentarios
from .forms import FilmesForm, UsuarioForm, ComentariosForm

# Create your views here.


def home(request):
    return render(request, 'index.html')

#filme
def filme_listar(request):
    filmes = Filmes.objects.all()
    contexto = {
        'lista_filmes': filmes
    }
    return render(request, 'filme.html',contexto)

def filme_cadastrar(request):
    form = FilmesForm(request.POST or None, request.FILES or None)
    if form.is_valid():
            form.save()
            return redirect('filmes_listar')
    contexto = {
        'form': form
    }
    return render(request, 'filme_add.html',contexto)

def filme_editar(request,id):
    filme = Filmes.objects.get(pk=id)
    
    form = FilmesForm(request.POST or None, instance=filme)
    if form.is_valid():
        form.save()
        return redirect('filmes_listar')
    
    contexto = {
        'form': form
    }
    return render(request, 'filme_add.html',contexto)

def filme_remover(request,id):
    filme = Filmes.objects.get(pk=id)
    filme.delete()
    return redirect('filmes_listar')


#Usuario
def usuario_listar(request):
    usuarios = Usuario.objects.all()
    contexto = {
        'lista_usuario': usuarios
    }
    return render(request, 'usuario.html',contexto)

def usuario_cadastrar(request):
    form = UsuarioForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('usuario_listar')
    contexto = {
        'form': form
    }
    return render(request, 'usuario_add.html',contexto)

def usuario_editar(request,id):
    usuarios = Usuario.objects.get(pk=id)
    
    form = UsuarioForm(request.POST or None, instance=usuarios)
    if form.is_valid():
        form.save()
        return redirect('usuario_listar')
    
    contexto = {
        'form': form
    }
    return render(request, 'usuario_add.html',contexto)

def usuario_remover(request,id):
    usuarios = Usuario.objects.get(pk=id)
    usuarios.delete()
    return redirect('usuario_listar')





#comentario
def comentario_listar(request):
    comentario = Comentarios.objects.all()
    contexto = {
        'lista_comentario': comentario
    }
    return render(request, 'cometario.html',contexto)

def comentario_cadastrar(request):
    form = ComentariosForm(request.POST or None)
    if form.is_valid():
            form.save()
            return redirect('cometario_listar')
    contexto = {
        'form': form
    }
    return render(request, 'cometario_add.html',contexto)

def comentario_editar(request,id):
    comentario = Comentarios.objects.get(pk=id)
    
    form = ComentariosForm(request.POST or None, instance=comentario)
    if form.is_valid():
        form.save()
        return redirect('cometario_listar')
    
    contexto = {
        'form': form
    }
    return render(request, 'cometario_add.html',contexto)

def comentario_remover(request,id):
    comentario = Comentarios.objects.get(pk=id)
    comentario.delete()
    return redirect('cometario_listar')