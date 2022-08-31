from django.shortcuts import render, redirect
from .models import Filmes
from .forms import FilmesForm

def filmes_listar(request):
    filmes = Filmes.objects.all()
    contexto = {
        'filmes_listar': Filmes
    }
    return render(request, 'cruds.html', contexto)

def filmes_cadastro(request):
    form = FilmesForm(request.POST or None)
    if form.is_valid():
            form.save()
            return redirect('filmes_listar')
    contexto = {
        'form': form
    }
    return render(request, 'cadastrar.html', contexto)



