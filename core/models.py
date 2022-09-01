from django.db import models

class Filmes(models.Model):
    nome = models.CharField('Nome', max_length=100)
    generos = models.CharField ("Gênero", max_length=100)
    classificacao = models.IntegerField ("Classificação Indicativa")

class Comentario(models.Model):
    nome = models.CharField('Nome do Filme', max_length=100)
    comentario = models.CharField('Comentário', max_length=100)
    avaliacao = models.IntegerField('Avaliação')
