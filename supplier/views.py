from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from . import models
from . import forms


class SupplierListView(ListView):
    model = models.Supplier
    template_name = 'supplier_list.html'
    context_object_name = 'suppliers'

    def get_queryset(self):
        supplier = super().get_queryset()
        search = self.request.GET.get('search')
        if search:
            supplier = models.Supplier.objects.filter(name__icontains = search)
        return supplier

class SupplierCreateView(CreateView):
    model = models.Supplier
    form_class = forms.SupplierModelForm
    template_name = 'supplier_create.html'
    success_url = '/suppliers/list/'

class SupplierUpdateView(UpdateView):
    model = models.Supplier
    form_class = forms.SupplierModelForm
    template_name = 'supplier_update.html'
    success_url = '/suppliers/list/'

class SupplierDeleteView(DeleteView):
    model = models.Supplier
    template_name = 'supplier_delete.html'
    success_url = '/suppliers/list/'

class SupplierDetailView(DetailView):
    model = models.Supplier
    template_name = 'supplier_detail.html'