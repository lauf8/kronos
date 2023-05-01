from rest_framework import viewsets
from apps.cronograma.models import Atividade, Cronograma
from apps.cronograma.serializers import AtividadeSerializer, CronogramaSerializer
   
class AtividadeViewSet(viewsets.ModelViewSet):
    queryset = Atividade.objects.all()
    serializer_class = AtividadeSerializer

class CronogramaViewSet(viewsets.ModelViewSet):
    queryset = Cronograma.objects.all()
    serializer_class = CronogramaSerializer

# Create your views here.
