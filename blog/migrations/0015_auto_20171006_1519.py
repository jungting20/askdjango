# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-06 06:19
from __future__ import unicode_literals

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20171005_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='lnglat',
            field=models.CharField(blank=True, max_length=50, null=True, validators=[blog.models.lnglat_validator]),
        ),
    ]