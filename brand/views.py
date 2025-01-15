from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from rest_framework import generics
from . import serializers
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from . import models
from . import forms


class BrandListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Brand
    template_name = 'brand_list.html'
    context_object_name = 'brands'
    paginate_by = 3
    permission_required = 'brand.view_brand'

    def get_queryset(self):
        brand = super().get_queryset()
        search = self.request.GET.get('search')
        if search:
            brand = models.Brand.objects.filter(name__icontains=search)
        return brand


class BrandCreatedView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Brand
    form_class = forms.BrandModelForm
    template_name = 'new_brand.html'
    success_url = reverse_lazy('brand_list')
    permission_required = 'brand.add_brand'


class BrandUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Brand
    form_class = forms.BrandModelForm
    template_name = 'brand_update.html'
    success_url = reverse_lazy('brand_list')
    permission_required = 'brand.change_brand'


class BrandDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Brand
    template_name = 'brand_delete.html'
    success_url = reverse_lazy('brand_list')
    permission_required = 'brand.delete_brand'


class BrandDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Brand
    template_name = 'brand_detail.html'
    permission_required = 'brand.view_brand'


class BrandListApiView(generics.ListCreateAPIView):
    queryset = models.Brand.objects.all()
    serializer_class = serializers.BrandSerializers


class BrandRestriveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Brand.objects.all()
    serializer_class = serializers.BrandSerializers
