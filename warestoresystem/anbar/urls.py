from django.urls import path,include
from . import views

app_name = 'anbar'


urlpatterns = [
    path('ProductCount/',views.ProductCount,name='productcount'),
    path('Sailed_product_count/',views.Sailed_product_count,name='sailed'),
    path('delete_or_is_null_product/',views.delete_or_is_null_product,name='delete-or-is-null'),
    path('damaged_product_count/',views.damaged_product_count,name='damaged'),
    path('subcategory_lists/',views.subcategory_lists,name='subcategory_lists'),
    path('sailed_productbrandlist',views.sailed_productbrandlist,name='sailed-product-brand'),
    path('Productmodellists',views.Productmodellists,name='producmodellis'),
    path('',include('anbar.api.urls')),
]
