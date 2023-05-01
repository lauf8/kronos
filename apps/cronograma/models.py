from django.db import models
from django.core.exceptions import ValidationError
import datetime


class Cronograma(models.Model):
    nome = models.CharField(max_length=50)
    def __str__(self):
        return self.nome


class Atividade(models.Model):
    horario_inicial = models.TimeField()
    horario_final = models.TimeField()
    atividade = models.CharField(max_length=75)
    DIAS_DA_SEMANA = [
        ('SEGUNDA', 'Segunda-feira'),
        ('TERCA', 'Terça-feira'),
        ('QUARTA', 'Quarta-feira'),
        ('QUINTA', 'Quinta-feira'),
        ('SEXTA', 'Sexta-feira'),
        ('SABADO', 'Sábado'),
        ('DOMINGO', 'Domingo'),
    ]
    dia_da_semana = models.CharField(max_length=10, choices=DIAS_DA_SEMANA)
    cronograma = models.ForeignKey(Cronograma, on_delete=models.CASCADE, related_name='atividades')

    def clean(self):
        super().clean()
        if self.horario_inicial and self.horario_final >= datetime.time(24, 00):
            raise ValidationError('A duração não pode ser maior que 23:59.')
