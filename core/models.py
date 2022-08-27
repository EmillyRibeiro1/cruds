from __future__ import generator_stop
from socket import NI_NUMERICHOST
from django.db import models

class cruds(models.Model):
    generos = models.CharField ("Gênero", max_length=100)
    classificação = models.IntegerField ("Classificação Indicativa")
    Lançamentos = models.CharField ("Lançamentos", max_length=100) 
