from django.urls import path,include
from . import views


urlpatterns = [
    path('customer-list/',views.CustomerListAV.as_view(),name='customer-list'),
    path('customer-detail/<int:pk>/',views.CustomerDetail.as_view(),name='customer-detail'),
    path('order-list/',views.OrderListAV.as_view(),name='order-list'),
    path('order-detail/<int:pk>/',views.OrderDetail.as_view(),name='order-detail'),
]
