from django.db import models

class cruds(models.Model):
    generos = models.CharField ("Gênero", max_length=100)
    classificação = models.IntegerField ("Classificação Indicativa")
    lançamentos = models.CharField ("Lançamentos", max_length=100) 
