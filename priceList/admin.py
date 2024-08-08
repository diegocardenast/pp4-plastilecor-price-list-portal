from django.contrib import admin
from .models import ListItem
from django_summernote.admin import SummernoteModelAdmin

@admin.register(ListItem)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('productName', 'productCode', 'heightDimension', 'widthDimension', 'lengthDimension', 'price')
    search_fields = ['productName', 'productCode']
    list_filter = ('author', 'created_on', 'heightDimension', 'widthDimension', 'lengthDimension')
    summernote_fields = ('productName',)

