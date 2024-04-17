from django.contrib import admin
from .models import WelcomePage
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.




@admin.register(WelcomePage)
class WelcomeAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)