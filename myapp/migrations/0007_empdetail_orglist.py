# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-26 05:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_empdetail'),
    ]

    operations = [
        migrations.AddField(
            model_name='empdetail',
            name='orglist',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='myapp.OrgList'),
        ),
    ]
