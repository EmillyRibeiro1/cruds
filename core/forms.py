from django.forms import ModelForm
from .models import cruds

class crudsForm(ModelForm):
    class meta:
        model = cruds
        fields = ['genero', 'classificaçao', 'lançamentos']