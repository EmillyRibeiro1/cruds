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
from django.conf import settings
from django.conf.urls.static import static
from core.views import filme_cadastrar,filme_editar,filme_listar,filme_remover,home
from core.views import comentario_cadastrar,comentario_editar,comentario_listar,comentario_remover
from core.views import usuario_cadastrar,usuario_editar,usuario_listar,usuario_remover
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name= 'home'),

    path('filmes/', filme_listar, name='filmes_listar'),
    path('filmes_cadastro/', filme_cadastrar, name='filmes_cadastro'),
    path('filmes_editar/<int:id>/', filme_editar, name='filmes_editar'),
    path('filmes_remover/<int:id>/', filme_remover, name='filmes_remover'),

    path('cometario_listar/', comentario_listar, name='cometario_listar'),
    path('cometario_cadastro/', comentario_cadastrar, name='cometario_cadastro'),
    path('cometario_editar/<int:id>/', comentario_editar, name='cometario_editar'),
    path('cometario_remover/<int:id>/', comentario_remover, name='cometario_remover'),

    path('usuario_listar/', usuario_listar, name='usuario_listar'),
    path('usuario_cadastro/', usuario_cadastrar, name='usuario_cadastro'),
    path('usuario_editar/<int:id>/', usuario_editar, name='usuario_editar'),
    path('usuario_remover/<int:id>/', usuario_remover, name='usuario_remover'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
