from django.forms import ModelForm
from .models import cruds

class crudsForm(ModelForm):
    class Meta:
        model = cruds
        fields = ['generos', 'classificação', 'lançamentos']