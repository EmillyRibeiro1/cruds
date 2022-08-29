from django.forms import ModelForm
from .models import cruds

class crudsForm(ModelForm):
    class Meta:
        model = cruds
        fields = ['nome', 'generos', 'classificação']