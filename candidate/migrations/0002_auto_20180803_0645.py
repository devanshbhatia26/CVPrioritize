# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-03 06:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfilemodel',
            name='file',
            field=models.FileField(upload_to='resume/2018-08-03 06:45:53.825661+00:00.pdf'),
        ),
    ]