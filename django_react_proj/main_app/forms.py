from django import forms
from .models import Categories,PurchaseOrder, PurchaseOrderLine,SaleOrderLine,SaleOrder

class PurchaseOrderForm(forms.ModelForm):
    class Meta:
        model = PurchaseOrder
        fields = '__all__'

class PurchaseOrderLineForm(forms.ModelForm):
    class Meta:
        model = PurchaseOrderLine
        fields = '__all__'

class SaleOrderForm(forms.ModelForm):
    class Meta:
        model = SaleOrder
        fields = '__all__'

class SaleOrderLineForm(forms.ModelForm):
    class Meta:
        model = SaleOrderLine
        fields = '__all__'


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = ['name']
