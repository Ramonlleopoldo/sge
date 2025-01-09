from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from . import models
from . import forms


class CategoryListView(ListView):
    model = models.Category
    template_name = 'category_list.html'
    context_object_name = 'categorys'

    def get_queryset(self):
        category = super().get_queryset()
        search = self.request.GET.get('search')
        if search:
            category = models.Category.objects.filter(name__icontains = search)
        return category

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

class CategoryDetailView(DetailView):
    model = models.Category
    template_name = 'category_detail.html'
