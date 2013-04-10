#coding=utf-8
from django.contrib import admin
from items.models import Item


class ItemAdmin(admin.ModelAdmin):
    list_filter = ('name','puzi' )
    list_display = ('id','name','puzi','like_count')
    search_fields = ['name']
#    list_editable=('price','amount')

admin.site.register(Item,ItemAdmin)
