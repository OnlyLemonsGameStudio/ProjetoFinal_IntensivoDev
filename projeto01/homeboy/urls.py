from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('cliente/', views.cliente, name='cliente'),
    path('loja/', views.loja, name='loja'),
    path('entregador/', views.entregador, name='entregador'),
    path('loja/produto_add/', views.produto_add, name='produto_add'),
    path('loja/produto_edit/<int:produto_pk>', views.produto_edit, name='produto_edit'),
    path('loja/produto_delete/<int:produto_pk>', views.produto_delete, name='produto_delete'),
    #path('cliente/pedido/', views.pedido, name='pedido'),
]