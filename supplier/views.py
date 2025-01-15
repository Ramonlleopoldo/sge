from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from rest_framework import generics
from . import serializers
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from . import models
from . import forms


class SupplierListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Supplier
    template_name = 'supplier_list.html'
    context_object_name = 'suppliers'
    paginate_by = 3
    permission_required = 'supplier.view_supplier'

    def get_queryset(self):
        supplier = super().get_queryset()
        search = self.request.GET.get('search')
        if search:
            supplier = models.Supplier.objects.filter(name__icontains=search)
        return supplier


class SupplierCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Supplier
    form_class = forms.SupplierModelForm
    template_name = 'supplier_create.html'
    success_url = '/suppliers/list/'
    permission_required = 'supplier.add_supplier'


class SupplierUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Supplier
    form_class = forms.SupplierModelForm
    template_name = 'supplier_update.html'
    success_url = '/suppliers/list/'
    permission_required = 'supplier.change_supplier'


class SupplierDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Supplier
    template_name = 'supplier_delete.html'
    success_url = '/suppliers/list/'
    permission_required = 'supplier.delete_supplier'


class SupplierDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Supplier
    template_name = 'supplier_detail.html'
    permission_required = 'supplier.view_supplier'

class SupplierListApiView(generics.ListCreateAPIView):
    queryset = models.Supplier.objects.all()
    serializer_class = serializers.SupplierSerializers

class SupplierRestriveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Supplier.objects.all()
    serializer_class = serializers.SupplierSerializers
