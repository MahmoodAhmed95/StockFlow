from django import forms
from .models import Categories,PurchaseOrder, PurchaseOrderLine,SaleOrderLine,SaleOrder

class PurchaseOrderForm(forms.ModelForm):
    class Meta:
        model = PurchaseOrder
        fields = '__all__'
        widgets = {
            'purchaseDate': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            }

class PurchaseOrderLineForm(forms.ModelForm):
    class Meta:
        model = PurchaseOrderLine
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Add the purchaseId field to the form and set it as a hidden field
        self.fields['purchaseId'] = forms.ModelChoiceField(
            queryset=PurchaseOrder.objects.all(),
            widget=forms.HiddenInput(),
            required=False  # Make the field not required
        )

class SaleOrderForm(forms.ModelForm):
    class Meta:
        model = SaleOrder
        fields = '__all__'

class SaleOrderLineForm(forms.ModelForm):
    class Meta:
        model = SaleOrderLine
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Add the purchaseId field to the form and set it as a hidden field
        self.fields['saleId'] = forms.ModelChoiceField(
            queryset=SaleOrder.objects.all(),
            widget=forms.HiddenInput(),
            required=False  # Make the field not required
        )


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = ['name']
