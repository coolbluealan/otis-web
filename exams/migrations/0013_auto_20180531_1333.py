# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-05-31 18:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0012_auto_20180531_1305'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='practiceexam',
            unique_together=set([('family', 'is_test', 'number')]),
        ),
    ]
