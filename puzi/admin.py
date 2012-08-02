#coding=utf8
from django.contrib import admin
from puzi.models import Puzi

class PuziAdmin(admin.ModelAdmin):
   # list_filter   
    list_displat=('id','name','user')
    search_fields=('name',)

admin.site.register(Puzi,PuziAdmin)
