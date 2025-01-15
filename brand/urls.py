from django.urls import path
from . import views


urlpatterns = [
    path('brands/list/', views.BrandListView.as_view(), name='brand_list'),
    path('brands/create/', views.BrandCreatedView.as_view(), name='brand_create'),
    path('brands/<int:pk>/update/', views.BrandUpdateView.as_view(), name='brand_update'),
    path('brands/<int:pk>/delete/', views.BrandDeleteView.as_view(), name='brand_delete'),
    path('brands/<int:pk>/detail/', views.BrandDetailView.as_view(), name='brand_detail'),

    path('api/v1/brands/', views.BrandListApiView.as_view(), name='brand_list_api_view'),
    path('api/v1/brands/<int:pk>/', views.BrandRestriveUpdateDelete.as_view(), name='brand_restrive_update_delete_api_view')
]
