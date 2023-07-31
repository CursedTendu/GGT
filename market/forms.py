from django import forms
from .models import Product, Review

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['service_name', 'game_version', 'service_type', 'price', 'discription']

class ReviewForm(forms.ModelForm):
       class Meta:
           model = Review
           fields = ['content']