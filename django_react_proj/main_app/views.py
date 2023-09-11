from django.shortcuts import render, get_object_or_404
from .models import Categories, Product

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
    return render(request, 'categories/detail.html', {'category': category, 'products': products})


def product(request):
  return render(request, 'main_app/product.html')

def purchase(request):
  return render(request, 'main_app/purchase.html')

def sale(request):
  return render(request, 'main_app/sale.html')

def customer(request):
  return render(request, 'main_app/customer.html')

def vendor(request):
  return render(request, 'main_app/vendor.html')


