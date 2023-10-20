from django.shortcuts import render,redirect,get_list_or_404,get_object_or_404
from anbar.models import Category,SubCategory,Product,ProductBrand,ProductModel
from customer.models import Order,Customer
from rest_framework.response import Response
from rest_framework import status,generics
from rest_framework.decorators import api_view
from django.forms.models import model_to_dict
from .serializers import ProductSerializer,ProductBrandSerializer,ProductModelSerializer,SubCategorySerializer
from datetime import date, timedelta
# model:Product
@api_view(['GET','POST'])
def product_list(request):
    products = Product.objects.all()
    if request.method == 'GET':
        # products_data = products.values_list() ---> bu kod da dogrudur
        # return Response(products_data) ---> bu kod da dogrudur
        #########Serializer ile yazilis qaydasi##################
        serializer = ProductSerializer(products,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        # title = request.data.get('title')
        # product_brands = request.data.get('product_brands')
        # subcategory = request.data.get('subcategory')
        # release_date = request.data.get('release_date')
        # new_product = Product.objects.create(title=title,product_brands_id=product_brands,subcategory_id=subcategory,release_date=release_date)
        # return Response(model_to_dict(new_product),status=status.HTTP_201_CREATED)
        ##########Serializer ile yazilis qaydasi###################
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
# #model:ProductBrand
@api_view(['GET','PUT','DELETE']) 
def product_detail(request,pk):
    # product_brands = ProductBrand.objects.get(pk=pk) --> 
    product_brands = get_object_or_404(ProductBrand,pk=pk) #----> 404 erroru almaq ucun bu kodu da yaza bilerik
    if request.method == 'GET':
        # brand_data = model_to_dict(product_brands) ---> bu kod da dogrudur  
        # return  Response(brand_data)---> bu kod da dogrudur
        ##########Serializer ile yazilis qaydasi###################
        serializer = ProductBrandSerializer(product_brands)
        return Response(serializer.data)
    elif request.method == 'PUT':
        # title = request.data.get('title') ---> bu kod da dogrudur 
        # product_brands.title = title ---> bu kod da dogrudur 
        # product_brands.save()---> bu kod da dogrudur 
        # product_brands_data = model_to_dict(product_brands) ---> bu kod da dogrudur 
        # return Response(product_brands_data,status=status.HTTP_202_ACCEPTED) ---> bu kod da dogrudur
        ##########Serializer ile yazilis qaydasi###################
        serializer = ProductBrandSerializer(product_brands,data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        # else:
        #     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        product_brands.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
# #model:ProductModel()
@api_view(['GET','POST'])
def product_model_function(request): 
    product_model = ProductModel.objects.all()
    if request.method == 'GET':
        # product_models_data = product_model.values_list() ---> bu kod da dogrudur
        # return Response(product_models_data) ---> bu kod da dogrudur
        ##########Serializer ile yazilis qaydasi###################
        serializer = ProductModelSerializer(product_model,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        # title = request.data.get('title') ---> bu kod da dogrudur
        # product_brands = request.data.get('product_brands') ---> bu kod da dogrudur
        # new_model = ProductModel.objects.create(title=title,product_brands_id=product_brands) ---> bu kod da dogrudur
        # return Response(model_to_dict(new_model),status=status.HTTP_201_CREATED) ---> bu kod da dogrudur
        ##########Serializer ile yazilis qaydasi###################
        serializer = ProductModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


# yuxaridaki kodlarin GENERICS formatinda yazilmasi qaydasi

#model: Product
class ProductListAV(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 

#model: ProductBrand    
class ProductDetailAV(generics.RetrieveUpdateAPIView):
    queryset = ProductBrand.objects.all()
    serializer_class =  ProductBrandSerializer 

#model:ProductModel
class ProductModelFunctionAV(generics.ListCreateAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductModelSerializer

    

# Anbar APP-inde isdifade olunan viewslerin API -a cevrilmesi.

#bu kod anbarda satilmis mehsullari gosderir
@api_view(['GET','POST'])
def Sailed_product_count(request):
    sailed_products = Product.objects.all().filter(damaged=False)
    serializer = ProductSerializer(sailed_products, many=True)
    return Response(serializer.data) 

# model:Product
#bu kod anbarda satilmis mehsullari gosderir
class SailedProductDetails(generics.ListCreateAPIView):
    queryset = Product.objects.all().filter(damaged=False)
    serializer_class = ProductSerializer

# Model:Product 
#bu kod anbarda satilmis mehsulu gosderir.Verilmis Pk deyerine uygun.
class SailedProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all().filter(damaged=False)
    serializer_class = ProductSerializer    

#bu kod anbarda zerer cekmis mehsullari gosderir
class damaged_product(generics.ListCreateAPIView):  
    queryset = Product.objects.filter(damaged=True)
    serializer_class = ProductSerializer

#*************************************************************************
#bu kod anbarda 'subcategory'-e aid mehsullarin lisdini gosderir
class subcategory_lists(generics.ListCreateAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
#*************************************************************************


#bu kod Product modellerinin listini gosderir
class Productmodellists(generics.ListCreateAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductModelSerializer


    



#bu kod anbarda olan ve ya olmayan mehsullari gosderir.
@api_view(['GET'])
def delete_or_is_null_product(request,pk):
    if request.method == 'GET':
        products = get_object_or_404(Product,pk=pk)
        serializer = ProductSerializer(products)
        return Response(serializer.data)
     





    



    