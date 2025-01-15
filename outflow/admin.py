from django.contrib import admin
from . import models


class OutflowAdmin(admin.ModelAdmin):
    list_display = ['quantity', 'description']
    search_fields = ['product',]


admin.site.register(models.Outflow, OutflowAdmin)
