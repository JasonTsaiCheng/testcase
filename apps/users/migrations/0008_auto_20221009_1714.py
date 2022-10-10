# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2022-10-09 17:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_taskfinishstatus'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskfinishstatus',
            name='task_status',
        ),
        migrations.AddField(
            model_name='taskfinishstatus',
            name='task_finish_status',
            field=models.IntegerField(choices=[(0, '未完成'), (1, '已完成')], default=0, verbose_name='任务完成状态'),
        ),
    ]