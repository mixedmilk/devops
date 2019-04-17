# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import User
from django.shortcuts import render, redirect, render_to_response
from django.http import JsonResponse, Http404, HttpResponse
from django.db import models
from django import forms
from .forms import UserForm, RegisterForm
import hashlib
from captcha.models import CaptchaStore
import json
import time
def hash_code(s, salt='mysite'):  # 加点盐
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())  # update方法只接收bytes类型
    return h.hexdigest()

def captcha_image_url(key):
    return '/captchaimage/{0}/'.format(key)

def captcha_refresh(request):
    if not request.is_ajax():
        raise Http404
    new_key = CaptchaStore.generate_key()
    to_json_response = {
        'key': new_key,
        'image_url': captcha_image_url(new_key),
    }
    return HttpResponse(json.dumps(to_json_response), content_type='application/json')

    # Create your views here.
def index(request):
    # return render(request, 'base.html')
    return render(request, 'loginsite/index.html')

def logout(request):
    if not request.session.get('is_login', None):
        return redirect('/loginsite/index')
    request.session.flush()
    return redirect('/loginsite/index')

def register(request):
    if request.session.get('is_login', None):
        # 登录状态不允许注册。你可以修改这条原则！
        return redirect("/loginsite/index/")
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']
            if password1 != password2:  # 判断两次密码是否相同
                message = "两次输入的密码不同！"
                return render(request, 'login/register.html', locals())
            else:
                same_username = User.objects.filter(name=username)
                if same_username:  # 用户名唯一
                    message = '用户已经存在，请重新选择用户名！'
                    return render(request, 'loginsite/register.html', locals())
                same_email_user = User.objects.filter(email=email)
                if same_email_user:  # 邮箱地址唯一
                    message = '该邮箱地址已被注册，请使用别的邮箱！'
                    return render(request, 'login/register.html', locals())
                new_user = User.objects.create()
                new_user.name = username
                new_user.password = hash_code(password1)
                new_user.email = email
                new_user.sex = sex
                new_user.save()
                return redirect('/loginsite/login/')
    register_form = RegisterForm()
    return render(request, 'loginsite/register.html', locals())

def login(request):
    # return render(request, 'loginsite/login.html')
    # beginSession_time = time.time()
    if request.session.get('is_login', None):
        return redirect('/loginsite/index/')
        # endSession_time = time.time()
        # print endSession_time - beginSession_time
    if request.method == 'POST':
        loginForm = UserForm(request.POST)

        # username = request.POST.get('username')
        # password = request.POST.get('password')
        message = '所有字段都必须填写！'
        if loginForm.is_valid():
            username = loginForm.cleaned_data['username']
            password = loginForm.cleaned_data['password']
            remember = loginForm.cleaned_data['remember']
        # if username and password:
        #     username = username.strip()
        #     password = password.strip()
            try:
                # beginUsertime = time.time()
                user = User.objects.get(name=username)
                # endUsertime = time.time()
                # print endUsertime - beginUsertime
                if user.password == hash_code(password):
                    if remember:
                        request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    return redirect('/loginsite/index/')
                else:
                    message = 'password wrong!!'
            except:
                message = "用户名不存在！"
        else:
            message = '请输入有效的登录信息'

        return render(request, 'loginsite/login.html', locals())
    loginForm = UserForm()
    return render(request, 'loginsite/login.html', locals())


