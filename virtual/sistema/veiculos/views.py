from veiculos.models import Veiculo
from django.views.generic import ListView, CreateView
from django.core.urlresolvers import reverse_lazy
from veiculos.forms import *

class listarVeiculos(ListView):
    """
    View para listar veiculos cadastrados
    """
    model = Veiculo
    template_name = 'veiculos/listar.html'

class novoVeiculo(CreateView):
    """
    View para a criacao de novos veiculos.
    """
    model = Veiculo
    form_class = FormularioVeiculo
    template_name = 'veiculos/novo.html'
    success_url = reverse_lazy('listar-veiculos')