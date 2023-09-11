from django.urls import path
from . import views

urlpatterns = [
path('', views.home, name='home'),
path('about/', views.about, name='about'),
#category Paths
path('categories/category/', views.category, name='category'),
path('category/<int:category_id>/', views.categories_detail, name='categories_detail'),
path('categories/create/', views.CategoryCreate.as_view(), name='categories_create'),
path('categories/<int:pk>/update/', views.CategoryUpdate.as_view(), name='categories_update'),
path('categories/<int:pk>/delete/', views.CategoryDelete.as_view(), name='categories_delete'),

# path('category/<int:category_id>/delete/', views.delete_category, name='delete_category'),
# product paths
path('product/productList/', views.productList, name='productList'),
path('product/addProduct/', views.addProduct, name='addProduct'),
path('product/editProduct/', views.editProduct, name='editProduct'),
# purchase paths
path('purchase/purchaseList/', views.purchaseList, name='purchaseList'),
path('purchase/addPurchase/', views.addPurchase, name='addPurchase'),
path('purchase/editPurchase/', views.editPurchase, name='editPurchase'),
# sale paths
path('sale/saleList/', views.saleList, name='saleList'),
path('sale/addSale/', views.addSale, name='addSale'),
path('sale/editSale/', views.editSale, name='editSale'),
# customer paths
path('customer/customerList/', views.customerList, name='customerList'),
path('customer/addCustomer/', views.addCustomer, name='addCustomer'),
path('customer/editCustomer/', views.editCustomer, name='editCustomer'),
# vendor paths
path('vendor/vendorList/', views.vendorList, name='vendorList'),
path('vendor/addVendor/', views.addVendor, name='addVendor'),
path('vendor/editVendor/', views.editVendor, name='editVendor'),
]
