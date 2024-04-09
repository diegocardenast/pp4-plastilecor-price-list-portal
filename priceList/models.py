from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# This is the model to insert products and their prices
class ListItem (models.Model):
    productName = models.CharField(max_length=200, unique=True)
    productCode = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="list_items"
    )
    dimensions = models.CharField(max_length=200, unique=False)
    price = models.IntegerField(null=True, unique=False)
    created_on = models.DateTimeField(auto_now_add=True)
    lastModified_on = models.DateTimeField(auto_now=True)

    #this part helps to order the list in descending order by product name
    class Meta:
        ordering = ["-productName"]
    
    def __str__(self):
        return f"{self.productName} | created by {self.author}"

