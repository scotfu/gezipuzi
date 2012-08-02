#coding=utf-8
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from like.models import Like
from puzi.models import Puzi
from django.contrib.auth.models import User

def plus(request,id):
    if request.method=='GET':
        try:
            puzi=Puzi.objects.get(pk=id)
        except Exception, e:
            return HttpResponse(e)
        if not Like.objects.filter(user=request.user,puzi=puzi):
            Like.objects.create(user=request.user, puzi=puzi)
            puzi.like_count+=1
            puzi.save()
            return HttpResponse('succeed')
        return HttpResponse('already voted')


