from django.forms import ModelForm
from .models import Filmes, Usuario

class FilmesForm(ModelForm):
    class Meta:
        model = Filmes
        fields = ['nome', 'generos', 'classificacao']

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'idade', 'email']