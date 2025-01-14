from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models
from . import forms


class SupplierListView(LoginRequiredMixin, ListView):
    model = models.Supplier
    template_name = 'supplier_list.html'
    context_object_name = 'suppliers'
    paginate_by = 3

    def get_queryset(self):
        supplier = super().get_queryset()
        search = self.request.GET.get('search')
        if search:
            supplier = models.Supplier.objects.filter(name__icontains=search)
        return supplier


class SupplierCreateView(LoginRequiredMixin, CreateView):
    model = models.Supplier
    form_class = forms.SupplierModelForm
    template_name = 'supplier_create.html'
    success_url = '/suppliers/list/'


class SupplierUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Supplier
    form_class = forms.SupplierModelForm
    template_name = 'supplier_update.html'
    success_url = '/suppliers/list/'


class SupplierDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Supplier
    template_name = 'supplier_delete.html'
    success_url = '/suppliers/list/'


class SupplierDetailView(LoginRequiredMixin, DetailView):
    model = models.Supplier
    template_name = 'supplier_detail.html'
