from django.urls import path
from . import views

urlpatterns = [
path('', views.home, name='home'),
path('about/', views.about, name='about'),
path('category/', views.category, name='category'),
path('category/<int:category_id>/', views.categories_detail, name='categories_detail'),
path('product/', views.product, name='product'),
path('purchase/', views.purchase, name='purchase'),
path('sale/', views.sale, name='sale'),
path('customer/', views.customer, name='customer'),
path('vendor/', views.vendor, name='vendor'),
]
