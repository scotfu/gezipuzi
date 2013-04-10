#coding=utf-8

from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger  
from items.models import Item
from puzi.models import Puzi

def index(request):
    try:
        items=Item.objects.all().order_by('create_time')[0:20]
    except Exception,e:
        print e
        return HttpResponse('error')
    print items
    return render_to_response('index.html',
        {'list':items},
        context_instance=RequestContext(request))

def pu(request):
    try:
        items=my_pagination(request,Item.objects.all().order_by('create_time'))
    except Exception,e:
        print e
        return HttpResponse('error')
    print items.object_list 
    return render_to_response('pu.html',
           {'list': items},
           context_instance=RequestContext(request))

    
def my_pagination(request, queryset):                                  
    display_amount=21                                                  
    after_range_num = 5
    bevor_range_num = 4                                                
    paginator = Paginator(queryset, display_amount)                    
    try:                                                               
        page =int(request.GET.get('page'))                             
    except:                                                            
        page = 1                                                       
    try:                                                               
        objects = paginator.page(page)                                 
    except EmptyPage:                                                  
        objects = paginator.page(paginator.num_pages)                  
    if page >= after_range_num:                                        
        page_range = paginator.page_range[page-after_range_num:page+bevor_range_num]                                                         
    else:                                                              
        page_range = paginator.page_range[0:page+bevor_range_num]      
    return objects
