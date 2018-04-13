# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render
from ops.models import User
from django.core import serializers
# Create your views here.

def index(request):
    results = serializers.serialize('json',User.objects.all())
    return render(request,'hostMainPage.html',{'content': results})
