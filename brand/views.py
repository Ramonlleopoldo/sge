from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from . import models
from . import forms


class BrandListView(ListView):
    model = models.Brand
    template_name = 'brand_list.html'
    context_object_name = 'brands'
    paginate_by = 3

    def get_queryset(self):
        brand = super().get_queryset()
        search = self.request.GET.get('search')
        if search:
            brand = models.Brand.objects.filter(name__icontains=search)
        return brand


class BrandCreatedView(CreateView):
    model = models.Brand
    form_class = forms.BrandModelForm
    template_name = 'new_brand.html'
    success_url = '/brands/list/'


class BrandUpdateView(UpdateView):
    model = models.Brand
    form_class = forms.BrandModelForm
    template_name = 'brand_update.html'
    success_url = '/brands/list/'


class BrandDeleteView(DeleteView):
    model = models.Brand
    template_name = 'brand_delete.html'
    success_url = '/brands/list/'


class BrandDetailView(DetailView):
    model = models.Brand
    template_name = 'brand_detail.html'
