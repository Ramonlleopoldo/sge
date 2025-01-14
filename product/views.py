from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models
from . import forms
from app import metrics
from brand.models import Brand
from category.models import Category


class ProductListView(LoginRequiredMixin, ListView):
    model = models.Product
    template_name = 'product_list.html'
    context_object_name = 'products'
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()
        search_title = self.request.GET.get('search_title')
        search_brand = self.request.GET.get('search_brand')
        search_category = self.request.GET.get('search_category')
        if search_title:
            queryset = queryset.filter(title__icontains=search_title)
        if search_brand:
            queryset = queryset.filter(brand__name__icontains=search_brand)
        if search_category:
            queryset = queryset.filter(category__name__icontains=search_category)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_metrics'] = metrics.get_product_metric()
        context['brands'] = Brand.objects.all()
        context['category'] = Category.objects.all()
        return context


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = models.Product
    form_class = forms.ProductModelForm
    template_name = 'product_create.html'
    success_url = '/products/list/'


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Product
    form_class = forms.ProductModelForm
    template_name = 'product_update.html'
    success_url = '/products/list/'


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Product
    template_name = 'product_delete.html'
    success_url = '/products/list/'


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = models.Product
    template_name = 'product_detail.html'
