from rest_framework import serializers
from .models import Product,Categories,Customer,SaleOrder,SaleOrderLine,Vendor,PurchaseOrder,PurchaseOrderLine

# class ProductSerializer(serializers.ModelSerializer):
#     qty_on_hand = serializers.IntegerField(read_only=True)
#     inventory_valuation = serializers.DecimalField(max_digits=10, decimal_places=3, read_only=True)
#     class Meta:
#         model = Product
#         fields = ('id', 'name', 'purchaseCost', 'salePrice', 'qty_on_hand', 'inventory_valuation')
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'purchaseCost', 'salePrice', 'image', 'categoryId')
class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ('id', 'name', 'image')

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'name', 'phone', 'email')

class SaleOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleOrder
        fields = ('id', 'saleDate', 'saleNote', 'confirmed','customerId')

class SaleOrderLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleOrderLine
        fields = ('id', 'quantity', 'saleId', 'productId')

class VendorSerializer(serializers.ModelSerializer):
       class Meta:
        model = Vendor
        fields = ('id', 'name', 'phone', 'email')

class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = ('id', 'purchaseDate', 'purchaseNote', 'confirmed','vendorId')

class PurchaseOrderLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrderLine
        fields = ('id', 'quantity', 'purchaseId', 'productId')