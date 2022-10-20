from tabnanny import verbose
from django.db import models



class Produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.CharField(max_length=500, verbose_name="Descrição")
    preco = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return "{} ({}) R${}".format(self.nome, self.descricao, self.preco)

class Pedido(models.Model):
    none = None

class ItemPedido(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.SET_NULL, null=True)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)