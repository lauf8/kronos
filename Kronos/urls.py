from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from apps.orcamento.views import OrcamentoViewSet, DespesaViewSet, RendaViewSet
from apps.cronograma.views import AtividadeViewSet, CronogramaViewSet
from apps.publicacao.views import PublicacaoViewSet, ComentarioViewSet

router = routers.DefaultRouter()
router.register(r'orcamento', OrcamentoViewSet, basename='orcamentos')
router.register(r'despesa', DespesaViewSet, basename='despesas')
router.register(r'renda', RendaViewSet, basename='rendas')
router.register(r'cronograma', CronogramaViewSet, basename='cronogramas')
router.register(r'atividade', AtividadeViewSet, basename='atividades')
router.register(r'publicacao', PublicacaoViewSet, basename='publicacoes')
router.register(r'comentario', ComentarioViewSet, basename='comentarios')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('', include('apps.publicacao.urls')),
]
