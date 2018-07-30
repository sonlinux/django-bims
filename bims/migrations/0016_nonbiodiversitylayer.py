# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-17 06:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bims', '0015_merge_20180706_0539'),
    ]

    operations = [
        migrations.CreateModel(
            name='NonBiodiversityLayer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('wms_url', models.CharField(max_length=256)),
                ('wms_layer_name', models.CharField(max_length=128)),
                ('wms_format', models.CharField(default=b'image/png', max_length=64)),
            ],
        ),
    ]
