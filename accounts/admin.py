#coding=utf-8
from django.contrib import admin
from accounts.models import UserProfile

class AccountsAdmin(admin.ModelAdmin):
    list_display=('id','user','nickname','avatar')

admin.site.register(UserProfile,AccountsAdmin)
