from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    qty_on_hand = serializers.IntegerField(read_only=True)
    inventory_valuation = serializers.DecimalField(max_digits=10, decimal_places=3, read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'purchaseCost', 'salePrice', 'qty_on_hand', 'inventory_valuation')
