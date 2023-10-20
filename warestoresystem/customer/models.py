from django.db import models
from django.contrib.auth.models import User
import django.utils.timezone
from anbar.models import *



# Create your models here.

class Order(models.Model):
  
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null=True,blank=True)
    quantity = models.IntegerField()
    order_date = models.DateTimeField(auto_now_add=True)
    # status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE,null=True,blank=True)
    payment_method = models.CharField(max_length=50)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_address = models.CharField(max_length=100)
    billing_address = models.CharField(max_length=100,default='')
    is_expedited_shipping = models.BooleanField(default=False)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Order {self.id} - Product: {self.product}, Quantity: {self.quantity}, Date: {self.order_date}"


class Customer(models.Model):
    
    user = models.ForeignKey(User,on_delete=models.PROTECT)    
    filial_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)


    def __str__(self):
        return self.filial_name
    





    
