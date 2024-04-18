from django.contrib import admin
from .models import ContactUsRequest
from django_summernote.admin import SummernoteModelAdmin

#       If you want to customise the admin panel view in your
#       own projects, then inherit from admin.ModelAdmin like
#       we do below.

@admin.register(ContactUsRequest)
class ContactRequestAdmin(admin.ModelAdmin):

    list_display = ('name', 'message', 'email', 'read',)