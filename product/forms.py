from django import forms
from . import models


class ProductModelForm(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = ['title','category', 'brand', 'serie_number', 'cost_price', 'selling_price', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'brand': forms.Select(attrs={'class': 'form-control'}),
            'serie_number': forms.TextInput(attrs={'class': 'form-control'}),
            'cost_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'selling_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'style': 'max-height: 50px;'}),
        }
        labels = {
            'title': 'Título',
            'brand': 'Marca',
            'category': 'Categoria',
            'serie_number': 'Número de Série',
            'cost_price': 'Preço de Custo',
            'selling_price': 'Preço de Venda',
            'description': 'Descrição',
        }
