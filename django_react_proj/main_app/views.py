from django.shortcuts import render
from .models import Categories, Product,Customer,SaleOrder,SaleOrderLine,Vendor,PurchaseOrder,PurchaseOrderLine

# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def category(request):
  return render(request, 'main_app/category.html')

def product(request):
  products = Product.objects.all()
  return render(request, 'main_app/product.html',{'products':products})

def purchase(request):
  return render(request, 'main_app/purchase.html')

def sale(request):
  return render(request, 'main_app/sale.html')

def customer(request):
  return render(request, 'main_app/customer.html')

def vendor(request):
  return render(request, 'main_app/vendor.html')


