from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from . import models
from . import forms


class CategoryListView(ListView):
    model = models.Category
    template_name = 'category_list.html'
    context_object_name = 'categorys'

class CategoryCreateView(CreateView):
    model = models.Category
    form_class = forms.CategoryModelForm
    template_name = 'category_create.html'
    success_url = '/categorys/list/'
    
class CategoryUpdateView(UpdateView):
    model = models.Category
    form_class = forms.CategoryModelForm
    template_name = 'category_update.html'
    success_url = '/categorys/list/'

class CategoryDeleteView(DeleteView):
    model = models.Category
    template_name = 'category_delete.html'
    success_url = '/categorys/list/'