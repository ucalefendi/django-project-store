from django.urls import path
from . import views

urlpatterns = [
    #########sade yazilis formasi############################
    path('product-list/',views.product_list,name='product-list'),
    path('product-detail/<int:pk>/',views.product_detail,name='product-detail'),
    path('product_model_function/',views.product_model_function,name='product_model_function'),
    #########################################################################################
    path('product-list/',views.ProductListAV.as_view(),name='product-list'),
    path('product-detail/<int:pk>/',views.ProductDetailAV.as_view(),name='product-detail'),
    path('product_model_function/',views.ProductModelFunctionAV.as_view(),name='product_model_function'),
    # path('sailed_product_details/',views.sailed_product_details,name='sailed_product_details'),
    path('sailedproductdetails/',views.SailedProductDetails.as_view(),name='sailedproductdetails'),
    path('delete_or_is_null_product/<int:pk>/',views.delete_or_is_null_product,name='delete_or_is_null_product'),
    path('sailed-product-detail/<int:pk>/',views.SailedProductDetail.as_view(),name='sailed-product-detail'),
    path('damaged_product/',views.damaged_product.as_view(),name='damaged_product'),
    path('subcategory_lists/',views.subcategory_lists.as_view(),name='subcategory_lists'), 
    path('product_models_list/',views.Productmodellists.as_view(),name='product_models_list'),
]
