from django.contrib import admin
from .models import Item

class ItemAdmin(admin.ModelAdmin):
    list_display = ('id','description','done')
    list_filter = ('done',) 
    search_fields = ('description',)

admin.site.register(Item, ItemAdmin)
# Register your models here.
