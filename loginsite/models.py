# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your models here.
from django.db import models
class User(models.Model):
    gender_choice = (
        ('male', 'man'),
        ('female', 'woman'),
    )
    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256, blank=False, null=False)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=12, choices=gender_choice, default='male')
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'userinfo'
        ordering = ['-c_time']
        verbose_name = '用户'
        verbose_name_plural = '用户'
        indexes = [
            models.Index(fields=['c_time'], name='create_time'),
            models.Index(fields=['name', 'email'], name='idx_name_email'),
        ]





