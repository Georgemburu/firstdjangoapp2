from django import forms


from .models import Product


class productCreateForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
            'active'
        ]