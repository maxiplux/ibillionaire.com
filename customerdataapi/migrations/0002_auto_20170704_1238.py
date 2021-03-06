# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-07-04 17:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customerdataapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApiData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('change', models.CharField(max_length=100)),
                ('change_perc', models.CharField(max_length=100)),
                ('market_cap', models.CharField(max_length=100)),
                ('volume', models.CharField(max_length=100)),
                ('last_update', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='CustomerData',
        ),
    ]
