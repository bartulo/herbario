# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-19 19:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import web.utils


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_planta'),
    ]

    operations = [
        migrations.CreateModel(
            name='Foto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=100)),
                ('foto', models.ImageField(upload_to=web.utils.get_upload_path)),
            ],
        ),
        migrations.RemoveField(
            model_name='planta',
            name='foto',
        ),
        migrations.AddField(
            model_name='foto',
            name='planta',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='web.Planta'),
        ),
    ]