from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from apps.orcamento.models import Renda, Despesa, Orcamento
from apps.orcamento.serializers import RendaSerializer, DespesaSerializer, OrcamentoSerializer

class RendaViewSet(viewsets.ModelViewSet):
    queryset = Renda.objects.all()
    serializer_class = RendaSerializer
    
class DespesaViewSet(viewsets.ModelViewSet):
    queryset = Despesa.objects.all()
    serializer_class = DespesaSerializer

class OrcamentoViewSet(viewsets.ModelViewSet):
    queryset = Orcamento.objects.all()
    serializer_class = OrcamentoSerializer