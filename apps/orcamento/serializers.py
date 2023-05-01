from rest_framework import serializers
from apps.orcamento.models import Orcamento, Despesa, Renda

class DespesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Despesa
        fields = '__all__'

class RendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Renda
        fields = '__all__'

class OrcamentoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Orcamento
        fields = '__all__'