#coding=utf-8

from django.http import HttpResponseRedirect, Http404
from comments.models import Comment
from puzi.models import Puzi
from django.contrib.auth.decorators import login_required



@login_required
def add(request):
    path=request.path
    if request.method=='POST':
             Comment.objects.create(user=request.user,
                puzi=Puzi.objects.get(pk=request.POST['puzi']),
                title=request.POST['title'],
                content=request.POST['content'])
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
