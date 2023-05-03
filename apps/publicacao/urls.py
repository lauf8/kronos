from apps.publicacao.views import PublicacaoApiView
from django.urls import path 

urlpatterns = [
    path('publicacao/teste/<int:publicacao>', PublicacaoApiView.as_view(), name='publicacoes'),
    
]