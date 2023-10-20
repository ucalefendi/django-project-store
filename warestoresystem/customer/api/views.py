from django.shortcuts import render,redirect,get_list_or_404,get_object_or_404
from customer.models import Order,Customer
from rest_framework.response import Response
from rest_framework import status,generics,serializers
from rest_framework.decorators import api_view
from django.forms.models import model_to_dict
from .serializer import CustomerSerializer,OrderSerializer


class CustomerListAV(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer



class OrderListAV(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer



class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer















