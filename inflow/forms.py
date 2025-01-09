from django import forms
from . import models


class InflowModelForm(forms.ModelForm):
    class Meta:
        model = models.Inflow
        fields = '__all__'
        widgets = {
            'supplier': forms.Select(attrs={'class': 'form-control custom-select'}),  # Estilizar campo supplier
            'product': forms.Select(attrs={'class': 'form-control custom-select'}),   # Estilizar campo product
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'style': 'max-height: 50px;'}),
        }
        labels = {
            'product': 'Produto',
            'supplier': 'Fornecedor',
            'quantity': 'Quantidade',
            'description': 'Descrição',
        }
