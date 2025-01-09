from django.urls import path
from . import views

urlpatterns = [
    path('inflows/list/', views.InflowListView.as_view(), name='inflow_list'),
    path('inflows/create/', views.InflowCreatedView.as_view(), name='inflow_create'),
    path('inflows/<int:pk>/details/', views.InflowDetailView.as_view(), name='inflow_detail'),
]