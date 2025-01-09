from django import forms
from . import models


class BrandModelForm(forms.ModelForm):
    class Meta:
        model = models.Brand
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }
