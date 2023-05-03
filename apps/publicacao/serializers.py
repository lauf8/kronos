from rest_framework import serializers
from apps.publicacao.models import Publicacao, Comentario

class PublicacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publicacao
        fields = '__all__'

class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = '__all__'