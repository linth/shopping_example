# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-12-26 21:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buying', '0012_auto_20171225_1824'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderstatus',
            name='bank',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='orderstatus',
            name='facebook',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='orderstatus',
            name='last_5_digits',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='orderstatus',
            name='product',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
