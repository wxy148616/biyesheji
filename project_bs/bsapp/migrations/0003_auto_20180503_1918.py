# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-03 11:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bsapp', '0002_ptwo_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pone',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pone',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='pone',
            name='gender',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='pone',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pone',
            name='qq',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ptwo',
            name='timestamp',
            field=models.CharField(default=b'2018-05-03 19:18:01', max_length=20),
        ),
    ]
