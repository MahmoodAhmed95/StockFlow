from django.shortcuts import render,redirect, get_object_or_404
from .models import Categories, Product,Customer,SaleOrder,SaleOrderLine,Vendor,PurchaseOrder,PurchaseOrderLine
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import Sum

# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')
# Category View
def category(request):
  categories = Categories.objects.all()
  return render(request, 'main_app/categories/category.html',{
'categories': categories
  })
def categories_detail(request, category_id):
    category = get_object_or_404(Categories, id=category_id)
    products = Product.objects.filter(categoryId=category)
    return render(request, 'main_app/categories/detail.html', {'category': category, 'products': products})
class CategoryCreate(CreateView):
  model = Categories
  fields = ['name','image']

class CategoryUpdate(UpdateView):
  model = Categories
  fields = ['name','image']
  
class CategoryDelete(DeleteView):
  model = Categories
  success_url = '/categories/category'

# product views 
def productList(request):
  products = Product.objects.all()
  for product in products:
        # total purchased
        total_purchased = PurchaseOrderLine.objects.filter(productId=product).aggregate(Sum('quantity'))['quantity__sum'] or 0
        # total solded
        total_sold = SaleOrderLine.objects.filter(productId=product).aggregate(Sum('quantity'))['quantity__sum'] or 0
        # qty on hand 
        qty_on_hand = total_purchased - total_sold
        # Calculate Inventory Valuation by multiplying Purchase Cost and Qty On Hand
        inventory_valuation = product.purchaseCost * qty_on_hand
        # attach both to the product
        product.qty_on_hand = qty_on_hand
        product.inventory_valuation = inventory_valuation
  return render(request, 'main_app/product/productList.html',{'products':products})
def addProduct(request):
  return render(request, 'main_app/product/addProduct.html')
def editProduct(request):
  return render(request, 'main_app/product/editProduct.html')
# purchase view
def purchaseList(request):
  purchases = PurchaseOrder.objects.all()
  return render(request, 'main_app/purchase/purchaseList.html',{'purchases':purchases})
def addPurchase(request):
  return render(request, 'main_app/purchase/addPurchase.html')
def editPurchase(request):
  return render(request, 'main_app/purchase/editPurchase.html')
# sale view
def saleList(request):
  sales = SaleOrder.objects.all()
  return render(request, 'main_app/sale/saleList.html',{'sales':sales})
def addSale(request):
  return render(request, 'main_app/sale/addSale.html')
def editSale(request):
  return render(request, 'main_app/sale/editSale.html')
# customer view
def customerList(request):
  customers = Customer.objects.all()
  return render(request, 'main_app/customer/customerList.html',{'customers':customers})
def addCustomer(request):
  return render(request, 'main_app/customer/addCustomer.html')
def editCustomer(request):
  return render(request, 'main_app/customer/editCustomer.html')
# vendor view
def vendorList(request):
  vendors = Vendor.objects.all()
  return render(request, 'main_app/vendor/vendorList.html', {'vendors':vendors})
def addVendor(request):
  return render(request, 'main_app/vendor/addVendor.html')
def editVendor(request):
  return render(request, 'main_app/vendor/editVendor.html')

#product
class productCreate(CreateView):
  model = Product
  fields = '__all__'
class productUpdate(UpdateView):
  model = Product
  fields = ['name', 'purchaseCost', 'salePrice', 'image', 'categoryId']
class productDelete(DeleteView):
  model = Product
  success_url = '/product/productList'

# vendor
class vendorCreate(CreateView):
  model = Vendor
  fields = '__all__'
class vendorUpdate(UpdateView):
  model = Vendor
  fields = ['name', 'phone', 'email']
class vendorDelete(DeleteView):
  model = Vendor
  success_url = '/vendor/vendorList'

# customer
class customerCreate(CreateView):
  model = Customer
  fields = '__all__'
class customerUpdate(UpdateView):
  model = Customer
  fields = ['name', 'phone', 'email']
class customerDelete(DeleteView):
  model = Customer
  success_url = '/customer/customerList'

  # sale
class saleCreate(CreateView):
  model = SaleOrder
  fields = '__all__'
class saleUpdate(UpdateView):
  model = SaleOrder
  fields = ['saleDate', 'saleNote', 'confirmed','customerId']
class saleDelete(DeleteView):
  model = SaleOrder
  success_url = '/sale/saleList'

    # sale
class purchaseCreate(CreateView):
  model = PurchaseOrder
  fields = '__all__'
class purchaseUpdate(UpdateView):
  model = PurchaseOrder
  fields = ['saleDate', 'saleNote', 'confirmed','vendorId']
class purchaseDelete(DeleteView):
  model = PurchaseOrder
  success_url = '/purchase/purchaseList'