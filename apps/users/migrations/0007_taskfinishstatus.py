# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2022-10-09 17:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20220927_1743'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskFinishStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_status', models.IntegerField(choices=[(0, '已完成'), (1, '未完成')], default=0, verbose_name='任务状态')),
                ('marker', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='markers', to=settings.AUTH_USER_MODEL, verbose_name='标注者')),
                ('task', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='users.TaskTable', verbose_name='任务')),
            ],
            options={
                'verbose_name': '任务完成情况',
                'verbose_name_plural': '任务完成情况',
            },
        ),
    ]
