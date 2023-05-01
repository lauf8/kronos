from django.db import models

class Orcamento(models.Model):
    nome = models.CharField(max_length=100)
    despesas = models.ManyToManyField('Despesa', related_name='orcamentos')
    rendas = models.ManyToManyField('Renda', related_name='orcamentos')
    
    def valor_total(self):
        valor_despesas = self.despesas.aggregate(models.Sum('valor'))['valor__sum'] or 0
        valor_rendas = self.rendas.aggregate(models.Sum('valor'))['valor__sum'] or 0
        return valor_rendas - valor_despesas
    

class Despesa(models.Model):
    nome = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome
    
    

class Renda(models.Model):
    nome = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.nome
