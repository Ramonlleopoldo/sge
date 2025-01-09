from django.urls import path
from . import views

urlpatterns = [
    path('outflows/list/', views.OutflowListView.as_view(), name='outflow_list'),
    path('outflows/create/', views.OutflowCreatedView.as_view(), name='outflow_create'),
]