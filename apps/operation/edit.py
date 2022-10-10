# -*- coding:utf-8 -*-
__author__ = 'Jason'
__date__ = '2019/8/26 10:03'

import json
import datetime
# from pictures.models import HistoryDiseases


def edit_basic_info(request, user_info):
    data = json.loads(request.body.decode('utf-8'))
    basic_info = data['basicInfo']
    jws_info = data['jwsInfo']
    print('jws_info', jws_info)
    print('basic_info', basic_info)
    jws_exist = basic_info['jwsExist']
    print('diagnose.......', jws_exist)
    patient_id = basic_info['patient_id']
    print(patient_id)

    if 'isFront' not in basic_info:
        print('数据是从PC端发送过来')
        del basic_info['jwsExist']
        try:
            save_to_database(patient_id, basic_info, jws_info, jws_exist)
        except Exception as e:
            print('pc端修改患者信息后保存失败', e)
            return 0
        else:
            print('pc端修改患者信息后保存成功')
            return 1

    # 以下是前端网页发送过来的数据
    if 'diagnose_again' in basic_info:
        print('前端网页数据,该患者是通过再次就诊功能添加')
        del basic_info['diagnose_again']
        del basic_info['jwsExist']
        del basic_info['isFront']
        basic_info['pic_upload'] = 0
        basic_info['upload_signal'] = 0
        basic_info['status'] = 0
        basic_info['apply_time'] = datetime.datetime.now()
        try:
            save_to_database(patient_id, basic_info, jws_info, jws_exist)
        except Exception as e:
            print('网页端修改患者信息后保存失败', e)
            return 0
        else:
            print('网页端修改患者信息后保存成功')
            return 1
    else:
        del basic_info['hospital']
        del basic_info['superior_hospital']
        del basic_info['patient_id']
        del basic_info['apply_time']
        del basic_info['picture']
        del basic_info['jwsExist']
        del basic_info['historyDisease']
        del basic_info['diagnose']
        del basic_info['isFront']
        print('basic_info', basic_info)
        try:
            save_to_database(patient_id, basic_info, jws_info, jws_exist, user_info)
        except Exception as e:
            print('网页端修改患者信息后保存失败', e)
            return 0
        else:
            print('网页端修改患者信息后保存成功')
            return 1


def edit_review_info(request):  # 修改随访患者信息（转化）
    data = json.loads(request.body.decode('utf-8'))
    print(data)
    tem_patient_id = data['patient_id']
    tem_dic1 = {'review_time': data['review_time'], 'review_hospital': data['review_hospital']}
    tem_dic2 = {'patient_tel': data['patient_tel']}
    DoctorDiagnose.objects.filter(patient_id=tem_patient_id).update(**tem_dic1)
    PatientInfo.objects.filter(patient_id=tem_patient_id).update(**tem_dic2)
    return 1


def save_to_database(patient_id, basic_info, jws_info, jws_exist, user_info):
    PatientInfo.objects.filter(patient_id=patient_id).update(**basic_info)
    jws = HistoryDiseases.objects.filter(patient_id=patient_id)
    if jws:  # 如果已经存在既往史
        if jws_exist == 0:  # 如果提交的既往史为空，则把之前的既往史删除
            HistoryDiseases.objects.filter(patient_id=patient_id).delete()
        else:  # 如果提交的既往史不为空，则更新既往史
            HistoryDiseases.objects.filter(patient_id=patient_id).update(**jws_info)
    else:  # 如果之前没有录入既往史
        if jws_exist != 0:  # 如果提交的既往史不为空，则新建一个既往史，反之则不做处理
            jws_info['patient_id'] = patient_id
            HistoryDiseases.objects.create(**jws_info)

    hospital_id = user_info.hospital_id
    s_hospital_id = user_info.superior_hospital_id
    a = PatientInfo.objects.get(patient_id=patient_id)
    if s_hospital_id == 'doctor':  # 如果该用户是上级医院，说明在上级医院录入的患者信息，则在患者信息中只加上上级医院信息
        a.superior_hospital.add(s_hospital_id)
    if hospital_id:
        # 如果该用户是下级医院，说明在下级医院录入的患者信息，则在患者信息中只加上下级和所有上级医院信息
        a.hospital.add(hospital_id)  # 加入下级
        num = SuperiorHospital.objects.filter(affiliated_hospital=hospital_id)
        for n in num:
            print(n.id)
            a.superior_hospital.add(n.id)  # 加入所有上级医院


