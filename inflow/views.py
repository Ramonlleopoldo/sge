from django.views.generic import ListView, CreateView, DetailView
from rest_framework import generics
from . import serializers
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from . import models
from . import forms


class InflowListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Inflow
    template_name = 'inflow_list.html'
    context_object_name = 'inflows'
    paginate_by = 3
    permission_required = 'inflow.view_inflow'

    def get_queryset(self):
        queryset = super().get_queryset()
        search_product = self.request.GET.get('search_product')
        search_supplier = self.request.GET.get('search_supplier')
        if search_product:
            queryset = queryset.filter(product__title__icontains=search_product)
        if search_supplier:
            queryset = queryset.filter(supplier__name__icontains=search_supplier)
        return queryset


class InflowCreatedView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Inflow
    form_class = forms.InflowModelForm
    template_name = 'inflow_create.html'
    success_url = '/inflows/list/'
    permission_required = 'inflow.add_inflow'


class InflowDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Inflow
    template_name = 'inflow_detail.html'
    permission_required = 'inflow.view_inflow'


class InflowListApiView(generics.ListCreateAPIView):
    queryset = models.Inflow.objects.all()
    serializer_class = serializers.InflowSerializers


class InflowDetailsApiView(generics.RetrieveAPIView):
    queryset = models.Inflow.objects.all()
    serializer_class = serializers.InflowSerializers
