from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from rest_framework import generics
from . import serializers
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from . import models
from . import forms


class CategoryListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Category
    template_name = 'category_list.html'
    context_object_name = 'categorys'
    paginate_by = 3
    permission_required = 'category.view_category'

    def get_queryset(self):
        category = super().get_queryset()
        search = self.request.GET.get('search')
        if search:
            category = models.Category.objects.filter(name__icontains=search)
        return category


class CategoryCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Category
    form_class = forms.CategoryModelForm
    template_name = 'category_create.html'
    success_url = reverse_lazy('category_list')
    permission_required = 'category.add_category'


class CategoryUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Category
    form_class = forms.CategoryModelForm
    template_name = 'category_update.html'
    success_url = reverse_lazy('category_list')
    permission_required = 'category.change_category'


class CategoryDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Category
    template_name = 'category_delete.html'
    success_url = reverse_lazy('category_list')
    permission_required = 'category.delete_category'


class CategoryDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Category
    template_name = 'category_detail.html'
    permission_required = 'category.view_category'


class CategoryListApiView(generics.ListCreateAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializers


class CategoryRestriveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializers
