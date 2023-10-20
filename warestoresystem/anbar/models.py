from django.db import models

# from django_enum import EnumField
# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class SubCategory(models.Model):
    title = models.CharField(max_length=50)
    category = models.ForeignKey(Category,models.CASCADE,null=True,blank=False)

    def __str__(self):
        return self.title



class ProductBrand(models.Model):
    title = models.CharField(max_length=50) 

    def __str__(self):
        return self.title


class ProductModel(models.Model):
    title = models.CharField(max_length=50)
    product_brands = models.ForeignKey(ProductBrand,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.title






class Product(models.Model):
    title = models.CharField(max_length=50)
    product_brands = models.ForeignKey(ProductBrand,on_delete=models.CASCADE,null=True,blank=True)
    country = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    release_date = models.DateTimeField()
    description = models.TextField()
    involved_date = models.DateTimeField(auto_now_add=True)
    exported_date = models.DateTimeField(null=True,blank=True)
    description = models.TextField()
    subcategory = models.ForeignKey(SubCategory,on_delete=models.CASCADE,null=True,blank=True)
    product_model = models.ForeignKey(ProductModel,on_delete=models.CASCADE,null=True,blank=True)
    damaged = models.BooleanField(default=False)
    damaged_date = models.DateField(auto_now_add=True)
    involved = models.BooleanField(default=False)
    sale_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title



    

    














