from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from . import models
from . import forms


class InflowListView(ListView):
    model = models.Inflow
    template_name = 'inflow_list.html'
    context_object_name = 'inflows'

class InflowCreatedView(CreateView):
    model = models.Inflow
    form_class = forms.InflowModelForm
    template_name = 'inflow_create.html'
    success_url = '/inflows/list/'
    


