# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-23 11:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrgList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=40)),
                ('company_website', models.CharField(max_length=40)),
                ('company_address', models.TextField()),
            ],
        ),
    ]
