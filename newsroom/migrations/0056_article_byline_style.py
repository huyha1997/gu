# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 13:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsroom', '0055_auto_20170924_1221'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='byline_style',
            field=models.CharField(choices=[('ST', 'Standard'), ('TP', 'TextByPhotoBy')], default='ST', max_length=2),
        ),
    ]
