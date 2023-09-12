# file : django_react_proj\main_app\views.py

from django.shortcuts import render,redirect, get_object_or_404
# from django.urls import reverse_lazy
# from django.views.generic.edit import FormView
from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect
from .models import Categories, Product,Customer,SaleOrder,SaleOrderLine,Vendor,PurchaseOrder,PurchaseOrderLine
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import Sum, F
from .forms import PurchaseOrderForm, PurchaseOrderLineForm ,SaleOrderForm,SaleOrderLineForm
# Define the home view
def home(request):
  total_purchased_quantity = PurchaseOrderLine.objects.aggregate(Sum('quantity'))['quantity__sum'] or 0
  total_sold_quantity = SaleOrderLine.objects.aggregate(Sum('quantity'))['quantity__sum'] or 0
  total_gross_revenue = SaleOrderLine.objects.aggregate(
    total_gross_revenue=Sum(F('quantity') * F('productId__salePrice')))['total_gross_revenue'] or 0
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html', {
        'total_purchased_quantity': total_purchased_quantity,
        'total_sold_quantity': total_sold_quantity,
        'total_gross_revenue': total_gross_revenue,
    })

def about(request):
  return render(request, 'about.html')
# Category View
def category(request):
  categories = Categories.objects.all()
  for category in categories:
      total_products = Product.objects.filter(categoryId=category).count()
      category.total_products = total_products
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
# def saleForm(request, sale_id=None):
#     # Check if sale_id is provided to determine if it's an update or add operation
#     if sale_id:
#         sale_instance = get_object_or_404(SaleOrder, pk=sale_id)
#         title = "Update Sale"
#     else:
#         sale_instance = None
#         title = "Add Sale"

#     if request.method == 'POST':
#         saleOrder_form = SaleOrderForm(request.POST, instance=sale_instance)
#         saleOrderLine_form = SaleOrderLineForm(request.POST)

#         if saleOrder_form.is_valid() and saleOrderLine_form.is_valid():
#             # Save the SaleOrder instance (either a new one or an updated one)
#             sale_order = saleOrder_form.save()

#             # Create a new SaleOrderLine instance
#             sale_order_line = saleOrderLine_form.save(commit=False)
#             sale_order_line.sale_order = sale_order
#             sale_order_line.save()

#             return redirect('saleList')  # You should use the URL name

#     else:
#         saleOrder_form = SaleOrderForm(instance=sale_instance)
#         saleOrderLine_form = SaleOrderLineForm()

#     context = {
#         'saleOrder_form': saleOrder_form,
#         'saleOrderLine_form': saleOrderLine_form,
#         'title': title,  # Pass the title to the template for distinguishing between add and update
#     }

#     return render(request, 'main_app/saleForm.html', context)
# 
# 
# 
# 
# 
def saleForm(request, sale_id=None):
    customers = Customer.objects.all()
    products = Product.objects.all()
    # Check if purchase_id is provided to determine if it's an update or add operation
    if sale_id:
        sale_instance = get_object_or_404(SaleOrder, pk=sale_id)
        title = "Update Sale"
    else:
        sale_instance = None
        title = "Add Sale"

    if request.method == 'POST':
        saleOrder_form = SaleOrderForm(request.POST, instance=sale_instance)
        saleOrderLine_form = SaleOrderLineForm(request.POST)
        if saleOrder_form.is_valid():
            print("SaleOrder form is valid")

            # Save the PurchaseOrder instance (either a new one or an updated one)
            sale_order = saleOrder_form.save()

            if saleOrderLine_form.is_valid():
                print("SaleOrderLine form is valid")

                # Create a new PurchaseOrderLine instance without saving it yet
                sale_order_line = saleOrderLine_form.save(commit=False)
                
                # Set the purchaseId of the PurchaseOrderLine to the saved PurchaseOrder instance
                sale_order_line.saleId = sale_order
                # Save the PurchaseOrderLine
                sale_order_line.save()

                return redirect('saleList')  # You should use the URL name
            else:
                print("SaleOrderLine form is not valid. Errors:", saleOrderLine_form.errors)
        else:
            print("SaleOrder form is not valid. Errors:", saleOrder_form.errors)

    else:
        saleOrder_form = SaleOrderForm(instance=sale_instance)
        saleOrderLine_form = SaleOrderLineForm()

    context = {
        'saleOrder_form': saleOrder_form,
        'saleOrderLine_form': saleOrderLine_form,
        'title': title,  # Pass the title to the template for distinguishing between add and update
        'customers': customers,
        'products': products,

    }

    return render(request, 'main_app/saleForm.html', context)
# 
# 
# 
# 
# 
class saleUpdate(UpdateView):
  model = SaleOrder
  fields = ['saleDate', 'saleNote', 'confirmed','customerId']
class saleDelete(DeleteView):
  model = SaleOrder
  success_url = '/sale/saleList'

    # sale
# class PurchaseCreate(CreateView):
#   model = PurchaseOrderLine
#   fields = '__all__'
# def purchaseForm(request):
  
#   if request.method == 'POST':

#     PurchaseOrder_form = PurchaseOrderForm(request.POST)
#     PurchaseOrderLine_form = PurchaseOrderLineForm(request.POST)

#     if PurchaseOrder_form.is_valid() and PurchaseOrderLine_form.is_valid():

#         PurchaseOrder_form.save()
#         PurchaseOrderLine_form.save()
#         return HttpResponseRedirect('/purchase/purchaseList')        

#     else:
#         context = {
#             'PurchaseOrder_form': PurchaseOrder_form,
#             'PurchaseOrderLine_form': PurchaseOrderLine_form,
#         }

#   else:
#     context = {
#         'PurchaseOrder_form': PurchaseOrderForm(),
#         'PurchaseOrderLine_form': PurchaseOrderLineForm(),
#     }
#   return TemplateResponse(request, 'main_app/purchaseForm.html', context)

# def purchaseForm(request, purchase_id=None):
#     # Check if sale_id is provided to determine if it's an update or add operation
#     if purchase_id:
#         purchase_instance = get_object_or_404(PurchaseOrder, pk=purchase_id)
#         title = "Update Purchase"
#     else:
#         purchase_instance = None
#         title = "Add Purchase"

#     if request.method == 'POST':
#         purchaseOrder_form = PurchaseOrderForm(request.POST, instance=purchase_instance)
#         purchaseOrderLine_form = PurchaseOrderLineForm(request.POST)

#         if purchaseOrder_form.is_valid() and purchaseOrderLine_form.is_valid():
#             # Save the SaleOrder instance (either a new one or an updated one)
#             purchase_order = purchaseOrder_form.save()

#             # Create a new SaleOrderLine instance
#             purchase_order_line = purchaseOrderLine_form.save(commit=False)
#             purchase_order_line.purchase_order = purchase_order
#             purchase_order_line.save()

#             return redirect('purchaseList')  # You should use the URL name

#     else:
#         purchaseOrder_form = PurchaseOrderForm(instance=purchase_instance)
#         purchaseOrderLine_form = PurchaseOrderLineForm()

#     context = {
#         'purchaseOrder_form': purchaseOrder_form,
#         'purchaseOrderLine_form': purchaseOrderLine_form,
#         'title': title,  # Pass the title to the template for distinguishing between add and update
#     }

#     return render(request, 'main_app/purchaseForm.html', context)

def purchaseForm(request, purchase_id=None):
    vendors = Vendor.objects.all()
    products = Product.objects.all()
    # Check if purchase_id is provided to determine if it's an update or add operation
    if purchase_id:
        purchase_instance = get_object_or_404(PurchaseOrder, pk=purchase_id)
        title = "Update Purchase"
    else:
        purchase_instance = None
        title = "Add Purchase"

    if request.method == 'POST':
        purchaseOrder_form = PurchaseOrderForm(request.POST, instance=purchase_instance)
        purchaseOrderLine_form = PurchaseOrderLineForm(request.POST)
        if purchaseOrder_form.is_valid():
            print("PurchaseOrder form is valid")

            # Save the PurchaseOrder instance (either a new one or an updated one)
            purchase_order = purchaseOrder_form.save()

            if purchaseOrderLine_form.is_valid():
                print("PurchaseOrderLine form is valid")

                # Create a new PurchaseOrderLine instance without saving it yet
                purchase_order_line = purchaseOrderLine_form.save(commit=False)
                
                # Set the purchaseId of the PurchaseOrderLine to the saved PurchaseOrder instance
                purchase_order_line.purchaseId = purchase_order
                # Save the PurchaseOrderLine
                purchase_order_line.save()

                return redirect('purchaseList')  # You should use the URL name
            else:
                print("PurchaseOrderLine form is not valid. Errors:", purchaseOrderLine_form.errors)
        else:
            print("PurchaseOrder form is not valid. Errors:", purchaseOrder_form.errors)

    else:
        purchaseOrder_form = PurchaseOrderForm(instance=purchase_instance)
        purchaseOrderLine_form = PurchaseOrderLineForm()

    context = {
        'purchaseOrder_form': purchaseOrder_form,
        'purchaseOrderLine_form': purchaseOrderLine_form,
        'title': title,  # Pass the title to the template for distinguishing between add and update
        'vendors': vendors,
        'products': products,
    }

    return render(request, 'main_app/purchaseForm.html', context)


class purchaseUpdate(UpdateView):
  model = PurchaseOrder 
  fields = ['purchaseDate', 'purchaseNote', 'confirmed','vendorId']
class purchaseDelete(DeleteView):
  model = PurchaseOrder
  success_url = '/purchase/purchaseList'