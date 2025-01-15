from django.contrib import admin
from . import models


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'serie_number', 'cost_price', 'selling_price',]
    search_fields = ['title', 'serie_number']
    exclude = ['quantity']


admin.site.register(models.Product, ProductAdmin)
