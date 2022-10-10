# -*- coding:utf-8 -*-
__author__ = 'Jason'
__date__ = '2019/8/2 9:43'

import django_filters
from .models import Pictures


class PicturesFilter(django_filters.rest_framework.FilterSet):
    """
    照片信息的过滤类
    """
    class Meta:
        model = Pictures
        # 这里填入需要进行过滤的字段名称  如 'status', 但是是精确过滤
        fields = ['id', 'task']





