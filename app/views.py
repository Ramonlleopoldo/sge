from django.shortcuts import render
from . import metrics

def home (request):
    product_metric = metrics.get_product_metric()
    context = {
        'product_metric': product_metric
    }
    return render(request, 'home.html', context)
