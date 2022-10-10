# -*- encoding=utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from datetime import datetime
from users.models import TaskTable

# from operation.models import DoctorDiagnose


class Pictures(models.Model):
    pic_name = models.CharField(max_length=120, verbose_name="图片名称")

    upload_time = models.DateTimeField(default=datetime.now, verbose_name="上传时间")

    task = models.ForeignKey(TaskTable, verbose_name='任务', related_name="task", null=True,
                             blank=True)

    class Meta:
        verbose_name = "患者眼底图片信息表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.pic_name