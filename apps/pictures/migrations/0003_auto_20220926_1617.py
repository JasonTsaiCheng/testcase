# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2022-09-26 16:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pictures', '0002_auto_20220926_1427'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historydiseases',
            name='patient',
        ),
        migrations.DeleteModel(
            name='HistoryDiseases',
        ),
        migrations.DeleteModel(
            name='PatientInfo',
        ),
    ]