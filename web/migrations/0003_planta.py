# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-14 19:52
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_delete_planta'),
    ]

    operations = [
        migrations.CreateModel(
            name='Planta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genero', models.CharField(max_length=100)),
                ('especie', models.CharField(max_length=100)),
                ('fecha_recogida', models.DateField()),
                ('lugar', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('foto', models.ImageField(upload_to='prueba')),
                ('familia', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='web.Familia')),
            ],
        ),
    ]
