from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Categories, Product,Customer,SaleOrder,SaleOrderLine,Vendor,PurchaseOrder,PurchaseOrderLine

# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def category(request):
  categories = Categories.objects.all()
  return render(request, 'main_app/category.html',{
'categories': categories
  })

def categories_detail(request, category_id):
    category = get_object_or_404(Categories, id=category_id)
    products = Product.objects.filter(categoryId=category)
    return render(request, 'main_app/categories/detail.html', {'category': category, 'products': products})

# product views
def productList(request):
  products = Product.objects.all()
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

