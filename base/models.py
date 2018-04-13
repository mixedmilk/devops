# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
    lastLoginTime = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return self.username
