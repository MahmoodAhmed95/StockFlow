from django.shortcuts import render


# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def category(request):
  return render(request, 'main_app/category.html')

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


