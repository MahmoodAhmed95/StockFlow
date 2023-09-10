from django.db import models

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=100)
    image = models.TextField()
    number = models.IntegerField()

class Product(models.Model):
    name = models.CharField(max_length=100)
    purchaseCost= models.DecimalField(decimal_places=3)
    salePrice= models.DecimalField(decimal_places=3)
    image = models.TextField()
    categoryId = models.ForeignKey(Categories)
class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    email = models.CharField(max_length=100)
class SaleOrder(models.Model):
    saleDate= models.DateField()
    saleNote = models.TextField()
    customerId= models.ForeignKey(Customer)
class SaleOrderLine(models.Model):
    quantity= models.IntegerField()
    saleId= models.ForeignKey(SaleOrder)
    productId= models.ForeignKey(Product)
class Vendor(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    email = models.CharField(max_length=100)
class PurchaseOrder(models.Model):
    saleDate= models.DateField()
    saleNote = models.TextField()
    vendorId= models.ForeignKey(Vendor)
class PurchaseOrderLine(models.Model):
    quantity= models.IntegerField()
    purchaseId= models.ForeignKey(PurchaseOrder)
    productId= models.ForeignKey(Product)
