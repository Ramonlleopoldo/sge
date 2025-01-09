from django.views.generic import ListView, CreateView, DetailView
from . import models
from . import forms


class OutflowListView(ListView):
    model = models.Outflow
    template_name = 'outflow_list.html'
    context_object_name = 'outflows'

    def get_queryset(self):
        outflow = super().get_queryset()
        search = self.request.GET.get('search')
        if search:
            outflow = outflow.filter(product__title__icontains=search)
        return outflow


class OutflowCreatedView(CreateView):
    model = models.Outflow
    form_class = forms.OutflowModelForm
    template_name = 'outflow_create.html'
    success_url = '/outflows/list/'


class OutflowDetailView(DetailView):
    model = models.Outflow
    template_name = 'outflow_detail.html'
