# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-05 03:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vuelo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('time', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('destiny', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
