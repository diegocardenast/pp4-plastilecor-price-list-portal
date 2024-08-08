from django import forms
from .models import ListItem


class ProductForm(forms.ModelForm):
    """Form to create a product"""

    class Meta:
        model = ListItem
        fields = [
            "productName",
            "productCode",
            "heightDimension",
            "widthDimension",
            "lengthDimension",
            "price",
        ]

        labels = {
            "productName": "Name of the Product",
            "productCode": "Code of the Product",
            "heightDimension": "Height in mm",
            "widthDimension": "Width in mm",
            "lengthDimension": "Length in mm",
            "price": "Price of the Product in COP",
        }