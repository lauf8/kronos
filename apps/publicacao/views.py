from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from apps.publicacao.models import Publicacao, Comentario
from apps.publicacao.serializers import PublicacaoSerializer, ComentarioSerializer

class PublicacaoViewSet(viewsets.ModelViewSet):
    queryset = Publicacao.objects.all()
    serializer_class = PublicacaoSerializer

class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

class PublicacaoApiView(APIView):
    def get(self, request,publicacao):
            # publicacao = Publicacao.objects.filter(id=publicacao).fist()
            publicacao = get_object_or_404(Publicacao, id=publicacao)
            comentarios = Comentario.objects.filter(publicacao=publicacao)

            serializer1 = PublicacaoSerializer(publicacao, many=False)
            serializer2 = ComentarioSerializer(comentarios, many=True)
            results = {
            'Publicação': serializer1.data,
            'Comentários': serializer2.data,
 
        }

            return Response(results)

