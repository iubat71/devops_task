# from importlib.resources import Package

from tkinter import Widget
from django import forms
from .models import Package_refill,Package, Product

class PackagerefillForm(forms.ModelForm):
   
    class Meta:
        model=Package_refill
        fields=('e_id','package',)
      
        widgets = {
            'e_id': forms.TextInput(
                attrs={
                    'class': 'form-control', 'placeholder':"Employee ID"
                }
            ),
            'package': forms.Select( 
                attrs={
                    'class': 'form-select ','id':'packages',
                }
            ),
            'description': forms.TextInput(
                attrs={
                    'class': 'form-control ','placeholder':"This package Contains two packat of Wing"
                    ,"id":"detail "
                }
            )
        }