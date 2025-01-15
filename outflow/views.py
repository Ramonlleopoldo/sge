from django.views.generic import ListView, CreateView, DetailView
from rest_framework import generics
from . import serializers
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from . import models
from . import forms
from app import metrics


class OutflowListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Outflow
    template_name = 'outflow_list.html'
    context_object_name = 'outflows'
    paginate_by = 3
    permission_required = 'outflow.view_outflow'

    def get_queryset(self):
        outflow = super().get_queryset()
        search = self.request.GET.get('search')
        if search:
            outflow = outflow.filter(product__title__icontains=search)
        return outflow

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sales_metrics'] = metrics.get_sales_metrics()
        return context


class OutflowCreatedView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Outflow
    form_class = forms.OutflowModelForm
    template_name = 'outflow_create.html'
    success_url = '/outflows/list/'
    permission_required = 'outflow.add_outflow'


class OutflowDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Outflow
    template_name = 'outflow_detail.html'
    permission_required = 'outflow.view_outflow'


class OutflowListApiView(generics.ListCreateAPIView):
    queryset = models.Outflow.objects.all()
    serializer_class = serializers.OutflowSerializers


class OutflowDetailsApiView(generics.RetrieveAPIView):
    queryset = models.Outflow.objects.all()
    serializer_class = serializers.OutflowSerializers
