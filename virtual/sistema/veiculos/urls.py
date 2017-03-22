from django.conf.urls import url
from veiculos import views

urlpatterns = [
    url(r'^$', views.listarVeiculos.as_view(), name='listar-veiculos'),
    url(r'novo$', views.novoVeiculo.as_view(), name='novo-veiculos'),
]