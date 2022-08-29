from django.db import models

class cruds(models.Model):
    nome = models.CharField ("Nome", max_length=100)
    generos = models.CharField ("Gênero", max_length=100)
    classificação = models.IntegerField ("Classificação Indicativa")
