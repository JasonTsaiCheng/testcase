# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2022-10-10 09:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0005_markresult_arbitrator'),
    ]

    operations = [
        migrations.AddField(
            model_name='markresult',
            name='task_id',
            field=models.IntegerField(blank=True, null=True, verbose_name='所属任务id'),
        ),
    ]