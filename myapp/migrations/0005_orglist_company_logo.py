# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-25 09:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20170425_1229'),
    ]

    operations = [
        migrations.AddField(
            model_name='orglist',
            name='company_logo',
            field=models.FileField(blank='True', null='True', upload_to=''),
        ),
    ]