# -*- coding:utf-8 -*-
__author__ = 'Jason'
__date__ = '2019/9/24 10:58'
from rest_framework import serializers

from users.models import *


# class TaskFinishStatusSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = TaskFinishStatus
#         fields = '__all__'


class TaskTableSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    markers = serializers.SerializerMethodField()

    class Meta:
        model = TaskTable
        fields = ['id', 'task_name', 'create_time', 'markers', 'task_state', ]

    def get_markers(self, row):
        marker_list = row.marker.all()
        ret = []
        for item in marker_list:
            ret.append({'last_name': item.last_name, 'first_name': item.first_name})
        return ret


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        # depth = 1
        fields = ['id', 'last_name', 'first_name']
