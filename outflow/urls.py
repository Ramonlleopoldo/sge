from django.urls import path
from . import views

urlpatterns = [
    path('outflows/list/', views.OutflowListView.as_view(), name='outflow_list'),
    path('outflows/create/', views.OutflowCreatedView.as_view(), name='outflow_create'),
    path('outflows/<int:pk>/details/', views.OutflowDetailView.as_view(), name='outflow_detail'),

    path('api/v1/outflow/', views.OutflowListApiView.as_view(), name='outflow_list_api_view'),
    path('api/v1/outflow/<int:pk>/', views.OutflowDetailsApiView.as_view(), name='outflow_restrive_api_view')
]
