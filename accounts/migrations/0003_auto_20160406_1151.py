# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-06 11:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_student_iscandidate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candidate',
            old_name='post',
            new_name='postname',
        ),
    ]
