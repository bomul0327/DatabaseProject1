# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-07 03:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cctv', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cctv',
            name='install_date',
            field=models.DateField(verbose_name='date installed'),
        ),
    ]
