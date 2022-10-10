# -*- coding:utf-8 -*-
__author__ = 'Jason'
__date__ = '2019/7/31 20:15'
from rest_framework import serializers

from .models import Pictures


class PicturesSerializer(serializers.ModelSerializer):
    upload_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = Pictures
        depth = 1
        fields = '__all__'

# class HistoryDiseaseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = HistoryDiseases
#         fields = "__all__"


# class PatientsSerializer(serializers.ModelSerializer):
#     # doctor = DoctorSerializer()  # doctor由原来的外键改为普通字段 所以注释
#     # apply_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
#     patient_birthday = serializers.DateTimeField(format='%Y-%m-%d')
#     # diagnose = DoctorDiagnoseSerializer(many=True)  # 外键 关联诊断表
#     # picture = PatientPictureSerializer(many=True)  # 外键  关联照片信息表
#     historyDisease = HistoryDiseaseSerializer(many=True)  # 外键  关联既往史信息表
#
#     class Meta:
#         model = PatientInfo
#         fields = "__all__"


# class TestPatientsSerializer(serializers.ModelSerializer):
#     patient_birthday = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
#
#     diagnosis = serializers.SerializerMethodField()
#
#     class Meta:
#         model = PatientInfo
#         # fields = ['pk_patient_id', 'patient_name', 'patient_birthday', 'patient_gender', 'patient_age', 'diagnosis']
#         fields = "__all__"
#
