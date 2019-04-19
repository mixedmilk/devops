# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-18 13:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginsite', '0001_initial'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='user',
            name='create_time',
        ),
        migrations.RemoveIndex(
            model_name='user',
            name='idx_name_email',
        ),
        migrations.AddIndex(
            model_name='user',
            index=models.Index(fields=['c_time'], name='userinfo_c_time_a18952_idx'),
        ),
        migrations.AddIndex(
            model_name='user',
            index=models.Index(fields=['name', 'email'], name='userinfo_name_399b88_idx'),
        ),
    ]