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
path('product/create/', views.productCreate.as_view(), name='product_create'),
path('product/<int:pk>/update/', views.productUpdate.as_view(), name='product_update'),
path('product/<int:pk>/delete/', views.productDelete.as_view(), name='product_delete'),
# purchase paths
path('purchase/purchaseList/', views.purchaseList, name='purchaseList'),
path('purchase/addPurchase/', views.addPurchase, name='addPurchase'),
path('purchase/editPurchase/', views.editPurchase, name='editPurchase'),
path('purchase/create/', views.purchaseForm, name='purchaseForm'),
# path('purchase/create/', views.PurchaseCreate.as_view(), name='purchase_create'),
# path('purchase/create/', views.purchaseOrderLineCreate.as_view(), name='purchaseline_create'),
path('purchase/<int:purchase_id>/update/', views.purchaseForm, name='purchase_update'),
path('purchase/<int:pk>/delete/', views.purchaseDelete.as_view(), name='purchase_delete'),
# sale paths
path('sale/saleList/', views.saleList, name='saleList'),
path('sale/addSale/', views.addSale, name='addSale'),
path('sale/editSale/', views.editSale, name='editSale'),
# path('sale/create/', views.saleCreate.as_view(), name='sale_create'),
path('sale/create/', views.saleForm, name='addSaleForm'),
path('sale/<int:sale_id>/update/', views.saleForm, name='sale_update'),
path('sale/<int:pk>/delete/', views.saleDelete.as_view(), name='sale_delete'),
# customer paths
path('customer/customerList/', views.customerList, name='customerList'),
path('customer/addCustomer/', views.addCustomer, name='addCustomer'),
path('customer/editCustomer/', views.editCustomer, name='editCustomer'),
path('customer/create/', views.customerCreate.as_view(), name='customer_create'),
path('customer/<int:pk>/update/', views.customerUpdate.as_view(), name='customer_update'),
path('customer/<int:pk>/delete/', views.customerDelete.as_view(), name='customer_delete'),
# vendor paths
path('vendor/vendorList/', views.vendorList, name='vendorList'),
path('vendor/addVendor/', views.addVendor, name='addVendor'),
path('vendor/editVendor/', views.editVendor, name='editVendor'),
path('vendor/create/', views.vendorCreate.as_view(), name='vendor_create'),
path('vendor/<int:pk>/update/', views.vendorUpdate.as_view(), name='vendor_update'),
path('vendor/<int:pk>/delete/', views.vendorDelete.as_view(), name='vendor_delete'),
]
