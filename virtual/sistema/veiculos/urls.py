from django.conf.urls import url
from veiculos import views

urlpatterns = [
    url(r'^$', views.listarVeiculos.as_view(), name='listar-veiculos'),
    url(r'novo$', views.novoVeiculo.as_view(), name='novo-veiculos'),
    url(r'^(?P<pk>[0-9]+)/$', views.editarVeiculo.as_view(), name='editar-veiculo'),
    url(r'^excluir/(?P<pk>[0-9]+)/$', views.deletarVeiculos.as_view(), name='deletar-veiculo'),
]