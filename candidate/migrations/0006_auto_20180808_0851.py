# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-08 08:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0005_auto_20180807_0820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='score',
            field=models.FloatField(),
        ),
    ]