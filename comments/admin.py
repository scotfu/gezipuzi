#coding=utf8
from django.contrib import admin
from comments.models import Comment
from django.contrib.auth.models import User


class CommentAdmin(admin.ModelAdmin):
    list_display=('id','title','content','user','item')
    search_fields=('title','user','item')

admin.site.register(Comment,CommentAdmin)
