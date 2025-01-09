from django import forms
from . import models


class OutflowModelForm(forms.ModelForm):
    class Meta:
        model = models.Outflow
        fields = '__all__'
        widgets = {
            'product': forms.Select(attrs={'class': 'form-control custom-select'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'style': 'max-height: 50px;'}),
        }
        labels = {
            'product': 'Produto',
            'quantity': 'Quantidade',
            'description': 'Descrição',
        }
