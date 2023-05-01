from rest_framework import serializers
from apps.cronograma.models import Cronograma, Atividade

class CronogramaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cronograma
        fields = '__all__'

class AtividadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atividade
        fields = '__all__'