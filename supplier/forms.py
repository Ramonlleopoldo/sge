from django import forms
from . import models


class SupplierModelForm(forms.ModelForm):
    class Meta:
        model = models.Supplier
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }
