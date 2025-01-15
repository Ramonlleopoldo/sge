from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from rest_framework import generics
from . import serializers
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from . import models
from . import forms
from app import metrics
from brand.models import Brand
from category.models import Category


class ProductListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Product
    template_name = 'product_list.html'
    context_object_name = 'products'
    paginate_by = 3
    permission_required = 'product.view_product'

    def get_queryset(self):
        queryset = super().get_queryset()
        search_title = self.request.GET.get('search_title')
        search_brand = self.request.GET.get('search_brand')
        search_category = self.request.GET.get('search_category')
        if search_title:
            queryset = queryset.filter(title__icontains=search_title)
        if search_brand:
            queryset = queryset.filter(brand__id=search_brand)
        if search_category:
            queryset = queryset.filter(category__id=search_category)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_metrics'] = metrics.get_product_metric()
        context['brands'] = Brand.objects.all()
        context['categorys'] = Category.objects.all()
        return context


class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Product
    form_class = forms.ProductModelForm
    template_name = 'product_create.html'
    success_url = reverse_lazy('product_list')
    permission_required = 'product.add_product'


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Product
    form_class = forms.ProductModelForm
    template_name = 'product_update.html'
    success_url = reverse_lazy('product_list')
    permission_required = 'product.change_product'


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('product_list')
    permission_required = 'product.delete_product'


class ProductDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Product
    template_name = 'product_detail.html'
    permission_required = 'product.view_product'


class ProductListApiView(generics.ListCreateAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializers


class ProductRestriveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializers
