from django.contrib import admin
from .models import ListItem
from django_summernote.admin import SummernoteModelAdmin

#Adding summernote model to improve admin panel
@admin.register(ListItem)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('productName', 'productCode', 'dimensions', 'price')
    search_fields = ['productName', 'productCode']
    list_filter = ('author', 'created_on', 'dimensions')
    #prepopulated_fields = {'slug': ('productName',)}
    summernote_fields = ('productName',)

# Register your models here.
#admin.site.register(ListItem) -- NOT NEEDED IF USING summernote

