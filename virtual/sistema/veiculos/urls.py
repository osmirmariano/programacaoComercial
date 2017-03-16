from django.conf.urls import url
from veiculos import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]