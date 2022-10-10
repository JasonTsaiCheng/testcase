# -*- coding:utf-8 -*-
__author__ = 'Jason'
__date__ = '2019/8/26 11:25'
import json
import requests


class YunPian(object):

    def __init__(self, api_key):
        self.api_key = api_key
        self.single_send_url = 'https://sms.yunpian.com/v2/sms/single_send.json'

    def send_sms(self, patient_name, patient_gender, review_time, review_hospital, mobile):
        params = {
            'apikey': self.api_key,
            'mobile': mobile,
            'text': "【蔡成】尊敬的{patient_name}{patient_gender},请于{review_time}前,前往{review_hospital}进行眼底复查。"
                    "如已收到请忽略"
                    .format(patient_name=patient_name, patient_gender=patient_gender,
                            review_time=review_time, review_hospital=review_hospital)
             }
        response = requests.post(self.single_send_url, data=params)
        re_dict = json.loads(response.text)
        return re_dict


if __name__ == '__main__':
    yun_pian = YunPian('7e65d14ad635b9a04affaa049f507732')
    yun_pian.send_sms('Jason', '0', '2020-08-17', '天乐社区', '15665422662')


