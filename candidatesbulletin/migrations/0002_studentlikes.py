# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-13 09:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_student_hasvoted'),
        ('candidatesbulletin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentLikes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liked', models.BooleanField(default=False)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidatesbulletin.CandidatePosts')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Student')),
            ],
            options={
                'ordering': ['student', '-updated'],
            },
        ),
    ]
