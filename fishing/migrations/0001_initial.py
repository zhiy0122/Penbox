# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-19 09:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fishes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IP', models.GenericIPAddressField(verbose_name='IP')),
                ('user_agent', models.CharField(max_length=128, verbose_name='UA')),
                ('refer', models.CharField(max_length=128, verbose_name='UA')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='访问时间')),
            ],
        ),
    ]
