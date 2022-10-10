# -*- coding:utf-8 -*-
__author__ = 'Jason'
__date__ = '2019/7/29 15:44'

from django.views.generic.base import View

from patients.models import PatientInfo

class PatientsListView(View):
    def get(self,request):
        '''
        通过django的view实现患者列表页
        :param request:
        :return:
        '''
        json_list = []
        patients = PatientInfo.objects.all()[:10]
        for patient in patients:
            json_dict = {}
            json_dict["patient_id"] = patient.patient_id
            json_dict["patient_name"] = patient.patient_name
            json_dict["patient_gender"] = patient.patient_gender
            json_dict["patient_age"] = patient.patient_age
            json_dict["patient_tel"] = patient.patient_tel
            json_dict["patient_name"] = patient.patient_name
            json_dict["apply_time"] = '2019-07-29 19:32'
            json_dict["status"] = '未诊断'
            json_list.append(json_dict)

        from django.http import HttpResponse
        import json
        return HttpResponse(json.dumps(json_list),content_type="application/json")







