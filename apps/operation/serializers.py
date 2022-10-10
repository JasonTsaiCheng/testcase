# -*- coding:utf-8 -*-
__author__ = 'Jason'
__date__ = '2019/8/9 15:55'
from rest_framework import serializers
from .models import *


class MarkResultSerializer(serializers.ModelSerializer):
    mark_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = MarkResult
        fields = "__all__"
        depth = 1

# class DoctorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserProfile
#         fields = "__all__"
#
#
# class UserAddSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = PatientInfo
#         fields = ("patient_id", "patient_name", "patient_gender",
#                   "patient_tel", "patient_age", "status", "address",
#                   "pic_upload", "doctor_id", "hospital_id")

#
# class DiagnoseConclusionSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = DiagnoseConclusion
#         fields = "__all__"
#
#
# class DiagnoseDescriptionSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = DiagnoseDescription
#         fields = "__all__"
#
#
# class DoctorDiagnoseSerializers(serializers.ModelSerializer):
#     picture = PatientPictureSerializer(many=True)
#     apply_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
#     check_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
#     diagnose_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M')
#
#     class Meta:
#         depth = 1
#         model = DoctorDiagnose
#         fields = "__all__"
#
#
# class DoctorOptDiagnoseSerializers(serializers.ModelSerializer):
#     apply_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
#     diagnose_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
#     positive_find_date = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
#
#     class Meta:
#         model = DoctorOptDiagnose
#         fields = '__all__'
#         depth = 1
#
#
# class ReportWithdrawSerializers(serializers.ModelSerializer):
#     withdraw_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
#
#     class Meta:
#         model = ReportWithdraw
#         depth = 1
#         fields = "__all__"
#
#
# class WeChatUserSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = WeChatUser
#         depth = 3
#         fields = "__all__"
