# -*- encoding=utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    user_role = models.IntegerField(verbose_name="角色",
                                    choices=((0, u"标注者"), (1, u"仲裁者")), default=0)

    user_gender = models.IntegerField(choices=((0, u"男"), (1, u"女")),
                                      default=0, verbose_name="性别")

    user_mobile = models.CharField(max_length=11, blank=True, verbose_name="手机号")

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}({1})'.format(self.first_name, self.last_name)


class TaskTable(models.Model):
    task_name = models.CharField(max_length=50, verbose_name='任务名称', unique=True)
    marker = models.ManyToManyField(UserProfile, related_name='picture_maker', verbose_name=u"标注者")
    create_time = models.DateTimeField(default=datetime.now, verbose_name="创建时间")
    task_state = models.IntegerField(choices=((0, u"正常"), (1, u"暂停")),
                                     default=0, verbose_name="任务状态")

    arbitrate_status = models.IntegerField(choices=((0, u"未仲裁"), (1, u"已仲裁")),
                                           default=0, verbose_name="任务仲裁状态")

    arbitrate_rules = models.IntegerField(verbose_name='仲裁规则', null=True, blank=True)

    class Meta:
        verbose_name = "任务表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.task_name

# class TaskFinishStatus(models.Model):
#     task = models.ForeignKey(TaskTable, verbose_name='任务', related_name="tasks", null=True,
#                              blank=True)
#     marker = models.ForeignKey(UserProfile, verbose_name='标注者', related_name="markers", null=True,
#                                blank=True)
#
#     task_finish_status = models.IntegerField(choices=((0, u"未完成"), (1, u"已完成")),
#                                       default=0, verbose_name="任务完成状态")
#
#     class Meta:
#         verbose_name = "任务完成情况"
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return str(self.id)
