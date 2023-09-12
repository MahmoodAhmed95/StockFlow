from django.contrib import admin
from .models import Product,PurchaseOrder,PurchaseOrderLine,SaleOrder,SaleOrderLine,Customer,Vendor,Categories

# Register your models here.
admin.site.register(Product)
admin.site.register(PurchaseOrder)
admin.site.register(PurchaseOrderLine)
admin.site.register(SaleOrder)
admin.site.register(SaleOrderLine)
admin.site.register(Customer)
admin.site.register(Vendor)
admin.site.register(Categories)