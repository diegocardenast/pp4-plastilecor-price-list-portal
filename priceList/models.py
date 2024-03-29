from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ListItem (models.Model):
    productName = models.CharField(max_length=200, unique=True)
    productCode = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="list_items"
    )
    dimensions = models.CharField(max_length=200, unique=False)
    price = models.IntegerField(null=True, unique=False)
    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    lastModified_on = models.DateTimeField(auto_now_add=True, editable=True)

    # Source: https://stackoverflow.com/questions/4754485/dry-way-to-add-created-modified-by-and-time
    def save(self):
        if self.id:
            self.lastModified_on = datetime.now()
        else:
            self.created_on = datetime.now()
        super(MyModel,self).save()