from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),

    path('', include('brand.urls')),
    path('', include('category.urls')),
    path('', include('supplier.urls')),
    path('', include('product.urls')),
    path('', include('inflow.urls')),
    path('', include('outflow.urls')),
]
