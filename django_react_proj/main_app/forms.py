from django import forms
from .models import Categories,PurchaseOrder, PurchaseOrderLine

class PurchaseOrderForm(forms.ModelForm):
    class Meta:
        model = PurchaseOrder
        fields = '__all__'

class PurchaseOrderLineForm(forms.ModelForm):
    class Meta:
        model = PurchaseOrderLine
        fields = '__all__'

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = ['name']
