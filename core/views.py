from django.shortcuts import render
from .models import cruds
from .forms import crudsForm

def listar_filmes(request):
    projeto = cruds.objects.all()
    context = {
        'cruds': cruds
    }
    return render(request, 'cruds.html', context)

def cadastrar(request):
    form = crudsForm()
    context = {
        'form_crud': form
    }
    return render(request, 'cadastrar.html', context)
