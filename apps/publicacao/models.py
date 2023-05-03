from django.db import models
from apps.cronograma.models import Cronograma

class Publicacao(models.Model):
    titulo = models.CharField(max_length=225)
    conteudo = models.TextField()
    cronograma = models.ForeignKey(Cronograma, on_delete=models.SET_NULL, null=True, blank=True)


class Comentario(models.Model):
    conteudo = models.TextField()
    publicacao = models.ForeignKey(Publicacao, on_delete=models.CASCADE)