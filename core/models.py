from django.db import models

class Filmes(models.Model):
    nome = models.CharField('Nome', max_length=100)
    generos = models.CharField ("Gênero", max_length=100)
    classificacao = models.IntegerField ("Classificação Indicativa")
    
