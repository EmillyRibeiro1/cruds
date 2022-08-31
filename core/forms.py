from django.forms import ModelForm
from .models import Filmes

class FilmesForm(ModelForm):
    class Meta:
        model = Filmes
        fields = ['nome', 'generos', 'classificacao']