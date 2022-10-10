# -*- coding:utf-8 -*-
__author__ = 'Jason'
__date__ = '2019/9/3 10:53'

import django_filters
from .models import *


class MarkResultFilter(django_filters.rest_framework.FilterSet):
    """
    照片信息的过滤类
    """
    class Meta:
        model = MarkResult
        # 这里填入需要进行过滤的字段名称  如 'status', 但是是精确过滤
        fields = ['picture__id', 'marker', 'task_id']


# class DiagnoseConclusionFilter(django_filters.rest_framework.FilterSet):
#     """
#     诊断结论的过滤类
#     """
#     times = django_filters.CharFilter(field_name='times', lookup_expr='gte')
#
#     # diagnose_record = django_filters.CharFilter(field_name='diagnose_record',lookup_expr='gte')
#     # review_time = django_filters.CharFilter(field_name='diagnose__review_time', lookup_expr='contains')
#     # apply_time 此处可以进行模糊过滤，用contains关键字
#
#     class Meta:
#         model = DiagnoseConclusion
#         fields = ['conclusion', ]  # 这里填入需要进行过滤的字段名称  如 'status', 但是是精确过滤
#
#
# class DiagnoseDescriptionFilter(django_filters.rest_framework.FilterSet):
#     """
#     诊断结论的过滤类
#     """
#     times = django_filters.CharFilter(field_name='times', lookup_expr='gte')
#
#     # diagnose_record = django_filters.CharFilter(field_name='diagnose_record',lookup_expr='gte')
#     # review_time = django_filters.CharFilter(field_name='diagnose__review_time', lookup_expr='contains')
#     # apply_time 此处可以进行模糊过滤，用contains关键字
#
#     class Meta:
#         model = DiagnoseDescription
#         fields = ['description', ]  # 这里填入需要进行过滤的字段名称  如 'status', 但是是精确过滤
#
#
# class DoctorDiagnoseFilter(django_filters.rest_framework.FilterSet):
#     apply_time = django_filters.CharFilter(field_name='apply_time', lookup_expr='contains')
#     diagnose_time = django_filters.CharFilter(field_name='apply_time', lookup_expr='contains')
#
#     class Meta:
#         model = DoctorDiagnose
#         fields = ['pk_doctor_diagnose_id', 'status', 'check_doctor',
#                   'check_status', 'is_soft_delete', 'patient__pk_patient_id', 'hospital_area']
#
#
# class DoctorOptDiagnoseFilter(django_filters.rest_framework.FilterSet):
#     class Meta:
#         model = DoctorOptDiagnose
#         fields = ['pk_doctor_opt_diagnose_id', 'patient__pk_patient_id', 'hospital_area']
#
#
# class ReportWithdrawFilter(django_filters.rest_framework.FilterSet):
#     class Meta:
#         model = ReportWithdraw
#         fields = ['patient_name', 'solved']
#
#
# class WeChatUserFilter(django_filters.rest_framework.FilterSet):
#     class Meta:
#         model = WeChatUser
#         fields = ['openid', ]
