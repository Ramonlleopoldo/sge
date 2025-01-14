from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models
from . import forms


class InflowListView(LoginRequiredMixin, ListView):
    model = models.Inflow
    template_name = 'inflow_list.html'
    context_object_name = 'inflows'
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()
        search_product = self.request.GET.get('search_product')
        search_supplier = self.request.GET.get('search_supplier')
        if search_product:
            queryset = queryset.filter(product__title__icontains=search_product)
        if search_supplier:
            queryset = queryset.filter(supplier__name__icontains=search_supplier)
        return queryset


class InflowCreatedView(LoginRequiredMixin, CreateView):
    model = models.Inflow
    form_class = forms.InflowModelForm
    template_name = 'inflow_create.html'
    success_url = '/inflows/list/'


class InflowDetailView(LoginRequiredMixin, DetailView):
    model = models.Inflow
    template_name = 'inflow_detail.html'
