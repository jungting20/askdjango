# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-24 07:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20170924_1547'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='tag_set',
            new_name='tag_set_man',
        ),
    ]
