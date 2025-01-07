from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from . import models
from . import forms


class BrandListView(ListView):
    model = models.Brand
    template_name = 'brand_list.html'
    context_object_name = 'brands'

class BrandCreatedView(CreateView):
    model = models.Brand
    form_class = forms.BrandModelForm
    template_name = 'new_brand.html'
    success_url = '/brands/list/'

class BrandUpdateView(UpdateView):
    model = models.Brand
    form_class = forms.BrandModelForm
    template_name = 'brand_update.html'
    success_url = '/brands/list/'

class BrandDeleteView(DeleteView):
    model = models.Brand
    template_name = 'brand_delete.html'
    success_url = '/brands/list/'

    


