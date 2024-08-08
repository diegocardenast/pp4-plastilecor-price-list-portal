from django.db import models
from django.contrib.auth.models import User

class ListItem (models.Model):
    """ This is the products data model"""
    productName = models.CharField(max_length=200, unique=True)
    productCode = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="list_items"
    )
    heightDimension = models.IntegerField(null=True, unique=False)
    widthDimension = models.IntegerField(null=True, unique=False)
    lengthDimension = models.IntegerField(null=True, unique=False)

    price = models.IntegerField(null=True, unique=False)
    created_on = models.DateTimeField(auto_now_add=True)
    lastModified_on = models.DateTimeField(auto_now=True)

    """ this part helps to order the list in descending order by price """
    class Meta:
        ordering = ["price"]

    def __str__(self):
        return f"{self.productName} | created by {self.author}"
