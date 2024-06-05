from django import forms
from .models import ListItem


class ProductForm(forms.ModelForm):
    """Form to create a product"""

    class Meta:
        model = ListItem
        fields = [
            "productName",
            "productCode",
            "dimensions",
            "price",
        ]

        labels = {
            "productName": "Name of the Product",
            "productCode": "Code of the Product",
            "dimensions": "Dimensions of the Product in mm (W x H x L)",
            "price": "Price of the Product in COP",
        }