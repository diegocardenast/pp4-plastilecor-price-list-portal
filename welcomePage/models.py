from django.db import models

# Create your models here.

"""Welcome Page Model"""
class WelcomePage(models.Model):
    welcomeTitle = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.welcomeTitle
