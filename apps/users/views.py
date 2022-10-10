# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from .serializers import *

from .filters import *

from rest_framework import generics

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .filters import UserFilter
from .models import *
from rest_framework.viewsets import ModelViewSet
from django.http import HttpResponse
import json, sys
import traceback
from rest_framework.pagination import PageNumberPagination
from django.db import transaction


class PatientsPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'  # 指明向后台要多少条数据
    page_query_param = "p"  # 请求的第多少页
    max_page_size = 40


class UserListView(ModelViewSet):
    """
    诊断结论，分页，搜索，过滤(在filter.py中配置)，排序
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = UserFilter

    def update(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            user_id = data['id']
            UserProfile.objects.filter(id=user_id).update(**data)
        except Exception as e:
            print(e)
            return HttpResponse('0')
        return HttpResponse('1')


class TaskTableListView(ModelViewSet):
    """
    诊断结论，分页，搜索，过滤(在filter.py中配置)，排序
    """
    queryset = TaskTable.objects.all().order_by('-create_time')
    serializer_class = TaskTableSerializer
    pagination_class = PatientsPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = TaskTableFilter

    def create(self, request, *args, **kwargs):
        data = json.loads(request.body)
        task_name = data['task_name']
        user_id_list = data['id_list']
        try:
            with transaction.atomic():
                a = TaskTable.objects.create(task_name=task_name)
                for user_id in user_id_list:
                    a.marker.add(user_id)
        except Exception as e:
            print(e)
            ex_type, ex_val, ex_stack = sys.exc_info()
            print(ex_type)  # 打印异常类型
            print(ex_val)  # 打印异常的值
            for stack in traceback.extract_tb(ex_stack):
                print(stack)  # 打印异常位置
            return HttpResponse('0')

        return HttpResponse('1')

    def update(self, request, *args, **kwargs):
        data = json.loads(request.body)
        print(data)
        task_id = data['task_id']
        task_state = data['task_state']
        try:
            TaskTable.objects.filter(id=task_id).update(task_state=task_state)
        except Exception as e:
            print(e)
            return HttpResponse('0')
        return HttpResponse('1')

    def destroy(self, request, *args, **kwargs):
        data = json.loads(request.body)
        task_id = data['task_id']
        try:
            TaskTable.objects.filter(id=task_id).delete()
        except Exception as e:
            print(e)
            return HttpResponse('0')
        return HttpResponse('1')


class PictureLabelResult(ModelViewSet):
    """
    诊断结论，分页，搜索，过滤(在filter.py中配置)，排序
    """
    queryset = TaskTable.objects.all().order_by('-create_time')
    serializer_class = TaskTableSerializer
    pagination_class = PatientsPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = TaskTableFilter

    def create(self, request, *args, **kwargs):
        print(json.loads(request.body))
        return HttpResponse('1')

# class TaskFinishStatusListView(ModelViewSet):
#     """
#     诊断结论，分页，搜索，过滤(在filter.py中配置)，排序
#     """
#     queryset = TaskFinishStatus.objects.all()
#     serializer_class = TaskFinishStatusSerializer
#     pagination_class = PatientsPagination
#     filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
#     filter_class = TaskFinishStatusFilter
