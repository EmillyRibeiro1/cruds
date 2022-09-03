from .models import Usuario, Filmes, Comentarios
from django.forms import ModelForm

class UsuarioForm(ModelForm):
    class Meta():
        model = Usuario
        fields = ['nome', 'idade', 'email']

class FilmesForm(ModelForm):
    class Meta():
        model = Filmes
        fields = ['nome', 'genero', 'classificacao', 'foto']

class ComentariosForm(ModelForm):
    class Meta():
        model = Comentarios
        fields = ['comet', 'nomeFil', 'avaliacao']