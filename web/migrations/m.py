# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-11 23:44
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Planta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genero', models.CharField(max_length=100)),
                ('especie', models.CharField(max_length=100)),
                ('lugar', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
    ]