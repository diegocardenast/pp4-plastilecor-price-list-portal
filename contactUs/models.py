from django.db import models

# Create your models here.

"""adding contact form data model"""
class ContactUsRequest(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Contact request | {self.name}"
