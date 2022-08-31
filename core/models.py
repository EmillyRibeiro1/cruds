from django.db import models

class Filmes(models.Model):
    nome = models.CharField('Nome', max_length=100)
    generos = models.CharField ("Gênero", max_length=100)
    classificacao = models.IntegerField ("Classificação Indicativa")

class Usuario(models.Model):
    nome = models.CharField('Nome Completo', max_length=100)
    idade = models.IntegerField('Idade')
    email = models.CharField('E-mail', max_length=100)
