from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from apps.orcamento.views import OrcamentoViewSet, DespesaViewSet, RendaViewSet
from apps.cronograma.views import AtividadeViewSet, CronogramaViewSet

router = routers.DefaultRouter()
router.register(r'orcamento', OrcamentoViewSet, basename='orcamentos')
router.register(r'despesa', DespesaViewSet, basename='despesas')
router.register(r'renda', RendaViewSet, basename='rendas')
router.register(r'cronograma', CronogramaViewSet, basename='cronogramas')
router.register(r'atividade', AtividadeViewSet, basename='atividades')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
