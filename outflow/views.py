from django.views.generic import ListView, CreateView
from . import models
from . import forms


class OutflowListView(ListView):
    model = models.Outflow
    template_name = 'outflow_list.html'
    context_object_name = 'outflows'

class OutflowCreatedView(CreateView):
    model = models.Outflow
    form_class = forms.OutflowModelForm
    template_name = 'outflow_create.html'
    success_url = '/outflows/list/'