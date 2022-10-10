# -*- encoding=utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from pictures.models import Pictures
from django.db import models
from users.models import UserProfile


class MarkResult(models.Model):
    picture = models.ForeignKey(Pictures, verbose_name='被标注的照片', related_name="pictures", null=True,
                                blank=True)

    mark_result = models.IntegerField(verbose_name='标注结果',
                                      choices=((0, u"无"), (1, u"有")), default=0)

    mark_time = models.DateTimeField(default=datetime.now, verbose_name="标注时间")

    arbitrate_status = models.IntegerField(verbose_name='仲裁状态',
                                           choices=((0, u"未判断"), (1, u"无需仲裁"), (2, u"需仲裁")), default=0)

    arbitrate_result = models.IntegerField(verbose_name='仲裁结果',
                                           choices=((0, u"无"), (1, u"有")), default=0)

    marker = models.ForeignKey(UserProfile, verbose_name='标注者', related_name="marker", null=True,
                               blank=True)

    arbitrator = models.ForeignKey(UserProfile, verbose_name='仲裁者', related_name="arbitrator", null=True,
                                   blank=True)

    task_id = models.IntegerField(verbose_name='所属任务id', null=True, blank=True)

    class Meta:
        verbose_name = "标注结果"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.id)
