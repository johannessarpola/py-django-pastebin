# -*- coding: utf-8 -*-
# Generated by Django 1.11a1 on 2017-02-17 16:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pastebin', '0008_userpastestats'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpastestats',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]