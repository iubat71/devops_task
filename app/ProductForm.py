from tkinter import Widget
from django import forms
from .models import Product, Product_refill

class ProductrefillForm(forms.ModelForm):
    class Meta:
        model=Product_refill
        fields=('e_id','product','quantity')
        widgets = {
            'e_id': forms.TextInput(
                attrs={
                    'class': 'form-control', 'placeholder':"Employee ID"
                }
            ),
            'product': forms.Select(
                attrs={
                    'class': 'form-select ','id':'product',
                }
            ),
            'quantity': forms.TextInput(
                attrs={
                    'class': 'form-control q','placeholder':"Enter the Refill Quantity"
                    ,"id":"formGroupExampleInput2 q"
                }
            )
        }
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['product'].queryset = Product.objects.none()
    
            