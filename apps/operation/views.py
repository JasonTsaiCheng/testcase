# -*- coding: utf-8 -*-
from django.conf import settings
import random
import string
import urllib
from rest_framework import viewsets
from rest_framework import mixins
from django.http import HttpResponse, JsonResponse
from django.db.models import Q, F
from django.db import transaction
from django.core import serializers
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url
from django.shortcuts import render
from django.views.generic import View
# from django.shortcuts import render,redirect
from rest_framework import generics
from operation import edit
from django.core.cache import cache
import traceback
import json, re, os, sys
# import xml.etree.ElementTree as ET
# import io
import base64
import shutil
# import math
# import time
# from django.conf import settings
import datetime
from utils.mkdir import mkdir
from operation.sendSms import SendSms
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
from rest_framework.response import Response
from .filters import *
from rest_framework_jwt.utils import jwt_decode_handler
# from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
# from django.core.mail import EmailMultiAlternatives,get_connection
# from django.http import HttpResponse, Http404, FileResponse

# from .models import DiagnoseConclusion, PatientPicture, DiagnoseDescription
# from operation.models import DoctorDiagnose, ReportWithdraw, DoctorOptDiagnose, WeChatUser
# from users.models import UserProfile, Hospital
from django.core.paginator import Paginator, EmptyPage, InvalidPage, PageNotAnInteger
# from pictures.models import HistoryDiseases, PatientInfo

from .serializers import *

# from django.forms.models import model_to_dict
# from utils.pdfgen import create_pdf, create_pdf2, retention_tag
# from utils.mkdir import mkdir
# #from utils.interface import AI_process
# from utils import imgProcess, check_md5, get_IP
# from utils.AIprocess import img_iqa, dr_detect, dr_detect_outside
# from utils.AIprocess import picture_strengthen as fog_removal
# from utils.img_strengthen import strengthen
from utils.forms import RegisterForm, ResetPwdForm
# from utils.createImgs import produce_img
from rest_framework.authentication import BaseAuthentication
import smtplib
# from utils.pdfgen import PdfMaker
from email.mime.text import MIMEText
from email.header import Header
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from django.db.models.aggregates import Count, Max
from django.db import connection
from .models import *


class PatientsPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'  # 指明向后台要多少条数据
    page_query_param = "p"  # 请求的第多少页
    max_page_size = 40


class MarkResultListView(ModelViewSet):
    """
    患者列表页，分页，搜索，过滤(在filter.py中配置)，排序

    """
    queryset = MarkResult.objects.all()
    serializer_class = MarkResultSerializer
    pagination_class = PatientsPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = MarkResultFilter
    search_fields = ('pic_name',)
    # 上面填入的是搜素字段的名称 前端传值url: /patients/?search = 1566542
    ordering_fields = ('id',)  # 排序

    def create(self, request, *args, **kwargs):
        data = json.loads(request.body)
        user_id = data['user_id']
        label_result = data['label_result']
        task_id = data['task_id']
        bulk_list = []
        try:
            marker_instance = UserProfile.objects.get(id=user_id)
            for key, value in label_result.items():
                picture_instance = Pictures.objects.get(id=key)
                bulk_list.append(MarkResult(marker=marker_instance,
                                            mark_result=value,
                                            picture=picture_instance,
                                            task_id=task_id))
            MarkResult.objects.bulk_create(bulk_list)

        except Exception as e:
            print(e)
            return HttpResponse('0')
        else:
            return HttpResponse('1')




class EmailClass(object):
    def __int__(self, email, username, url):
        self.email = email  # 用户邮箱地址
        self.username = username  # 用户名字
        self.url = url  # 远程系统的地址 要拼接

        # 第三方 SMTP 服务
        self.mail_host = "smtp.mxhichina.com"  # 设置服务器
        self.mail_user = "support@orbisbiotech.com"  # 用户名
        self.mail_pass = "Orbis888"  # 口令
        self.sender = 'support@orbisbiotech.com'

    def send_email(self):
        receivers = [self.email]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
        tem_secret_name = base64.b64encode(bytes(self.username, 'utf-8'))
        secret_name = bytes.decode(tem_secret_name)
        mail_msg = """
        <p>密码修改请点击以下链接</p>
        <p><a href=""" + self.url + """logoutOperation/modifyPwd?sid=""" + secret_name + """>修改奥比斯远程医疗系统密码</a></p>
        <p>您的用户名:""" + self.username + """</p>
        <p>奥比斯科技竭诚为您服务</p>
        """
        print(mail_msg)
        message = MIMEText(mail_msg, 'html', 'utf-8')
        message['From'] = Header("support@orbisbiotech.com", 'utf-8')
        message['To'] = Header(self.email, 'utf-8')

        subject = '密码重置'
        message['Subject'] = Header(subject, 'utf-8')

        print('开始发送邮件')
        smtpObj = smtplib.SMTP_SSL(timeout=2)
        smtpObj.connect(self.mail_host, 465)  # 465 为 SMTP 端口号
        smtpObj.login(self.mail_user, self.mail_pass)
        smtpObj.sendmail(self.sender, receivers, message.as_string())
        smtpObj.quit()
        print("邮件发送成功")


class UserRegisterView(View):
    def post(self, request):
        back_form = dict()
        try:
            data = json.loads(request.body.decode('utf-8'))
            form = RegisterForm(data)
            email = data['email']

            user = UserProfile.objects.filter(email=email)
            if user:
                back_form['code'] = 0
                back_form['msg'] = '该邮箱已经被注册'
                return HttpResponse(json.dumps(back_form, ensure_ascii=False))
            if form.is_valid():
                form.save()
                user = UserProfile.objects.filter(email=email)[0]
                user.is_active = 1  # 新注册的用户默认激活
                user.save()
                back_form['code'] = 1
                back_form['msg'] = '注册成功, 请联系管理员激活账号'
            else:
                for filed in form:
                    result_form = str(filed.errors)
                    if 'error' not in result_form:
                        continue
                    res1 = ''.join(re.findall('[\u4e00-\u9fa5]', result_form))
                    back_form['code'] = 0
                    back_form['msg'] = res1
            return HttpResponse(json.dumps(back_form, ensure_ascii=False))
        except Exception as e:
            ex_type, ex_val, ex_stack = sys.exc_info()
            print(ex_type)  # 打印异常类型
            print(ex_val)  # 打印异常的值
            for stack in traceback.extract_tb(ex_stack):
                print(stack)  # 打印异常位置
            back_form['code'] = 0
            back_form['msg'] = str(e)
            return HttpResponse(json.dumps(back_form, ensure_ascii=False))


class PasswordView(View):
    def __int__(self):
        pass

    def get(self, request):

        data = request.GET
        print('qqqwweerr', data)
        return HttpResponse('2')
        email_address = data['email']
        url = data['url']
        result = UserProfile.objects.filter(email=email_address)
        if not result:
            return HttpResponse('0')
        try:
            username = result[0].username

            emails = EmailClass(email_address, username, url)

            emails.send_email()

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

    def post(self, request, *args, **kwargs):
        data = request.POST
        back_form = dict()
        print(data)
        if 'username' not in data:
            back_form['code'] = '0'
            back_form['info'] = '该用户不存在,请从邮箱打开该链接'
            return HttpResponse(json.dumps(back_form, ensure_ascii=False))
        tem_secret_name = data['username']
        missing_padding = 4 - len(tem_secret_name) % 4
        if missing_padding:
            tem_secret_name += '=' * missing_padding
        secret_name = tem_secret_name.encode('utf-8')
        tem_username = base64.decodestring(secret_name)
        username = bytes.decode(tem_username)
        user = UserProfile.objects.filter(username=username)
        if not user:
            back_form['code'] = '0'
            back_form['msg'] = '该用户不存在,请从邮箱打开该链接'
            return HttpResponse(json.dumps(back_form, ensure_ascii=False))
        del data['username']
        data['password'] = data['password1']
        form = ResetPwdForm(data)
        if form.is_valid():
            print()
            user[0].set_password(data['password'])
            user[0].save()
            back_form['code'] = '1'
            back_form['msg'] = '验证成功，用户名%s' % username
            return HttpResponse(json.dumps(back_form, ensure_ascii=False))
        else:
            for filed in form:
                result_form = str(filed.errors)
                if 'error' not in result_form:
                    continue
                res1 = ''.join(re.findall('[\u4e00-\u9fa5]', result_form))
                back_form['code'] = '0'
                back_form['msg'] = res1
            return HttpResponse(json.dumps(back_form, ensure_ascii=False))


# 图形验证码功能
class CaptchaView(View):
    def judge_captcha(self, captchaStr, captchaHashkey):
        if captchaStr and captchaHashkey:
            try:
                # 获取根据hashkey获取数据库中的response值
                get_captcha = CaptchaStore.objects.get(hashkey=captchaHashkey)
                print(get_captcha.response)
                if get_captcha.response == captchaStr.lower():  # 如果验证码匹配
                    return True
            except Exception as e:
                print('错误', e)
                return False
        else:
            return False

    def get(self, request):
        hash_key = CaptchaStore.generate_key()  # 验证码答案
        image_url = captcha_image_url(hash_key)  # 验证码地址
        captcha = {'hash_key': hash_key, 'image_url': image_url}
        print(captcha)
        return JsonResponse(captcha, safe=False)

    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        if data:
            answer = data["answer"]  # 用户提交的验证码
            hash_key = data["hash_key"]  # 验证码答案
            if self.judge_captcha(answer, hash_key):
                return HttpResponse("1")
            else:
                return HttpResponse("0")
        else:
            return HttpResponse("0")


def user_operation(request, order):
    if order == 'forgetPwd':  # 忘记密码发送邮件
        data = json.loads(request.body.decode('utf-8'))
        email = data['email']
        url = data['url']
        print(data)
        result = UserProfile.objects.filter(email=email)
        if not result:
            return HttpResponse('0')
        try:
            username = result[0].username
            send_email(email, username, url)
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

    if order == 'config':
        try:
            data = json.loads(request.body.decode('utf-8'))
            # user_id = data['user_id']
            # account_type = data['account_type']
            # if account_type == '1':
            #     data['superior_hospital'] = '6'
            # del data['user_id']
            # UserProfile.objects.filter(id=user_id).update(**data)
            print(data)
            return HttpResponse('1')
        except Exception as e:
            ex_type, ex_val, ex_stack = sys.exc_info()
            print(ex_type)  # 打印异常类型
            print(ex_val)  # 打印异常的值
            for stack in traceback.extract_tb(ex_stack):
                print(stack)  # 打印异常位置
            return HttpResponse("0")

    if order == 'web_upload_picture':  # 网页上传照片
        tem_patient_imgs = request.FILES.getlist('patient_img')
        task_id = request.POST['task_id']
        folder_name = 'patient_img'
        position = settings.BASE_DIR + "/media/" + folder_name
        mkdir(position)
        try:

            for f in tem_patient_imgs:
                pic_name = f.name
                a = Pictures.objects.create(pic_name=pic_name)
                a.task.add(task_id)
                with open(position + "/" + pic_name, 'wb+') as destination:
                    for chunk in f.chunks():
                        destination.write(chunk)
        except Exception as e:
            print(e)
            return HttpResponse('1')
        else:
            return HttpResponse('2')

    if order == 'clickDiagnoseButton':  # 防止两个医生同时诊断一个患者
        data = json.loads(request.body.decode('utf-8'))
        pk_doctor_diagnose_id = ''
        pk_doctor_opt_diagnose_id = ''
        if 'pk_doctor_diagnose_id' in data:
            pk_doctor_diagnose_id = data['pk_doctor_diagnose_id']
            patient_info = DoctorDiagnose.objects.filter(pk_doctor_diagnose_id=pk_doctor_diagnose_id)
        else:
            pk_doctor_opt_diagnose_id = data['pk_doctor_opt_diagnose_id']
            patient_info = DoctorOptDiagnose.objects.filter(pk_doctor_opt_diagnose_id=pk_doctor_opt_diagnose_id)
        doctor = str(data['click_doctor'])
        click_time = patient_info[0].doctor_click_time
        click_doctor = patient_info[0].click_doctor
        if click_doctor:
            click_doctor = str(patient_info[0].click_doctor.id)
        status = patient_info[0].status

        if status == '2':
            # 该名患者已经被诊断
            return HttpResponse('2')
        if click_time:  # 如果有点击时间，说明此患者有可能在被诊断
            if click_doctor == doctor:  # 如果此次点击的医生和上次点击的医生是同一个人，则可以无限制点击
                tem_dic = {}
                click_time = datetime.datetime.now()
                user_instance = UserProfile.objects.get(id=doctor)
                tem_dic['doctor_click_time'] = click_time
                tem_dic['click_doctor'] = user_instance
                if pk_doctor_diagnose_id:
                    DoctorDiagnose.objects.filter(pk_doctor_diagnose_id=pk_doctor_diagnose_id).update(**tem_dic)
                else:
                    DoctorOptDiagnose.objects.filter(pk_doctor_opt_diagnose_id=pk_doctor_opt_diagnose_id).update(
                        **tem_dic)
                return HttpResponse('1')
            else:  # 如果此次点击的医生和上次点击的医生不是同一个人，则进行以下判断
                expire_time = click_time + datetime.timedelta(minutes=5)
                if expire_time > datetime.datetime.now():  # 如果诊断保护时间未到，则提示正在被诊断
                    return HttpResponse('0')
                else:  # 如果诊断保护时间已到，
                    # 则更新诊断保护click_time和click_doctor，并让其诊断
                    print('diagnose time is expired')
                    tem_dic = {}
                    click_time = datetime.datetime.now()
                    user_instance = UserProfile.objects.get(id=doctor)
                    tem_dic['doctor_click_time'] = click_time
                    tem_dic['click_doctor'] = user_instance

                    if pk_doctor_diagnose_id:
                        DoctorDiagnose.objects.filter(pk_doctor_diagnose_id=pk_doctor_diagnose_id).update(**tem_dic)
                    else:
                        DoctorOptDiagnose.objects.filter(pk_doctor_opt_diagnose_id=pk_doctor_opt_diagnose_id).update(
                            **tem_dic)
                    return HttpResponse('1')
        else:  # 如果没有点击时间，说明该患者是第一次被诊断，则让其诊断，并录入click_time和click_doctor
            tem_dic = {}
            click_time = datetime.datetime.now()
            user_instance = UserProfile.objects.get(id=doctor)
            tem_dic['doctor_click_time'] = click_time
            tem_dic['click_doctor'] = user_instance
            if pk_doctor_diagnose_id:
                DoctorDiagnose.objects.filter(pk_doctor_diagnose_id=pk_doctor_diagnose_id).update(**tem_dic)
            else:
                DoctorOptDiagnose.objects.filter(pk_doctor_opt_diagnose_id=pk_doctor_opt_diagnose_id).update(**tem_dic)
            return HttpResponse('1')

    if order == 'leaveWithoutDiagnose':  # 用户在离开诊断界面时需要将click_time和click_doctor清除
        data = json.loads(request.body.decode('utf-8'))
        try:
            if 'pk_doctor_diagnose_id' in data:
                pk_doctor_diagnose_id = data['pk_doctor_diagnose_id']
                DoctorDiagnose.objects.filter \
                    (pk_doctor_diagnose_id=pk_doctor_diagnose_id).update(click_doctor=None, doctor_click_time=None)
                return HttpResponse('1')
            else:
                pk_doctor_opt_diagnose_id = data['pk_doctor_opt_diagnose_id']
                DoctorOptDiagnose.objects.filter \
                    (pk_doctor_opt_diagnose_id=pk_doctor_opt_diagnose_id).update(click_doctor=None,
                                                                                 doctor_click_time=None)
        except Exception as e:
            print(e)
            return HttpResponse('0')
        else:
            return HttpResponse('1')

    if order == 'createPdf':
        data = json.loads(request.body.decode('utf-8'))
        report_module = 'module3'
        folder_name = 'general'

        data['other_data']['report_module'] = report_module

        print(data)

        try:
            data = {**data['basic_data'], **data['other_data']}

            # if 'diagnose_id' in data:
            # tem_pdf_name = DoctorDiagnose.objects.filter(id=data['diagnose_id'])[0].pdf_name
            # if tem_pdf_name:
            #     return HttpResponse(tem_pdf_name)

            left_eye_pic_name = data['left_origin_src'].split('/')[2]
            right_eye_pic_name = data['right_origin_src'].split('/')[2]

            '''
            如果医生上传的全部是左眼或者右眼的照片
            '''
            if 'Left' in left_eye_pic_name and 'Left' in right_eye_pic_name:
                right_pic_name = data['left_origin_src'].replace('Left', 'Right')
                right_copy_pic = settings.BASE_DIR + '/media' + right_pic_name
                old_pic_name = settings.BASE_DIR + '/media' + data['left_origin_src']
                shutil.copyfile(old_pic_name, right_copy_pic)
                tem_dic = dict()
                tem_dic['patient_id'] = data['patient_id']
                tem_dic['selected'] = '1'
                tem_dic['pic_name'] = right_pic_name.split('/')[2]
                tem_dic['own_to'] = data['diagnose_record']
                PatientPicture.objects.filter(pic_name=right_eye_pic_name).update(selected=1)
                PatientPicture.objects.create(**tem_dic)
            elif 'Right' in left_eye_pic_name and 'Right' in right_eye_pic_name:
                left_pic_name = data['right_origin_src'].replace('Right', 'Left')
                left_copy_pic = settings.BASE_DIR + '/media' + left_pic_name
                old_pic_name = settings.BASE_DIR + '/media' + data['right_origin_src']
                shutil.copyfile(old_pic_name, left_copy_pic)
                tem_dic = dict()
                tem_dic['patient_id'] = data['patient_id']
                tem_dic['selected'] = '1'
                tem_dic['pic_name'] = left_pic_name.split('/')[2]
                tem_dic['own_to'] = data['diagnose_record']
                PatientPicture.objects.filter(pic_name=left_eye_pic_name).update(selected=1)
                PatientPicture.objects.create(**tem_dic)
            else:
                '''需要知道是第几次就诊的两张照片被选择为selected 所以先将以下一句代码注释，后果是可能会出现
                                一次就诊断记录的被选中照片超过三张
                                '''
                # PatientPicture.objects.filter(patient_id=data['patient_id']).update(selected=0)
                '''一键增强之后 没有对应的selected照片'''
                tem_dic = dict()
                tem_dic['patient_id'] = data['pk_patient_id']
                tem_dic['selected'] = '1'
                # tem_dic['own_to'] = data['diagnose_record']
                if 'strengthen' in left_eye_pic_name:
                    tem_dic['pic_name'] = left_eye_pic_name
                    PatientPicture.objects.create(**tem_dic)
                if 'strengthen' in right_eye_pic_name:
                    tem_dic['pic_name'] = right_eye_pic_name
                    PatientPicture.objects.create(**tem_dic)
                PatientPicture.objects.filter(pic_name=left_eye_pic_name).update(selected=1)
                PatientPicture.objects.filter(pic_name=right_eye_pic_name).update(selected=1)

            # if 'diagnose_id' in data:
            #     diagnose_result = DoctorDiagnose.objects.filter(id = data['diagnose_id'])[0]
            #     doctor_id = diagnose_result.diagnose_doctor
            # else:
            #     diagnose_result = DoctorDiagnose.objects.filter(patient_id=data['patient_id'])[data['diagnose_record']]
            #     doctor_id = diagnose_result.diagnose_doctor

            # if not doctor_id:
            # doctor_id = data['diagnose_doctor']
            # user_profile = UserProfile.objects.get(id=doctor_id)
            # doctor_name = user_profile.last_name + user_profile.first_name
            data['doctor_name'] = data['diagnose_doctor']['last_name'] + data['diagnose_doctor']['first_name']
            data['report_title'] = ''

            # folder_name = query_result[0].superior_simplify_name
            # hospital = query_result[0].superior_hospital_name
            # data['report_title'] = query_result[0].report_title

            # diagnose_result = DoctorDiagnose.objects.filter(pk_doctor_diagnose_id=data['diagnose_id'])[0]
            if 'diagnose_time' in data:
                # if data['diagnose_time']:
                # 将诊断报告中的事件秒给去除
                seconds = data['diagnose_time'][-3:]
                tem_diagnose_time = data['diagnose_time'].replace(seconds, '')
                data['diagnose_time'] = tem_diagnose_time
            # else:
            #     diagnose_time = diagnose_result.diagnose_time
            #     if diagnose_time:
            #         data['diagnose_time'] = diagnose_time.strftime('%Y-%m-%d %H:%M')
            #     else:
            #         data['diagnose_time'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
            data['database'] = folder_name

            data['left_origin_src'] = settings.BASE_DIR + '/media' + data['left_origin_src']
            data['right_origin_src'] = settings.BASE_DIR + '/media' + data['right_origin_src']
            data['right_AI_src'] = settings.BASE_DIR + '/media' + data['right_AI_src'].replace('_strengthen', '')
            data['left_AI_src'] = settings.BASE_DIR + '/media' + data['left_AI_src'].replace('_strengthen', '')
            if os.path.exists(data['left_origin_src']):
                pass
            else:
                data['left_origin_src'] = settings.BASE_DIR + '/media/' + 'noimg.jpg'
            if os.path.exists(data['right_origin_src']):
                pass
            else:
                data['right_origin_src'] = settings.BASE_DIR + '/media/' + 'noimg.jpg'
            if os.path.exists(data['left_AI_src']):
                pass
            else:
                data['left_AI_src'] = settings.BASE_DIR + '/media/' + 'noimg.jpg'
            if os.path.exists(data['right_AI_src']):
                pass
            else:
                data['right_AI_src'] = settings.BASE_DIR + '/media/' + 'noimg.jpg'

            pdf_maker = PdfMaker(data)
            if 'parent_name' in data:
                pdf_name = pdf_maker.create_pdf3()
                # if 'diagnose_id' in data:
                #     DoctorDiagnose.objects.filter(id=data['diagnose_id']).update(pdf_name=pdf_name)
                return HttpResponse(pdf_name)
            else:
                pdf_maker.create_pdf4()
                return HttpResponse(folder_name)

        except Exception as e:
            print('single pdf generation failed:', e)
            ex_type, ex_val, ex_stack = sys.exc_info()
            print(ex_type)  # 打印异常类型
            print(ex_val)  # 打印异常的值
            for stack in traceback.extract_tb(ex_stack):
                print(stack)  # 打印异常位置
            return HttpResponse('0')


def send_email(email, username, url):
    import smtplib
    from email.mime.text import MIMEText
    from email.header import Header

    # 第三方 SMTP 服务
    mail_host = "smtp.mxhichina.com"  # 设置服务器
    mail_user = "support@orbisbiotech.com"  # 用户名
    mail_pass = "Orbis888"  # 口令

    sender = 'support@orbisbiotech.com'
    receivers = [email]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    tem_secret_name = base64.b64encode(bytes(username, 'utf-8'))
    secret_name = bytes.decode(tem_secret_name)
    mail_msg = """
    <p>密码修改请点击以下链接</p>
    <p><a href=""" + url + """logoutOperation/modifyPwd?sid=""" + secret_name + """>修改奥比斯远程医疗系统密码</a></p>
    <p>您的用户名:""" + username + """</p>
    <p>奥比斯科技竭诚为您服务</p>
    """
    print(mail_msg)
    message = MIMEText(mail_msg, 'html', 'utf-8')
    message['From'] = Header("support@orbisbiotech.com", 'utf-8')
    message['To'] = Header(email, 'utf-8')

    subject = '密码重置'
    message['Subject'] = Header(subject, 'utf-8')

    print('开始发送邮件')
    smtpObj = smtplib.SMTP_SSL(timeout=2)
    smtpObj.connect(mail_host, 465)  # 465 为 SMTP 端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    smtpObj.quit()
    print("邮件发送成功")


def user_logout_operation(request, order):
    if order == 'forgetPwd':  # 忘记密码发送邮件
        data = json.loads(request.body.decode('utf-8'))
        email = data['email']
        url = data['url']
        print(data)
        result = UserProfile.objects.filter(email=email)
        if not result:
            return HttpResponse('0')
        try:
            username = result[0].username
            send_email(email, username, url)
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

    if order == 'get_openid':
        app_id = 'wxa212e4161b9c2dfb'
        app_secret = '5dd1248d4e14ee408d9210da9ba9e5f9'
        try:
            js_code = request.GET.get('js_code')
            url = 'https://api.weixin.qq.com/sns/jscode2session?appid=' \
                  + app_id + '&secret=' + app_secret + '&js_code=' + js_code + \
                  '&grant_type=authorization_code'
            f = urllib.request.urlopen(url)
            result = f.read().decode('utf-8')
        except Exception as e:
            ex_type, ex_val, ex_stack = sys.exc_info()
            print(ex_type)  # 打印异常类型
            print(ex_val)  # 打印异常的值
            for stack in traceback.extract_tb(ex_stack):
                print(stack)  # 打印异常位置
            return HttpResponse('0')
        else:
            return HttpResponse(result)

    if order == "sendSms":
        try:
            send_sms = SendSms(request)
            send_sms.send_single_message()
        except Exception as e:
            ex_type, ex_val, ex_stack = sys.exc_info()
            print(ex_type)  # 打印异常类型
            print(ex_val)  # 打印异常的值
            print(e)
            for stack in traceback.extract_tb(ex_stack):
                print(stack)  # 打印异常位置
            return HttpResponse('0')
        return HttpResponse('1')

    if order == 'get_mobile_code':  # 获取手机验证码
        data = json.loads(request.body.decode('utf-8'))
        patient_tel = data['patient_tel']
        seeds = string.digits
        random_str = random.sample(seeds, k=4)
        random_number = "".join(random_str)
        tem_dic = dict()
        tem_dic['send_time'] = datetime.datetime.now()
        tem_dic['mobile'] = patient_tel
        tem_dic['code'] = random_number
        try:
            send_sms = SendMobileVerifyCode(tem_dic)
            send_sms.send_code()
        except Exception as e:
            ex_type, ex_val, ex_stack = sys.exc_info()
            print(ex_type)  # 打印异常类型
            print(ex_val)  # 打印异常的值
            print(e)
            for stack in traceback.extract_tb(ex_stack):
                print(stack)  # 打印异常位置
            return HttpResponse('0')
        record = MobileVerifyRecord.objects.filter(mobile=patient_tel)
        if record:
            MobileVerifyRecord.objects.filter(mobile=patient_tel).update(**tem_dic)
        else:
            MobileVerifyRecord.objects.create(**tem_dic)
        return HttpResponse('1')

    if order == 'verify_mobile_code':  # 验证手机验证码
        data = json.loads(request.body.decode('utf-8'))
        patient_tel = data['patient_tel']
        patient_code = data['patient_code']
        record = MobileVerifyRecord.objects.filter(mobile=patient_tel)
        if record:
            expire_time = record[0].send_time + datetime.timedelta(seconds=60)
            if expire_time < datetime.datetime.now():
                print('验证码已经过期')
                return HttpResponse('0')
            else:
                print('验证码没有过期')
                if patient_code != record[0].code:
                    print('验证码错误')
                    return HttpResponse('1')
                else:
                    print('验证码正确')
                    return HttpResponse('2')
        else:
            return HttpResponse('3')

    if order == 'modifyPwd':  # 展示修改密码的页面
        form = ResetPwdForm()
        print(form)
        return render(request, "password_reset.html", context={'form': form})

    if order == 'modifyPwdDone':
        data = json.loads(request.body.decode('utf-8'))
        print('收到修改密码的数据')
        back_form = dict()
        if 'username' not in data:
            back_form['info'] = '该用户不存在,请从邮箱打开该链接'
            return HttpResponse(json.dumps(back_form, ensure_ascii=False))
        tem_secret_name = data['username']
        missing_padding = 4 - len(tem_secret_name) % 4
        if missing_padding:
            tem_secret_name += '=' * missing_padding
        secret_name = tem_secret_name.encode('utf-8')
        tem_username = base64.decodestring(secret_name)
        username = bytes.decode(tem_username)
        user = UserProfile.objects.filter(username=username)
        if not user:
            back_form['info'] = '该用户不存在,请从邮箱打开该链接'
            return HttpResponse(json.dumps(back_form, ensure_ascii=False))
        del data['username']
        data['password'] = data['password1']
        form = ResetPwdForm(data)
        if form.is_valid():
            print('验证成功', username)
            user[0].set_password(data['password'])
            user[0].save()
            return HttpResponse('1')
        else:
            for filed in form:
                result_form = str(filed.errors)
                if 'error' not in result_form:
                    continue
                res1 = ''.join(re.findall('[\u4e00-\u9fa5]', result_form))
                back_form['info'] = res1
            return HttpResponse(json.dumps(back_form, ensure_ascii=False))

    if order == 'pwd_reset_complete':
        return render(request, "password_reset_complete.html")

    if order == 'dcm_request':
        try:
            data = request.POST.getlist('patient_info')
            tem_patient_img = request.FILES.getlist('img')
            random_number = str(random.randint(1, 1000))
            random_string = random.choice(string.ascii_lowercase)
            random_name = random_number + random_string
            position = settings.BASE_DIR + "/media/patient_img/"
            id_direction_list = list()
            for dic in data:
                id_direction_list.append(eval(dic))
            i = 0

            '''
            改版后 小盒子传来的patient_id不是真正的patient_id 而是患者在该家医院的序号，
            需要找到该序号对应的patient_id
            '''
            # patient_count 序号
            patient_count = id_direction_list[0]['patient_id']
            patient_name = id_direction_list[0]['patient_name']
            file_md5 = id_direction_list[0]['file_md5']
            print('md5_from_small_box: %s' % file_md5)
            file_path = id_direction_list[0]['file_path']
            directory_name = ''
            if 'directory_name' in id_direction_list[0]:
                directory_name = id_direction_list[0]['directory_name']
                print(directory_name)
            if 'superior_hospital_id' in id_direction_list[0]:
                superior_hospital_id = id_direction_list[0]['superior_hospital_id']
            else:
                superior_hospital_id = '1'

            '''
            医院的id号有了，患者的序号patient_count有了，接下来开始查询出patient_id 如果没有则创造一个
            '''
            upload_record = DoctorDiagnose.objects.filter(patient_count=patient_count,
                                                          hospital_area=superior_hospital_id)

            '''
            传来的序号需要与当前系统最大的序号做对比，如果传来的序号过大则不允许上传 直接返回1
            '''
            record3 = DoctorDiagnose.objects.filter(superior_hospital=superior_hospital_id)
            patient_count_max = record3.aggregate(Max('patient_count'))['patient_count__max']
            if not patient_count_max:
                patient_count_max = 0
            try:
                if int(patient_count) - int(patient_count_max) > 3:
                    print('序号过大，不允许创建')
                    print('patient_count', patient_count)
                    print('patient_count_max', patient_count_max)
                    return HttpResponse('1')
            except Exception as e:
                print(patient_count)
                print(patient_count_max)
                print(e)
                print('序号不是纯数字，不允许创建')
                return HttpResponse('1')

            dia_record = 0
            print('建档结果', upload_record)
            if upload_record:
                patient_id = upload_record[0].patient_id
                status = upload_record[0].status
                dia_record = upload_record[0].diagnose_record
                print('%s在远程建档了' % patient_id)
                print('目前状态是%s' % status)
            else:
                print('在远程未建档')
                tem_patient = dict()
                tem_patient['patient_name'] = patient_name
                tem_patient['patient_count'] = patient_count
                tem_patient['patient_age'] = '1'
                tem_patient['patient_tel'] = '11111111111'
                tem_patient['upload_signal'] = '1'
                tem_patient['pic_upload'] = '1'
                check_num, patient_count = create_check_num(superior_hospital_id)
                tem_patient['check_num'] = check_num
                with transaction.atomic():
                    try:
                        b = PatientInfo.objects.create(**tem_patient)
                        patient_id = b.patient_id
                        a = PatientInfo.objects.get(patient_id=patient_id)
                        a.superior_hospital.add(superior_hospital_id)
                    except Exception as e:
                        print(e)
                        ex_type, ex_val, ex_stack = sys.exc_info()
                        print(ex_type)  # 打印异常类型
                        print(ex_val)  # 打印异常的值
                        for stack in traceback.extract_tb(ex_stack):
                            print(stack)  # 打印异常位置
                        return HttpResponse('0')

            own_to = dia_record  # 为了不影响dia_record在其他地方的使用 用 own_to 代替
            never_exist_before = False
            if directory_name:
                print('小盒子端传来了文件夹的名称')
                picture_directory_record = PictureDirectoryRecord.objects.filter(
                    directory_name=directory_name).last()  # 取出最新记录
                if picture_directory_record:
                    print('这个文件夹之前有过上传记录')
                    own_to = picture_directory_record.own_to
                else:
                    # 如果这个文件夹名在之前从未出现过，则有可能是多次就诊
                    print('这个文件夹之前没有过上传记录')
                    never_exist_before = True
                    own_to = dia_record
                    PictureDirectoryRecord.objects.create \
                        (directory_name=directory_name, own_to=own_to, patient_id=patient_id)

            left_rop = 0
            right_rop = 0
            for f in tem_patient_img:
                '''ROP计算'''
                # label_rop, possible_rop = detect_rop(f)
                direction = id_direction_list[i]['direction']
                if direction == 'L':
                    direction = 'Left'
                    # left_rop = label_rop[0]
                else:
                    direction = 'Right'
                    # right_rop = label_rop[0]
                formats = os.path.splitext(f.name)[-1]
                origin_file_name = str(patient_id) + '_' + direction + '_' + random_name + "_origin_" + \
                                   str(i) + '_ori' + formats

                '''保存照片'''
                with open(position + origin_file_name, 'wb+') as destination:
                    for chunk in f.chunks():
                        destination.write(chunk)

                '''校验md5'''
                file_md5_server = file2md5(position + origin_file_name)
                print('file_md5_server: %s' % file_md5)
                print(file_md5 == file_md5_server)
                print(type(file_md5))
                print(type(file_md5_server))
                if file_md5 != file_md5_server:
                    print('MD5值不一致，删除该文件')
                    print(position + origin_file_name)
                    # os.remove(position + origin_file_name)
                    return HttpResponse(file_path)
                else:
                    print('MD5值正确，继续往下执行')

                '''MD5校验通过后保存照片信息到数据库'''
                PatientPicture.objects.create(patient_id=patient_id, pic_name=origin_file_name, own_to=own_to)
                i = i + 1

            diagnose_record = DoctorDiagnose.objects.filter(patient_id=patient_id).last()  # 取出最新记录

            if upload_record:
                update_dict = dict()
                dia_record = upload_record[0].diagnose_record
                now_time = datetime.datetime.now()
                update_dict['upload_signal'] = 1
                update_dict['pic_upload'] = 1
                update_dict['status'] = 0
                update_dict['diagnose_record'] = dia_record
                update_dict['apply_time'] = now_time

                if dia_record > 0:
                    diagnose_time = diagnose_record.diagnose_time
                    '''如果没有诊断时间 说明还是未诊 处于未诊断列表 无法计算当前时间与上次诊断时间 则如下处理'''
                    if not diagnose_time:
                        print('没有诊断时间 说明还在未诊列表')
                        PatientInfo.objects.filter(patient_id=patient_id).update(**update_dict)
                    else:
                        '''解决因网速慢刚诊断完又上传照片被误认为是多次就诊的bug。'''
                        time_delta = now_time - diagnose_time
                        if directory_name:
                            if never_exist_before:
                                print('该患者已经诊断，并且该照片所在的文件夹从未出现过'
                                      '说明是再次就诊，则将status 改为0')
                                PatientInfo.objects.filter(patient_id=patient_id).update(**update_dict)
                            else:
                                print('该患者已诊断，但是该照片所在的文件夹以前出现过'
                                      '说明是不是再次就诊，则将status不动  可以全都不动'
                                      '将照片的own_to搞对即可')
                                # del update_dict['status']
                                # PatientInfo.objects.filter(patient_id=patient_id).update(**update_dict)
                        else:
                            ''''兼容版本 如果小盒子没有判断多次就诊 则使用时间来判断'''
                            print('相差秒数%s' % time_delta.seconds)
                            if time_delta.seconds > 1:
                                print('该患者已经诊断，且照片上传时间间隔超过1天说明是再次就诊，则将status 改为0')
                                PatientInfo.objects.filter(patient_id=patient_id).update(**update_dict)
                else:
                    print('建档之后未诊断,是第一次就诊')
                    PatientInfo.objects.filter(patient_id=patient_id).update(upload_signal=1, pic_upload=1)

            if diagnose_record:  # 如果有诊断记录(可能是AI先生成的,人工还未诊断)
                id = diagnose_record.id
                diagnose_advice = diagnose_record.diagnose_advice  # 看看医生是否已诊断
                if not diagnose_advice:  # 如果医生未诊断，说明患者还在未诊列表并且用户不止一次在上传照片
                    DoctorDiagnose.objects.filter(id=id).update(left_rop=left_rop, right_rop=right_rop,
                                                                patient_id=patient_id)
                else:  # 医生已诊断,说明是再次就诊时第一次上传照片
                    if never_exist_before:
                        print('医生已诊断,且照片从来没见过,说明是再次就诊时第一次上传照片')
                        DoctorDiagnose.objects.create(left_rop=left_rop, right_rop=right_rop, patient_id=patient_id)
            else:  # 如果没有诊断记录说明是首次就诊
                DoctorDiagnose.objects.create(left_rop=left_rop, right_rop=right_rop, patient_id=patient_id)

        except Exception as e:
            print(e)
            ex_type, ex_val, ex_stack = sys.exc_info()
            print(ex_type)  # 打印异常类型
            print(ex_val)  # 打印异常的值
            for stack in traceback.extract_tb(ex_stack):
                print(stack)  # 打印异常位置
            return HttpResponse('0')
        return HttpResponse('1')

    if order == "add":
        try:
            data = json.loads(request.body.decode('utf-8'))
            openid = data['openid']
            del data['openid']
            try:
                del data['modify_type']
            except Exception as e:
                pass
            superior_hospital_id = ''

            if 'hospital_id' in data:
                superior_hospital_id = data['hospital_id']

                del data['hospital_id']

                record2 = PatientInfo.objects.filter(patient_tel=data['patient_tel'],
                                                     superior_hospital=superior_hospital_id,
                                                     patient_name=data['patient_name'])
                check_num, patient_count = create_check_num(superior_hospital_id)
                data['patient_count'] = patient_count
                data['check_num'] = check_num

            else:
                record2 = PatientInfo.objects.filter(patient_tel=data['patient_tel'],
                                                     patient_name=data['patient_name'])
            if record2:
                '''重复建档'''
                return HttpResponse('2')

        except Exception as e:
            print('建档错误', e)
            ex_type, ex_val, ex_stack = sys.exc_info()
            for stack in traceback.extract_tb(ex_stack):
                print(stack)  # 打印异常位置
            return HttpResponse('0')

        try:
            with transaction.atomic():
                patient = PatientInfo.objects.create(**data)
                patient_id = patient.patient_id
                a = WeChatUser.objects.create(openid=openid)
                a.patient.add(patient_id)
        except Exception as e:
            print('save basic info failed', e)
            ex_type, ex_val, ex_stack = sys.exc_info()
            print(ex_type)  # 打印异常类型
            print(ex_val)  # 打印异常的值
            for stack in traceback.extract_tb(ex_stack):
                print(stack)  # 打印异常位置
            return HttpResponse('0')

        try:
            with transaction.atomic():  # 数据库事务，数据库出现错误会进行回退
                a = PatientInfo.objects.get(patient_id=patient_id)
                if superior_hospital_id:
                    a.superior_hospital.add(superior_hospital_id)  # 加入患者扫码时传来的上级医院
                return HttpResponse(patient_id)
        except Exception as e:
            print(e)
            ex_type, ex_val, ex_stack = sys.exc_info()
            print(ex_type)  # 打印异常类型
            print(ex_val)  # 打印异常的值
            for stack in traceback.extract_tb(ex_stack):
                print(stack)  # 打印异常位置
            return HttpResponse('0')

    if order == 'addStep2':
        '''基本信息填写完成后，补充信息后再次提交'''
        data = json.loads(request.body.decode('utf-8'))
        # patient_id = data['patient_id']
        s_hospital_id = data['hospital_id']
        check_num, patient_count = create_check_num(s_hospital_id)
        data['patient_count'] = patient_count
        data['check_num'] = check_num
        try:
            del data['openid']
            del data['patient_id']
            del data['hospital_id']
            with transaction.atomic():
                c = PatientInfo.objects.create(**data)
                a = PatientInfo.objects.get(patient_id=c.patient_id)
                a.superior_hospital.add(s_hospital_id)  # 加入患者扫码时传来的上级医院
        except Exception as e:
            print('modify basic info failed', e)
            ex_type, ex_val, ex_stack = sys.exc_info()
            print(ex_type)  # 打印异常类型
            print(ex_val)  # 打印异常的值
            for stack in traceback.extract_tb(ex_stack):
                print(stack)  # 打印异常位置
            return HttpResponse('0')
        else:
            return HttpResponse('1')

    if order == 'modify':
        data = json.loads(request.body.decode('utf-8'))
        patient_id = data['patient_id']
        if 'modify_type' not in data:
            data['modify_type'] = '0'
        else:
            s_hospital_id = data['hospital_id']
        modify_type = data['modify_type']
        print('modify_type:%s' % modify_type)
        try:
            openid = data['openid']
            del data['openid']
            del data['patient_id']
            if 'hospital_id' in data:
                del data['hospital_id']
            if 'modify_type' in data:
                del data['modify_type']
            with transaction.atomic():
                if modify_type == '0':
                    print('普通修改')
                    try:
                        tem_patient = PatientInfo.objects.get(patient_id=patient_id)
                        patient_tel = tem_patient.patient_tel
                        patient_name = tem_patient.patient_name
                        PatientInfo.objects.filter \
                            (patient_name=patient_name, patient_tel=patient_tel).update(**data)
                    except Exception as e:
                        print(e)
                        return HttpResponse('0')
                elif modify_type == '2':
                    print('当前不属于任何医院，需要分配医院并更新患者信息')
                    # PatientInfo.objects.filter(patient_id=patient_id).update(**data)
                    a = PatientInfo.objects.get(patient_id=patient_id)
                    a.superior_hospital.add(s_hospital_id)  # 加入患者扫码时传来的上级医院
                    check_num, patient_count = create_check_num(s_hospital_id)
                    data['patient_count'] = patient_count
                    data['check_num'] = check_num
                    PatientInfo.objects.filter(patient_id=patient_id).update(**data)
                else:
                    print('未在本院建档，但是已经属于其他医院，则新建一个人并分配到本院')
                    check_num, patient_count = create_check_num(s_hospital_id)
                    data['patient_count'] = patient_count
                    data['check_num'] = check_num
                    p = PatientInfo.objects.create(**data)
                    a = PatientInfo.objects.get(patient_id=p.patient_id)
                    a.superior_hospital.add(s_hospital_id)  # 加入患者扫码时传来的上级医院
                    a = WeChatUser.objects.create(openid=openid)
                    a.patient.add(p.patient_id)
                    del data['patient_count']
                    del data['check_num']
                    try:
                        tem_patient = PatientInfo.objects.get(patient_id=patient_id)
                        patient_tel = tem_patient.patient_tel
                        patient_name = tem_patient.patient_name
                        PatientInfo.objects.filter(patient_tel=patient_tel, patient_name=patient_name).update(**data)
                    except Exception as e:
                        print(e)
                        return HttpResponse('0')

                    return HttpResponse(p.patient_id)

        except Exception as e:
            print('modify basic info failed', e)
            ex_type, ex_val, ex_stack = sys.exc_info()
            print(ex_type)  # 打印异常类型
            print(ex_val)  # 打印异常的值
            for stack in traceback.extract_tb(ex_stack):
                print(stack)  # 打印异常位置
            return HttpResponse('0')
        else:
            return HttpResponse('1')

    if order == 'get_wechat_openid':
        base_dir = settings.BASE_DIR
        try:
            data = json.loads(request.body.decode('utf-8'))
            code = data['code']
            if 'redirect_url' in data:
                redirect_url = data['redirect_url']
                if 'message' in redirect_url:  # 这里需要使用妇幼公众号
                    url = 'https://api.weixin.qq.com/sns/oauth2/access_token?' \
                          'appid=wx3d655a4a9d298966&' \
                          'secret=7eb0114b1db97efce3b693152f94a4ab&' \
                          'code=' + code + '&grant_type=authorization_code'
                else:  # 这里需要使用orbis或者谱耀众号
                    if 'wshong' in base_dir:
                        # 奥比斯
                        url = 'https://api.weixin.qq.com/sns/oauth2/access_token?' \
                              'appid=wxb09d72b0a37558e6&' \
                              'secret=53a954722cfa6320e14ad76d685c4a57&' \
                              'code=' + code + '&grant_type=authorization_code'
                    else:

                        # 泰明
                        url = 'https://api.weixin.qq.com/sns/oauth2/access_token?' \
                              'appid=wxbc3a2d6336fa4869&' \
                              'secret=abacfc2a9eef7ae53f979f5d9d95bf84&' \
                              'code=' + code + '&grant_type=authorization_code'

            else:  # 这里需要使用orbis或者谱耀众号
                # 奥比斯
                if 'wshong' in base_dir:
                    url = 'https://api.weixin.qq.com/sns/oauth2/access_token?' \
                          'appid=wxb09d72b0a37558e6&' \
                          'secret=53a954722cfa6320e14ad76d685c4a57&' \
                          'code=' + code + '&grant_type=authorization_code'

                # 泰明
                else:
                    url = 'https://api.weixin.qq.com/sns/oauth2/access_token?' \
                          'appid=wxbc3a2d6336fa4869&' \
                          'secret=abacfc2a9eef7ae53f979f5d9d95bf84&' \
                          'code=' + code + '&grant_type=authorization_code'

            response = urllib.request.urlopen(url).read().decode('utf-8')
            return HttpResponse(response)
        except Exception as e:
            ex_type, ex_val, ex_stack = sys.exc_info()
            print(ex_type)  # 打印异常类型
            print(ex_val)  # 打印异常的值
            for stack in traceback.extract_tb(ex_stack):
                print(stack)  # 打印异常位置
            return HttpResponse('0')

    if order == 'bind_child':
        try:
            data = json.loads(request.body.decode('utf-8'))
            print(data)
            patients2 = ''
            patient_tel = data['mother_tel']
            if 'parent_name' in data:
                parent_name = data['parent_name']
                patients2 = PatientInfo.objects.filter(parent_name=parent_name, patient_tel=patient_tel)
            if 'patient_name' in data:
                patient_name = data['patient_name']
                patients2 = PatientInfo.objects.filter(patient_name=patient_name, patient_tel=patient_tel)
            mother_ID_number = data['mother_ID_number']
            openid = data['openid']
            patients1 = PatientInfo.objects.filter(mother_ID_number=mother_ID_number)

        except Exception as e:
            print(e)
            ex_type, ex_val, ex_stack = sys.exc_info()
            print(ex_type)  # 打印异常类型
            print(ex_val)  # 打印异常的值
            for stack in traceback.extract_tb(ex_stack):
                print(stack)  # 打印异常位置
            return HttpResponse('0')
        if patients1:
            try:
                with transaction.atomic():
                    for p in patients1:
                        a = WeChatUser.objects.create(openid=openid)
                        patient_id = p.patient_id
                        a.patient.add(patient_id)
                    return HttpResponse('1')
            except Exception as e:
                print(e)
                ex_type, ex_val, ex_stack = sys.exc_info()
                print(ex_type)  # 打印异常类型
                print(ex_val)  # 打印异常的值
                for stack in traceback.extract_tb(ex_stack):
                    print(stack)  # 打印异常位置
                return HttpResponse('0')

        elif patients2:
            try:
                with transaction.atomic():
                    for p in patients2:
                        a = WeChatUser.objects.create(openid=openid)
                        patient_id = p.patient_id
                        a.patient.add(patient_id)
                    return HttpResponse('1')
            except Exception as e:
                print(e)
                ex_type, ex_val, ex_stack = sys.exc_info()
                print(ex_type)  # 打印异常类型
                print(ex_val)  # 打印异常的值
                for stack in traceback.extract_tb(ex_stack):
                    print(stack)  # 打印异常位置
                return HttpResponse('0')

        else:
            return HttpResponse('2')

    if order == 'unbind_child':
        try:
            data = json.loads(request.body.decode('utf-8'))
            openid = data['openid']
            patient_id = data['patient_id']
            patient = PatientInfo.objects.get(patient_id=patient_id)
            WeChatUser.objects.filter(openid=openid, patient=patient).delete()
        except Exception as e:
            print(e)
            return HttpResponse('0')
        return HttpResponse('1')

    if order == "upload_log":  # 小盒子端上传日志
        user_name = request.GET.get('hospital_name')
        my_file = request.FILES.get("user_log", None)
        if not user_name:
            user_name = 'fuyou'
        if not my_file:
            return HttpResponse("0")
        try:
            position = settings.BASE_DIR + "/media/log_file/" + user_name
            mkdir(position)
            now_time = datetime.datetime.now()
            # 格式化时间字符串
            str_time = now_time.strftime("%Y-%m-%d %X").replace(' ', '_') + '.log'
            with open(position + "/" + str_time, 'wb+') as destination:
                for chunk in my_file.chunks():
                    destination.write(chunk)
        except Exception as e:
            ex_type, ex_val, ex_stack = sys.exc_info()
            print(ex_type)  # 打印异常类型
            print(ex_val)  # 打印异常的值
            for stack in traceback.extract_tb(ex_stack):
                print(stack)  # 打印异常位置
            return HttpResponse("0")
        else:
            return HttpResponse("1")

    if order == 'get_pdf':
        data = json.loads(request.body.decode('utf-8'))
        id = data['diagnose_id']
        diagnose_info = DoctorDiagnose.objects.filter(id=id)[0]
        pdf_name = diagnose_info.pdf_name
        diagnose_time = diagnose_info.diagnose_time

        time_line = datetime.datetime.strptime('2022-04-06', "%Y-%m-%d")

        if pdf_name:
            # 新版本的诊断字段中会保存pdf_name 信息
            return HttpResponse(pdf_name)
        else:
            # 诊断时间小于当前时间的 都属于旧版本 则直接展示网页
            if diagnose_time < time_line:
                return HttpResponse('1')

            # 诊断时间大于当前时间的属于 新版本 则提示未出具报告
            else:
                return HttpResponse('0')


def dict_fetchall(cursor):  # 解析数据库查询结果
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]
