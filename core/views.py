from django.shortcuts import render

def listar_filmes(request):
    return render(request, 'cruds.html')
