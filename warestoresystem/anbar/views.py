from django.shortcuts import render,redirect,get_list_or_404
from .models import Category,SubCategory,Product,ProductBrand,ProductModel
from datetime import date, timedelta
# Create your views here.


def ProductCount(request):
    products = Product.objects.all()
    return   render(request,context={'products':products})

def Sailed_product_count(request):
    sailed_count = Product.objects.filter(damaged=False).count()
    return render(request, 'sailed_product_count.html', context={'sailed_count': sailed_count})  

def delete_or_is_null_product(request):
    products = Product.objects.all()
    if products.exists():
        return render(request,context={'message':'products exists'})
    else:
        return  render(request,context={'message':'products not exists'}) 

    

def damaged_product_count(request):
    damaged_count = Product.objects.filter(damaged=True).count()  
    return damaged_count

def subcategory_lists(request):
    subcategorys = SubCategory.objects.all()
    return render(request,context={'subcategorys': subcategorys})



def  sailed_productbrandlist(request):

    productbrands = ProductBrand.objects.all()
    products = Product.objects.all().filter(involved_date__gt = date.today() - timedelta(30))
    return render(request,context={'productbrands':productbrands,'products':products})


def Productmodellists(request):
    productmodels = ProductModel.objects.all()
    return render(request,context={'productmodels':productmodels})








