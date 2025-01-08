from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from . import models
from . import forms


class ProductListView(ListView):
    model = models.Product
    template_name = 'product_list.html'
    context_object_name = 'products'

class ProductCreateView(CreateView):
    model = models.Product
    form_class = forms.ProductModelForm
    template_name = 'product_create.html'
    success_url = '/products/list/'

class ProductUpdateView(UpdateView):
    model = models.Product
    form_class = forms.ProductModelForm
    template_name = 'product_update.html'
    success_url = '/products/list/'

class ProductDeleteView(DeleteView):
    model = models.Product
    template_name = 'product_delete.html'
    success_url = '/products/list/'