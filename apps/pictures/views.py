# -*- coding: utf-8 -*-
from .serializers import *
# from .serializers import TestPatientsSerializer
from rest_framework.response import Response
from rest_framework import mixins
from django.db import transaction
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework import filters
from .filters import *
from django.http import HttpResponse, JsonResponse

from rest_framework.viewsets import ViewSetMixin
from django.utils import timezone
from django.db.models import Max
from .models import *
from utils.mkdir import mkdir
from django.conf import settings
import json, sys
import traceback


# Create your views here.


class PatientsPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'  # 指明向后台要多少条数据
    page_query_param = "p"  # 请求的第多少页
    max_page_size = 40


class PicturesListView(ModelViewSet):
    """
    患者列表页，分页，搜索，过滤(在filter.py中配置)，排序
    """
    queryset = Pictures.objects.all()
    serializer_class = PicturesSerializer
    # pagination_class = PatientsPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = PicturesFilter
    search_fields = ('pic_name',)
    # 上面填入的是搜素字段的名称 前端传值url: /patients/?search = 1566542
    ordering_fields = ('create_time',)  # 排序

    def create(self, request, *args, **kwargs):
        tem_patient_imgs = request.FILES.getlist('patient_img')
        task_id = request.POST['task_id']
        folder_name = 'patient_img'
        position = settings.BASE_DIR + "/media/" + folder_name
        mkdir(position)
        try:
            for f in tem_patient_imgs:
                with transaction.atomic():
                    pic_name = f.name
                    task_instance = TaskTable.objects.get(id=task_id)
                    Pictures.objects.create(pic_name=pic_name, task=task_instance)
                    with open(position + "/" + pic_name, 'wb+') as destination:
                        for chunk in f.chunks():
                            destination.write(chunk)
        except Exception as e:
            print(e)
            ex_type, ex_val, ex_stack = sys.exc_info()
            print(ex_type)  # 打印异常类型
            print(ex_val)  # 打印异常的值
            for stack in traceback.extract_tb(ex_stack):
                print(stack)  # 打印异常位置
            return HttpResponse('1')
        else:
            return HttpResponse('2')


#
#
# class TestPatientsListView(ViewSetMixin, generics.GenericAPIView):
#     queryset = PatientInfo.objects.all()
#     serializer_class = TestPatientsSerializer
#     pagination_class = PatientsPagination
#     filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
#     filter_class = PatientFilter
#     search_fields = ('patient_name', 'patient_tel', 'ID_number')
#     # 上面填入的是搜素字段的名称 前端传值url: /patients/?search = 1566542
#     ordering_fields = ('apply_time',)  # 排序
#
#     def create(self, request, *args, **kwargs):
#         try:
#             data = json.loads(request.body.decode('utf-8'))
#             a = PatientInfo.objects.create(**data)
#         except Exception as e:
#             print(e)
#             return HttpResponse(str(e))
#         else:
#             return HttpResponse(str(a))
#
#     def list(self, request, *args, **kwargs):
#         # 获取数据
#         patients = self.get_queryset()
#
#         pager_patients = self.paginate_queryset(patients)
#
#         ser = self.get_serializer(instance=pager_patients, many=True)
#
#         return Response(ser.data)
#
#     def retrieve(self, request, pk):
#         try:
#             patient = PatientInfo.objects.get(pk_patient_id=pk)
#         except PatientInfo.DoesNotExist:
#             return Response('0')
#         else:
#             serializer = PatientsSerializer(patient)
#             return Response(serializer.data)
#
#     def partial_update(self, request, *args, **kwargs):
#         print('partial_update')
#         return HttpResponse('1')
#
#     def update(self, request, *args, **kwargs):
#         print('update')
#         return HttpResponse('1')
#
#     def destroy(self, request, pk):
#         try:
#             patient = PatientInfo.objects.get(pk_patient_id=pk)
#         except PatientInfo.DoesNotExist:
#             return Response('0')
#         else:
#             patient.delete()
#             return Response('1')
