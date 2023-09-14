# file : django_react_proj\main_app\views.py
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.utils.decorators import method_decorator
from django.shortcuts import render,redirect, get_object_or_404
# from django.urls import reverse_lazy
# from django.views.generic.edit import FormView
from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect, JsonResponse
from .models import Categories, Product,Customer,SaleOrder,SaleOrderLine,Vendor,PurchaseOrder,PurchaseOrderLine
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import Sum, F
from .forms import PurchaseOrderForm, PurchaseOrderLineForm ,SaleOrderForm,SaleOrderLineForm
from rest_framework import serializers
from rest_framework import viewsets
from .serializers import ProductSerializer, CategoriesSerializer,CustomerSerializer,VendorSerializer,PurchaseOrderSerializer,PurchaseOrderLineSerializer,SaleOrderSerializer,SaleOrderLineSerializer

# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
class PurchaseOrderViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
class PurchaseOrderLineViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrderLine.objects.all()
    serializer_class = PurchaseOrderLineSerializer
class SaleOrderViewSet(viewsets.ModelViewSet):
    queryset = SaleOrder.objects.all()
    serializer_class = SaleOrderSerializer
class SaleOrderLineViewSet(viewsets.ModelViewSet):
    queryset = SaleOrderLine.objects.all()
    serializer_class = SaleOrderLineSerializer

from django.db import transaction

# Define the home view
def home(request):
  form = AuthenticationForm()
  total_purchased_quantity = PurchaseOrderLine.objects.aggregate(Sum('quantity'))['quantity__sum'] or 0
  total_sold_quantity = SaleOrderLine.objects.aggregate(Sum('quantity'))['quantity__sum'] or 0
  total_gross_revenue = SaleOrderLine.objects.aggregate(
    total_gross_revenue=Sum(F('quantity') * F('productId__salePrice')))['total_gross_revenue'] or 0
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html', {
        'total_purchased_quantity': total_purchased_quantity,
        'total_sold_quantity': total_sold_quantity,
        'total_gross_revenue': total_gross_revenue, 'form':form,
    })

def about(request):
  return render(request, 'about.html')


# Category View
@login_required
def category(request):
  categories = Categories.objects.all()
  for category in categories:
      total_products = Product.objects.filter(categoryId=category).count()
      category.total_products = total_products
  return render(request, 'main_app/categories/category.html',{
'categories': categories
  })

@login_required
def categories_detail(request, category_id):
    category = get_object_or_404(Categories, id=category_id)
    products = Product.objects.filter(categoryId=category)
    return render(request, 'main_app/categories/detail.html', {'category': category, 'products': products})

@method_decorator(login_required, name='dispatch')
class CategoryCreate(CreateView):
  model = Categories
  fields = ['name','image']

@method_decorator(login_required, name='dispatch')
class CategoryUpdate(UpdateView):
  model = Categories
  fields = ['name','image']
  
@method_decorator(login_required, name='dispatch')
class CategoryDelete(DeleteView):
  model = Categories
  success_url = '/categories/category'

# def product_list(request):
#     products = Product.objects.all()
#     serializer = ProductSerializer(products, many=True)
#     return JsonResponse(serializer.data, safe=False)

# product views 
@login_required
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
@login_required
def purchaseList(request):
  purchases = PurchaseOrder.objects.all()
  return render(request, 'main_app/purchase/purchaseList.html',{'purchases':purchases})

def addPurchase(request):
  return render(request, 'main_app/purchase/addPurchase.html')
def editPurchase(request):
  return render(request, 'main_app/purchase/editPurchase.html')

# sale view
@login_required
def saleList(request):
  sales = SaleOrder.objects.all()
  return render(request, 'main_app/sale/saleList.html',{'sales':sales})

def addSale(request):
  return render(request, 'main_app/sale/addSale.html')
def editSale(request):
  return render(request, 'main_app/sale/editSale.html')

# customer view
@login_required
def customerList(request):
  customers = Customer.objects.all()
  return render(request, 'main_app/customer/customerList.html',{'customers':customers})

def addCustomer(request):
  return render(request, 'main_app/customer/addCustomer.html')
def editCustomer(request):
  return render(request, 'main_app/customer/editCustomer.html')

# vendor view
@login_required
def vendorList(request):
  vendors = Vendor.objects.all()
  return render(request, 'main_app/vendor/vendorList.html', {'vendors':vendors})

def addVendor(request):
  return render(request, 'main_app/vendor/addVendor.html')
def editVendor(request):
  return render(request, 'main_app/vendor/editVendor.html')

#product
@method_decorator(login_required, name='dispatch')
class productCreate(CreateView):
  model = Product
  fields = '__all__'
@method_decorator(login_required, name='dispatch')
class productUpdate(UpdateView):
  model = Product
  fields = ['name', 'purchaseCost', 'salePrice', 'image', 'categoryId']
@method_decorator(login_required, name='dispatch')
class productDelete(DeleteView):
  model = Product
  def delete(self, request, *args, **kwargs):
      # Perform the deletion logic
      self.object = self.get_object()
      self.object.delete()

      # Return a JSON response indicating success
      return JsonResponse({"message": "Item deleted successfully", "redirect_url": self.success_url})

# vendor
@method_decorator(login_required, name='dispatch')
class vendorCreate(CreateView):
  model = Vendor
  fields = '__all__'
@method_decorator(login_required, name='dispatch')
class vendorUpdate(UpdateView):
  model = Vendor
  fields = ['name', 'phone', 'email']
@method_decorator(login_required, name='dispatch')
class vendorDelete(DeleteView):
  model = Vendor
  success_url = '/vendor/vendorList'

# customer
@method_decorator(login_required, name='dispatch')
class customerCreate(CreateView):
  model = Customer
  fields = '__all__'
@method_decorator(login_required, name='dispatch')
class customerUpdate(UpdateView):
  model = Customer
  fields = ['name', 'phone', 'email']
@method_decorator(login_required, name='dispatch')
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
@login_required
def saleForm(request, sale_id=None):
    customers = Customer.objects.all()
    products = Product.objects.all()

    # Check if sale_id is provided to determine if it's an update or add operation
    if sale_id:
        sale_instance = get_object_or_404(SaleOrder, pk=sale_id)
        title = "Update Sale"
    else:
        sale_instance = None
        title = "Add Sale"

    if request.method == 'POST':
        saleOrder_form = SaleOrderForm(request.POST, instance=sale_instance)
        saleOrderLine_form = SaleOrderLineForm(request.POST)

        if saleOrder_form.is_valid() and saleOrderLine_form.is_valid():
            # Save the SaleOrder instance (either a new one or an updated one)
            sale_order = saleOrder_form.save()

            # Get the order lines array from the request POST data
            order_lines = request.POST.getlist('orderlines[]')

            with transaction.atomic():
                for order_line_data in order_lines:
                    # Split the data to get product_id and quantity
                    product_id, quantity = order_line_data.split(',')
                    
                    # Create a new SaleOrderLine instance
                    sale_order_line = SaleOrderLine()
                    sale_order_line.saleId = sale_order
                    sale_order_line.productId = Product.objects.get(id=product_id)
                    sale_order_line.quantity = quantity
                    sale_order_line.save()

            return redirect('saleList')  # You should use the URL name
        else:
            print("Form validation failed. Errors:", saleOrder_form.errors, saleOrderLine_form.errors)
    else:
        saleOrder_form = SaleOrderForm(instance=sale_instance)
        saleOrderLine_form = SaleOrderLineForm()

    context = {
        'saleOrder_form': saleOrder_form,
        'saleOrderLine_form': saleOrderLine_form,
        'title': title,
        'customers': customers,
        'products': products,
    }

    return render(request, 'main_app/saleForm.html', context)
# 
# 
# 
# 
# 
@method_decorator(login_required, name='dispatch')
class saleUpdate(UpdateView):
  model = SaleOrder
  fields = ['saleDate', 'saleNote', 'confirmed','customerId']
@method_decorator(login_required, name='dispatch')
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
@login_required
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

@method_decorator(login_required, name='dispatch')
class purchaseUpdate(UpdateView):
  model = PurchaseOrder 
  fields = ['purchaseDate', 'purchaseNote', 'confirmed','vendorId']
@method_decorator(login_required, name='dispatch')
class purchaseDelete(DeleteView):
  model = PurchaseOrder
  success_url = '/purchase/purchaseList'

# 
# 
# 
def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # Save the user to the db
      user = form.save()
      # Automatically log in the new user
      login(request, user)
      return redirect('home')
    else:
      error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup template
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)