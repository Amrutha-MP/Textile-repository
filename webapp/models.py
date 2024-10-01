from django.db import models

# Create your models here.
class ContactDb(models.Model):
    Name=models.CharField(max_length=50,null=True,blank=True)
    Email_Id=models.EmailField(max_length=50,null=True,blank=True)
    Message=models.CharField(max_length=50,null=True,blank=True)
class RegisterDb(models.Model):
    User_Name=models.CharField(max_length=50,null=True,blank=True)
    Email=models.EmailField(max_length=50,null=True,blank=True)
    Password=models.CharField(max_length=50,null=True,blank=True)
    CPassword = models.CharField(max_length=50, null=True, blank=True)
class CartDb(models.Model):
    User_Name=models.CharField(max_length=50,null=True,blank=True)
    Product_Name=models.CharField(max_length=50,null=True,blank=True)
    Quantity=models.IntegerField(null=True,blank=True)
    Price=models.IntegerField(null=True,blank=True)
    Total_price = models.IntegerField(null=True, blank=True)

class Checkout_DB(models.Model):
    User_Name=models.CharField(max_length=50,null=True,blank=True)
    Email=models.EmailField(max_length=50,null=True,blank=True)
    Place=models.CharField(max_length=50,null=True,blank=True)
    Address=models.TextField(max_length=50,null=True,blank=True)
    Mobile=models.IntegerField(null=True,blank=True)
    Message=models.CharField(max_length=50,null=True,blank=True)
    Total_price=models.IntegerField(null=True, blank=True)