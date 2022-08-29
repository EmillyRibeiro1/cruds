from django.shortcuts import render, redirect
from .models import cruds
from .forms import crudsForm

def listar_filmes(request):
    projeto = cruds.objects.all()
    context = {
        'cruds': cruds
    }
    return render(request, 'cruds.html', context)

def cadastrar(request):
    form = crudsForm(request.POST or None)

    if form.is_valid():
        return redirect('listar_filmes')

    context = {
        'form_cruds': form
    }
    return render(request, 'cadastrar.html', context)
