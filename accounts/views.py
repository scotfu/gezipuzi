#coding=utf-8
from django.http import HttpResponseRedirect #HttpResponse Http404
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout





def loginview(request):
    if request.method == 'POST':
        form=LoginForm(request.POST)
        session_cart=getCart(request)
        try:
            next= request.POST['next']
        except:
            next='/'
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(next)
    else:
        if '_auth_user_id' in request.session:
            return HttpResponseRedirect('/')
        else:
            try:
                next= request.GET['next']
            except:
                next='/'
    return render_to_response('login.html',
            {
            'next': next},
             context_instance=RequestContext(request))



def logoutview(request):
    logout(request)
    return HttpResponseRedirect('/')



def register(request):
    if  '_auth_user_id' in request.session:
        return HttpResponseRedirect('/')
    if request.method =='POST':
        user=User.objects.create_user(
        username=request.POST['username'],
        password=request.POST['password'],
        email=request.POST['email'],
            )
        user_profile=user.get_profile()
        user_profile.nickname=form.cleaned_data['nickname']
        user_profile.save()
        return HttpResponseRedirect('/accounts/login/')
    return render_to_response('register.html',
           
            context_instance=RequestContext(request),
    )
