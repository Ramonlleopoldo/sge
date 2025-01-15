from django.urls import path
from . import views


urlpatterns = [
    path('suppliers/list/', views.SupplierListView.as_view(), name='supplier_list'),
    path('suppliers/create/', views.SupplierCreateView.as_view(), name='supplier_create'),
    path('suppliers/<int:pk>/update/', views.SupplierUpdateView.as_view(), name='supplier_update'),
    path('suppliers/<int:pk>delete/', views.SupplierDeleteView.as_view(), name='supplier_delete'),
    path('suppliers/<int:pk>detail/', views.SupplierDetailView.as_view(), name='supplier_detail'),

    path('api/v1/supplier/', views.SupplierListApiView.as_view(), name='supplier_list_api_view'),
    path('api/v1/supplier/<int:pk>/', views.SupplierRestriveUpdateDelete.as_view(), name='supplier_restrive_update_delete_api_view')
]
