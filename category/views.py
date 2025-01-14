from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models
from . import forms


class CategoryListView(LoginRequiredMixin, ListView):
    model = models.Category
    template_name = 'category_list.html'
    context_object_name = 'categorys'
    paginate_by = 3

    def get_queryset(self):
        category = super().get_queryset()
        search = self.request.GET.get('search')
        if search:
            category = models.Category.objects.filter(name__icontains=search)
        return category


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = models.Category
    form_class = forms.CategoryModelForm
    template_name = 'category_create.html'
    success_url = '/categorys/list/'



class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Category
    form_class = forms.CategoryModelForm
    template_name = 'category_update.html'
    success_url = '/categorys/list/'


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Category
    template_name = 'category_delete.html'
    success_url = '/categorys/list/'


class CategoryDetailView(LoginRequiredMixin, DetailView):
    model = models.Category
    template_name = 'category_detail.html'
