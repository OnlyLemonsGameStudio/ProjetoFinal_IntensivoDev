from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse

from .models import Produto, Pedido, ItemPedido
from .forms import ProdutoForm

def home(request):
    return render(request, "index.html")

def cliente(request):
    if request.method == "GET":
        produtos = Produto.objects.all()
        context = {
            'produtos': produtos,
            }
        return render(request, "cliente.html", context)
    

def pedido(request):
    pedido = Pedido.objects.all()
    #produtos = pedido.get_itens()
    context = {
        'pedidos': pedido,
        }
    return render(request, "pedido.html", context)

def add_item(request, item_pk):
    produto = Produto.objects.get(pk=item_pk)
    pedido_item, status = ItemPedido.objects.get_or_create(produto=produto)
    pedido_, status = Pedido.objects.get_or_create()
    pedido_.itens.add(pedido_item)
    pedido_.save()
    return redirect('pedido')

def delete_item(request, item_pk):
    item_to_delete = ItemPedido.objects.filter(pk=item_pk)
    if item_to_delete.exists():
        item_to_delete[0].delete()
        messages.info(request, "Item deletado")
    return redirect('pedido')

def entregador(request):
    return render(request, "entregador.html")

def loja(request):
    produtos = Produto.objects.all()
    context = {
        'produtos': produtos,
        }
    return render(request, 'loja.html', context)

def produto_add(request):
    if request.method == "GET":
        return render(request, 'produto_add.html')
    else:
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        preco = request.POST.get('preco')
        produto = Produto(nome = nome, descricao = descricao, preco = preco)
        produto.save()
        return redirect('loja')

def produto_edit(request, produto_pk):
    produto = Produto.objects.get(pk=produto_pk)
    form = ProdutoForm(request.POST or None, instance=produto)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('loja')
    
    context = {
        'produto': produto.id,
        'form': form,
    }

    return render(request, "produto_edit.html", context)

def produto_delete(request, produto_pk):
    produto = Produto.objects.get(pk=produto_pk)
    produto.delete()
    return redirect('loja')

        