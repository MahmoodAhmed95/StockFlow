"""
URL configuration for django_react_proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from main_app import views
from rest_framework import routers
from main_app import views
from rest_framework.routers import DefaultRouter
from main_app import views
router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'categories', views.CategoriesViewSet)
router.register(r'customer', views.CustomerViewSet)
router.register(r'vendor', views.VendorViewSet)
router.register(r'purchaseorder', views.PurchaseOrderViewSet)
router.register(r'purchaseorderline', views.PurchaseOrderLineViewSet)
router.register(r'saleorder', views.SaleOrderViewSet)
router.register(r'saleorderline', views.SaleOrderLineViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    # re_path(r'^api/products/$', views.product_list),
    # re_path(r'^api/products/([0-9])$', views.main_app),
    path('', include('main_app.urls')),
    # path('api/', include(router.urls)),
]
