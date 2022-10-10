# -*- coding:utf-8 -*-
__author__ = 'Jason'
__date__ = '2019/9/24 11:03'
import django_filters
from .models import *


class UserFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = UserProfile
        fields = ['username', 'id']  # 这里填入需要进行过滤的字段名称  如 'username', 但是是精确过滤


class TaskTableFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = TaskTable
        fields = ['id', 'marker']  # 这里填入需要进行过滤的字段名称  如 'username', 但是是精确过滤


# class TaskFinishStatusFilter(django_filters.rest_framework.FilterSet):
#     class Meta:
#         model = TaskFinishStatus
#         fields = ['task', 'marker', 'task_finish_status']  # 这里填入需要进行过滤的字段名称  如 'username', 但是是精确过滤