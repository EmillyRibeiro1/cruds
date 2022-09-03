from django.db import models


class Filmes(models.Model):
    nome = models.CharField('Nome do Filme', max_length=100)
    genero = models.CharField('Gênero', max_length=100)
    classificacao = models.CharField('Classificação', max_length=10)
    foto = models.ImageField('Foto', upload_to='filmes', null=True)

class Usuario(models.Model):
    nome = models.CharField('Nome e Sobrenome', max_length=100)
    idade = models.IntegerField('Idade')
    email = models.EmailField(max_length=254)

class Comentarios(models.Model):
    comet = models.CharField('Comentario', max_length=100)
    nomeFil = models.CharField('Nome do Filme', max_length=100)
    avaliacao = models.CharField('Avaliação', max_length=100)