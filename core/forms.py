from django.forms import ModelForm
from .models import Filmes, Comentario

class FilmesForm(ModelForm):
    class Meta:
        model = Filmes
        fields = ['nome', 'generos', 'classificacao']

class ComentarioForm(ModelForm):
    class Meta:
        model = Comentario
        fields = ['nome', 'comentario', 'avaliacao']