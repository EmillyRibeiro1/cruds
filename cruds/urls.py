"""cruds URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import filmes_cadastro, filmes_listar, editar_filme, remover_filme, coment, listar_coments

urlpatterns = [
    path('cadastro/', filmes_cadastro, name='cadastro'),
    path('filmes/', filmes_listar, name='filmes_listar'),
    path('filme_editar/<int:id>/', editar_filme, name='editar_filme'),
    path('filme_remover/<int:id>/', remover_filme, name='remover_filme'),
    path('coments/', coment, name='coment'),
    path('coment_listar/', listar_coments, name='listar_coments'),
    path('admin/', admin.site.urls),
]
