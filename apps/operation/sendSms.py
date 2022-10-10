# -*- coding:utf-8 -*-
__author__ = 'Jason'
__date__ = '2019/8/27 13:35'
import json
import re
from orbis_marker.settings import REGEX_MOBILE
from orbis_marker.settings import APIKEY
from utils.yunpian import YunPian


class SendSms(object):

    def __init__(self, request):
        self.data = request.body.decode('utf-8')

    def send_single_message(self):
        yun_pian = YunPian(APIKEY)
        data = json.loads(self.data)
        tem_patient_id = data['patient_id']
        tem_review_time = data['review_time']
        tem_review_hospital = data['review_hospital']
        tem_patient_tel = data['patient_tel']
        tem_patient_name = data['patient_name']
        tem_patient_gender = data['patient_gender']
        if re.match(REGEX_MOBILE, tem_patient_tel):
            sms_status = yun_pian.send_sms(tem_patient_name, tem_patient_gender, tem_review_time,
                                           tem_review_hospital, tem_patient_tel)
            if sms_status['code'] == 0:
                print('发送成功')
            else:
                print('发送失败,未找到匹配的模板')
        else:
            print('手机号码不合法')

        DoctorDiagnose.objects.filter(patient_id=tem_patient_id).update(inform_type='message')
        return 1

    def send_batch_message(self):
        yun_pian = YunPian(APIKEY)
        data = json.loads(self.data)
        for datum in data:
            print(datum)
            # datum = json.loads(datum)
            tem_patient_id = datum['patient_id']
            tem_review_time = datum['diagnose'][0]['review_time']
            tem_review_hospital = datum['diagnose'][0]['review_hospital']
            tem_patient_tel = datum['patient_tel']
            tem_patient_name = datum['patient_name']
            tem_patient_gender = datum['patient_gender']
            if re.match(REGEX_MOBILE, tem_patient_tel):
                sms_status = yun_pian.send_sms(tem_patient_name, tem_patient_gender, tem_review_time,
                                               tem_review_hospital,tem_patient_tel)
                if sms_status['code'] == 0:
                    print('发送成功')
                else:
                    print('发送失败,未找到匹配的模板')
            else:
                print('手机号码不合法')
            DoctorDiagnose.objects.filter(patient_id=tem_patient_id).update(inform_type='message')
        return 1


