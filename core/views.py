from django.shortcuts import render
from .models import cruds

def listar_filmes(request):
    projeto = cruds.objects.all()
    context = {
        'cruds': cruds
    }
    return render(request, 'cruds.html', context)
