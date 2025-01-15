from django.urls import path
from . import views


urlpatterns = [
    path('categorys/list/', views.CategoryListView.as_view(), name='category_list'),
    path('categorys/create/', views.CategoryCreateView.as_view(), name='category_create'),
    path('categorys/<int:pk>/update/', views.CategoryUpdateView.as_view(), name='category_update'),
    path('categorys/<int:pk>delete/', views.CategoryDeleteView.as_view(), name='category_delete'),
    path('categorys/<int:pk>detail/', views.CategoryDetailView.as_view(), name='category_detail'),

    path('api/v1/category/', views.CategoryListApiView.as_view(), name='category_list_api_view'),
    path('api/v1/category/<int:pk>/', views.CategoryRestriveUpdateDelete.as_view(), name='category_restrive_update_delete_api_view')
]
