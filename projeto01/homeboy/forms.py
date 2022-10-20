from operator import attrgetter
from socket import fromshare
from turtle import width
from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ('nome', 'descricao', 'preco')

        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control','autofocus':''}),
            'descricao': forms.Textarea(attrs={'class':'forms-control'}),
            'preco': forms.NumberInput(attrs={'class':'forms-control'}),
        }