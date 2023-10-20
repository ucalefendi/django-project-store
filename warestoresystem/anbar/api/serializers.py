from rest_framework import serializers
from anbar.models import Category,SubCategory,Product,ProductBrand,ProductModel


class ProductSerializer(serializers.ModelSerializer):
    product_brands = serializers.StringRelatedField(read_only=True)
    subcategory = serializers.StringRelatedField(read_only=True)
    product_model = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Product
        fields = '__all__'

class ProductBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductBrand
        fields = '__all__'


class ProductModelSerializer(serializers.ModelSerializer):
    product_brands_info = ProductBrandSerializer(source='product_brands',read_only=True)
    product_brands = serializers.PrimaryKeyRelatedField(queryset=ProductBrand.objects.all(),write_only=True)
    class Meta:
        model = ProductModel
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'
