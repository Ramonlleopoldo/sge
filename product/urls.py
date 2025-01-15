from django.urls import path
from . import views


urlpatterns = [
    path('products/list/', views.ProductListView.as_view(), name='product_list'),
    path('products/create/', views.ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/update/', views.ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product_delete'),
    path('products/<int:pk>/detail/', views.ProductDetailView.as_view(), name='product_detail'),

    path('api/v1/product/', views.ProductListApiView.as_view(), name='product_list_api_view'),
    path('api/v1/product/<int:pk>/', views.ProductRestriveUpdateDelete.as_view(), name='product_restrive_update_delete_api_view')


]
