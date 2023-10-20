from django.contrib import admin
from .models import *
# Register your models here.

# class Meta:
#     model = ExchangeProducts
#     fields = '__all__'


admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(ProductBrand)
admin.site.register(ProductModel)
# admin.site.register(ExchangeProducts)
admin.site.register(Product)
