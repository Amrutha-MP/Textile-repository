from django.db import models

# Create your models here.
class Textiles_Db(models.Model):
    Category_Name=models.CharField(max_length=50,null=True,blank=True)
    Description =models.CharField(max_length=50,null=True,blank=True)
    Category_Image=models.ImageField(upload_to="profile images",null=True,blank=True)
class ProductDb(models.Model):
    CategoryName=models.CharField(max_length=50,null=True,blank=True)
    Product_Name=models.CharField(max_length=50,null=True,blank=True)
    Description=models.CharField(max_length=50,null=True,blank=True)
    Price=models.IntegerField(null=True,blank=True)
    Brand_Name=models.CharField(max_length=50,null=True,blank=True)
    CategoryImage1=models.ImageField(upload_to="product images",null=True,blank=True)
    CategoryImage2 = models.ImageField(upload_to="product images", null=True, blank=True)
    CategoryImage3 = models.ImageField(upload_to="product images", null=True, blank=True)