#coding=utf-8
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from puzi.models import Puzi

def show(request,id):
    if request.method=='GET':
        try:
            puzi=Puzi.objects.get(pk=id)
        except:
            return Http404
        return render_to_response('puzi.html',{
               'puzi':puzi,},
               context_instance=RequestContext(request))
    else:
        return Http404

