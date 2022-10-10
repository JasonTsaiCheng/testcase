# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2022-09-26 14:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('pictures', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pictures',
            name='task',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='task', to='users.TaskTable', verbose_name='任务'),
        ),
        migrations.AddField(
            model_name='historydiseases',
            name='patient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='historyDisease', to='pictures.PatientInfo', verbose_name='患者'),
        ),
    ]