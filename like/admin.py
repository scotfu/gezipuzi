#coding=utf8
from django.contrib import admin
from like.models import Like

class LikeAdmin(admin.ModelAdmin):
    list_display=('id','item','user')

admin.site.register(Like,LikeAdmin)
