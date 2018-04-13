# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse,HttpResponseRedirect

from django.shortcuts import render,render_to_response
#from ops.models import User
from django.core import serializers
from django import forms
from models import User
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as base_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
# Create your views here.
class UserForm(forms.Form):
    username = forms.CharField(label='用户名')
    password = forms.CharField(label='密   码',widget=forms.PasswordInput())
    #last_login = forms.DateTimeField()

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print username,password
        user = authenticate(username=username, password=password)
        if user is not None:
            base_login(request, user)
            return render(request, "welcome.html", {'msg': 'welcome'})
        else:
            print "no.."
    #     user = User.objects.all().filter(username=username)
    #         if user:
    #             passwd = User.objects.all().filter(username=username,password=password)
    #             if passwd:
    #                 loginState = True
    #             else:
    #                 loginState = False
    #                 msg = "password wrong"
    #         else:
    #             msg = "user does't exist!"
    #             return HttpResponse(msg)
    #         if loginState:
    #             return HttpResponseRedirect("/base/welcome/")
    #         else:
    #             return HttpResponse(msg)
    else:
        return render(request,"login.html")
        #return HttpResponse("Unknown option")

def logout_view(request):
    logout(request)
    return render(request,"login.html")

def ensure_login(request):
    if not request.user.is_authenticated:
        return render(request,"login.html")

@login_required(login_url='/base/login/')
def welcome(request):
    return render(request,"welcome.html",{'msg':'welcome'})
