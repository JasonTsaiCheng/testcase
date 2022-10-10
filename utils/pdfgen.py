# -*- coding:utf-8 -*-
__author__ = 'Jason'
__date__ = '2019/9/5 14:09'
from PIL import Image, ImageDraw, ImageFont
import PIL.Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
import reportlab.pdfbase.ttfonts
from django.conf import settings
from utils.mkdir import mkdir
import numpy as np
import cv2
import os, re, datetime
from reportlab.pdfbase.ttfonts import TTFont
import xml.etree.ElementTree as ET
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph
from pictures.models import PatientInfo
from users.models import UserProfile

ParagraphStyle.defaults['wordWrap'] = "CJK"
from reportlab.lib.units import inch

mask_report = cv2.imread(r'trained_model/template_report.bmp', 0)
we_report = cv2.imread(r'trained_model/weiqing_mask_template.bmp', 0)
we_color = cv2.imread(r'trained_model/we_color.bmp', 1)
font_position = settings.BASE_DIR + "/media/font/wqy-zenhei.ttc"
bold_font_position = settings.BASE_DIR + "/media/font/微软雅黑粗体.ttf"
# font_style1 = settings.BASE_DIR + "/media/font/文泉驿微米黑.ttf"
# font_style2 = settings.BASE_DIR + "/media/font/文泉驿正黑.ttf"
# font_style3 = settings.BASE_DIR + "/media/font/文泉驿等宽微米黑.ttf"
# font_style4 = settings.BASE_DIR + "/media/font/文泉驿等宽正黑.ttf"
# font_style5 = settings.BASE_DIR + "/media/font/微软雅黑粗体.ttf"
# font_style6 = settings.BASE_DIR + "/media/font/FZZZHONGHJW.TTF"
# font_style7 = settings.BASE_DIR + "/media/font/FZZCHJW.TTF"
# font_style8 = settings.BASE_DIR + "/media/font/FZZDHJW.TTF"
font_style9 = settings.BASE_DIR + "/media/font/simhei.ttf"


# font_style10 = settings.BASE_DIR + "/media/font/FZZXHJW.TTF"
# font_style11 = settings.BASE_DIR + "/media/font/FZZHJW.TTF"


def read_xml(xml_path):
    xml_file = os.path.abspath(xml_path)
    diseases = dict()
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()
        diseases['dr'] = root[0].text
        diseases['pm'] = root[1].text
        diseases['tr'] = root[2].text
        diseases['dr_suggestion'] = root[3].text
        diseases['pm_suggestion'] = root[4].text
        diseases['tr_suggestion'] = root[5].text
        return diseases
    except Exception as e:
        print(e)


#
# def resize_image_for_report(img):
#     if img.shape[0] / img.shape[1] != 3 / 4:
#         print('size is not 4:3')
#         if img.shape[1] <= int(img.shape[0] * 4 / 3):
#             img_new = np.zeros((img.shape[0], int(img.shape[0] * 4 / 3), 3), dtype=np.uint8)
#             pad = (int(img.shape[0] * 4 / 3) - img.shape[0]) // 2
#             img_new[:, pad:int(img.shape[0] + pad), :] = img
#             return img_new
#         else:
#             return img
#     else:
#         return img


#  图像resize时的取整问题
def resize_image_for_report(img):
    if (img.shape[0] / img.shape[1] - 3 / 4) > 1.0 / img.shape[0]:
        print('size is not 4:3')
        try:
            if img.shape[1] <= int(img.shape[0] * 4 / 3):
                img_new = np.zeros((img.shape[0], int(img.shape[0] * 4 / 3), 3), dtype=np.uint8)
                pad = (int(img.shape[0] * 4 / 3) - img.shape[0]) // 2
                img_new[:, pad:int(img.shape[0] + pad), :] = img
                return img_new
            else:
                return img
        except Exception as e:
            print(e)
            return img
    else:
        return img


def retention_tag(file, save_position):
    global mask_report, we_report, we_color
    mask_tmp = mask_report.copy()
    color_tmp = we_color.copy()
    we_tmp = we_report.copy()
    img = Image.open(file)
    if img.mode == 'RGBA':
        img = img.convert("RGB")
    img = np.array(img)
    h, w = img.shape[:2]
    print(h, w)

    # 我们的相机的图像
    if (h, w) == (1728, 2304) and mask_tmp is not None:
        # 用于解决没有右下角的标记问题的解决。
        is_mark = np.sum(img[1430:1440, 1800:1810, ::-1])
        print('is_mark', is_mark)
        if is_mark > 1000:
            if np.max(mask_tmp) == 255:
                mask_result = np.array(mask_tmp / 255, dtype=np.float)
                img[mask_result > 0.5] = 255
        else:
            img[img[:, :, 0] < 10] = 255

    elif (h, w) == (1752, 2336) and we_tmp is not None:
        is_mark = np.sum(img[1430:1440, 1800:1810, ::-1])
        if is_mark > 1000:
            if np.max(we_tmp) == 255:
                mask_result = np.array(we_tmp / 255, dtype=np.float)
                img[mask_result > 0.5] = 255
        else:
            img[img[:, :, 0] < 10] = 255
        img[1440:1752, 0:650] = color_tmp[1440:1752, 0:650, ::-1]
        # tmp_img = img + color_tmp
        # img = np.clip(tmp_img, 0, 255)
    img = resize_image_for_report(img)
    cv2.imwrite(save_position, img[:, :, ::-1])


def get_result(left_img_exist, right_img_exist, left_ai, right_ai, left_warning, right_warning):
    if left_img_exist and right_img_exist:  # 首先判断左右眼是否都有照片
        if left_warning and right_warning:
            diagnose_right = '右:图像质量不佳，无法计算'
            diagnose_left = '左:图像质量不佳，无法计算'
        elif left_warning:
            diagnose_left = '左:图像质量不佳，无法计算'
            if not right_ai:
                diagnose_right = '右:无异常'
            else:
                diagnose_right = '右:异 常'
        elif right_warning:
            diagnose_right = '右:图像质量不佳，无法计算'
            if not right_ai:
                diagnose_left = '左:无异常'
            else:
                diagnose_left = '左:异 常'
        else:
            if not left_ai and not right_ai:  # 再判断左右眼是否都异常
                diagnose_right = '右:无异常'
                diagnose_left = '左:无异常'
            elif not left_ai:
                diagnose_right = '右:异 常'
                diagnose_left = '左:无异常'
            elif not right_ai:
                diagnose_right = '右:无异常'
                diagnose_left = '左:异 常'
            else:
                diagnose_right = '右:异 常'
                diagnose_left = '左:异 常'

    elif left_img_exist:  # 左眼有照片右眼没有
        if left_warning:
            diagnose_left = '左:图像质量不佳，无法计算'
            diagnose_right = '右:无照片'
        else:
            if not left_ai:
                diagnose_right = '右:无照片'
                diagnose_left = '左:无异常'
            else:
                diagnose_right = '右:无照片'
                diagnose_left = '左:异 常'
    else:  # 右眼有照片 左眼没有
        if right_warning:
            diagnose_right = '右:图像质量不佳，无法计算'
            diagnose_left = '左:无照片'
        else:
            if not right_ai:
                diagnose_right = '右:无异常'
                diagnose_left = '左:无照片'
            else:
                diagnose_right = '右:异 常'
                diagnose_left = '左:无照片'
    return diagnose_right, diagnose_left


def create_pdf(data):
    report_type = 3  # 由此得知报告类型是AI报告还是非AI报告，0代表AI报告
    if 'reportType' in data:
        report_type = data['reportType']
    dir = settings.BASE_DIR + "/media/patient_pdf/" + data['database']
    mkdir(dir)
    patient_id = str(data['patient_id'])
    pdf_name = dir + '/' + data['patient_name'].strip() + '_' + patient_id + '.pdf'
    reportlab.pdfbase.pdfmetrics.registerFont(
        reportlab.pdfbase.ttfonts.TTFont('song', font_position))  # 注册字体
    c = canvas.Canvas(pdf_name)
    width, height = A4
    print('width,height', width, height)
    # title and subtitle
    subtitle = "眼底检查报告"
    title = "合肥高新区天乐社区卫生服务中心"
    title_len = len(title) / 3
    subtitle_len = len(subtitle)
    print('len(subtitle)', len(subtitle))
    title_size = 20
    subtitle_size = 15

    # 写了一个小标题
    c.setFont('song', subtitle_size)
    x_point = width / 2 - (subtitle_len * subtitle_size) / 2
    y_point = height - 1.5 * subtitle_size - 10
    c.drawString(x_point, y_point, subtitle)

    # 画了一条分割线
    c.line(0, y_point - 1.5 * subtitle_size, width, y_point - 1.5 * subtitle_size)

    name = '姓名:'
    gender = '性别:'
    age = '年龄:'
    diagnose_date = '日期:'
    print('data[diagnose_time]', data['diagnose_time'])
    if data['diagnose_time']:
        diagnose_time = data['diagnose_time']
    else:
        diagnose_time = ' '
    basic_info_height = y_point - 1.5 * subtitle_size - 10  # 分割线高度
    name_height = y_point - 1.5 * subtitle_size - 20
    name_width = 20
    gender_height = y_point - 1.5 * subtitle_size - 20
    gender_width = 160
    age_height = y_point - 1.5 * subtitle_size - 20
    age_width = 300
    diagnose_date_height = y_point - 1.5 * subtitle_size - 20
    diagnose_date_width = 440

    c.drawString(name_width - 8, name_height, name)  # 姓名
    patient_name = data['patient_name']
    if len(patient_name) > 5:
        c.setFont('song', 10)
    c.drawString(name_width + 27, name_height, patient_name)  # 姓名

    c.setFont('song', 15)
    c.drawString(gender_width - 10, gender_height, gender)  # 性别
    if data['patient_gender'] == '0':
        patient_gender = '男'
    else:
        patient_gender = '女'
    c.drawString(gender_width + 25, gender_height, patient_gender)  # 性别

    c.drawString(age_width - 10, age_height, age)  # 年龄
    patient_age = str(data['patient_age'])
    c.drawString(age_width + 25, age_height, patient_age)  # 年龄

    c.drawString(diagnose_date_width - 17, diagnose_date_height, diagnose_date)  # 日期
    c.setFont('song', 15)
    c.drawString(diagnose_date_width + 18, diagnose_date_height, diagnose_time)  # 日期

    # 画了一条分割线
    c.line(0, basic_info_height - 1.5 * subtitle_size, width, basic_info_height - 1.5 * subtitle_size)

    # OD OS标志位置 (A4纸 宽595 高841)
    c.setFont('song', 15)
    od_os_height = basic_info_height - 1.5 * subtitle_size - 20
    od_width = 270
    os_width = 270
    left_iqa_score = str(data['left_iqa_score'])
    right_iqa_score = str(data['right_iqa_score'])
    # OD = 'OD(图像质量:'+right_iqa_score+')'
    # OS = 'OS(图像质量:'+left_iqa_score+')'
    OD = 'OD(右眼)'
    OS = 'OS(左眼)'
    c.drawString(od_width + 150, od_os_height - 20, OS)  # 左眼OS
    c.drawString(os_width - 150, od_os_height - 20, OD)  # 右眼OD

    # 眼部照片位置
    picture_height = od_os_height - 210  # 眼底照片底部位置
    left_picture_width = 160
    right_picture_width = 160
    right_output_file = data['right_origin_src']
    left_output_file = data['left_origin_src']
    left_origin_format = os.path.splitext(left_output_file)[-1]
    right_origin_format = os.path.splitext(right_output_file)[-1]
    patient_id = str(data['patient_id'])
    left_pdf_jpg = settings.BASE_DIR + \
                   "/media/patient_img/" + patient_id + '_left_pdf' + left_origin_format

    right_pdf_jpg = settings.BASE_DIR + \
                    "/media/patient_img/" + patient_id + '_right_pdf' + right_origin_format

    # retention_tag(left_output_file, left_pdf_jpg)
    c.drawImage(left_pdf_jpg, right_picture_width + 150, picture_height - 20, height=200, width=270)  # 200 270

    # retention_tag(right_output_file, right_pdf_jpg)
    c.drawImage(right_pdf_jpg, left_picture_width - 150, picture_height - 20, height=200, width=270)  # 150 200

    os.remove(left_pdf_jpg)
    os.remove(right_pdf_jpg)

    # AI照片位置
    AIpicture_height = picture_height - 20  # 眼底照片底部位置
    # 先画条线
    line_height = AIpicture_height - 30  # 照片顶端位置加上照片长度再向下偏移20
    print('picture_height', picture_height, basic_info_height - 1.5 * subtitle_size)
    c.line(0, line_height, width, line_height)

    # 影像发现位置
    find = '影像所见:'
    find_height = line_height - 35
    c.drawString(20, find_height, find)  # 类别

    find_height = find_height - 25

    # 影像发现下的右眼
    c.setFont('song', 12)
    right_eye = '右眼:'
    right_des_height = line_height - 60
    right_eye_width = 20
    c.drawString(right_eye_width, right_des_height, right_eye)  # 右眼
    c.drawString(right_eye_width + 35, right_des_height,
                 '无' if (data['right_desc'] == '' or data['right_desc'] is None) else data[
                     'right_desc'])  # 右眼

    # 影像发现下的左眼
    left_eye = '左眼:'
    left_des_height = right_des_height - 25
    left_eye_width = 20
    c.drawString(left_eye_width, left_des_height, left_eye)  # 左眼
    c.drawString(left_eye_width + 35, left_des_height,
                 '无' if (data['left_desc'] == '' or data['left_desc'] is None) else data['left_desc'])  # 左眼
    # 建议

    # 类别
    # type = '类别'
    # c.setFont('song', 12)
    type_height = find_height - 20
    # type_width = 20
    # c.drawString(type_width, type_height, type)  # 类别
    # amount = '数量(个)'
    # c.setFont('song', 12)

    square = '总面积mm'
    c.setFont('song', 12)
    square_height = type_height
    square_width = 320

    max_square = '最大面积mm'
    c.setFont('song', 12)
    max_square_height = type_height
    max_square_width = 480
    # 出血
    blood = '出血'
    blood_height = type_height - 20
    blood_width = 20
    # c.drawString(blood_width, blood_height, blood)  # 出血

    # 渗出
    ooze = '渗出'
    ooze_height = blood_height - 20
    ooze_width = 20
    # c.drawString(ooze_width, ooze_height, ooze)  # 渗出

    # # 影像发现下的右眼
    left_eye_height = blood_height
    # 诊断
    c.setFont('song', 15)
    sensation = '初步印象:'
    sensation_height = left_eye_height - 20
    sensation_width = 20
    c.drawString(sensation_width, sensation_height, sensation)  # 诊断

    # 诊断发现下的右眼
    c.setFont('song', 12)
    right_eye = '右眼:'
    right_eye_height = sensation_height - 25
    right_eye_width = 20
    c.drawString(right_eye_width, right_eye_height, right_eye)  # 右眼
    c.drawString(right_eye_width + 35, right_eye_height,
                 '无' if (data['right_diagnose'] == '' or data['right_diagnose'] is None) else data[
                     'right_diagnose'])  # 右眼

    # 诊断发现下的左眼
    left_eye = '左眼:'
    left_eye_height = right_eye_height - 25
    left_eye_width = 20
    c.drawString(left_eye_width, left_eye_height, left_eye)  # 左眼
    c.drawString(left_eye_width + 35, left_eye_height,
                 '无' if (data['left_diagnose'] == '' or data['left_diagnose'] is None) else data['left_diagnose'])  # 左眼
    # 建议
    c.setFont('song', 15)
    suggestion = '建议:'
    suggestion_height = left_eye_height - 40
    suggestion_width = 20
    # if data['other_advice']:
    #     other_advice = data['other_advice']
    # else:
    #     other_advice = ''
    #
    # if data['other_advice'] == '无':
    #     other_advice = ''

    c.drawString(suggestion_width, suggestion_height, suggestion)  # 建议
    c.setFont('song', 12)
    try:
        review_time = data['review_time']
    except Exception as e:
        print(e)
        review_time = ''
    print('意思', data['diagnose_advice'], review_time)
    if review_time:
        print(data['diagnose_advice'], review_time)
        diagnose_advice = '建议' + data['review_time'] + '前复诊'
        c.drawString(suggestion_width, suggestion_height - 25, diagnose_advice)  # 建议
    else:
        c.drawString(suggestion_width, suggestion_height - 25, data['diagnose_advice'])  # 建议
    # 再画条线
    line_height = suggestion_height - 50  # 建议下方的横线
    c.line(0, line_height, width, line_height)
    # 医院
    hospital = '医院:'
    hospital_height = line_height - 25
    hospital_width = 20
    if report_type != 0:  # 如果报告类型不是AI报告，则会添加医院信息
        if data['hospital']:
            hospital_name = data['hospital']
        else:
            hospital_name = 'xx社区'
        c.drawString(hospital_width, hospital_height, hospital)  # 医院
        c.drawString(hospital_width + 28, hospital_height, hospital_name)  # 医院

    # 医生
    # doctor = '医生(签字):'
    doctor = '医生:'
    doctor_height = hospital_height
    # doctor_width = 440
    doctor_width = 505
    # c.drawString(doctor_width, doctor_height, doctor)  # 医生

    signature = data['doctor_name']
    # if signature:
    #     c.drawString(doctor_width + 30, doctor_height, signature)  # 医生姓名
    # c.drawString(doctor_width+60, doctor_height, signature)  # 医生姓名

    # 放置二维码
    code_jpg = settings.BASE_DIR + '/media/image/code.jpg'
    code_jpg_width = max_square_width + 20
    code_jpg_height = suggestion_height - 30
    c.drawImage(code_jpg, code_jpg_width, code_jpg_height, height=50, width=50)  # 200 270

    # 放置logo
    logo = settings.BASE_DIR + '/media/image/' + data['database'] + '_logo.jpg'
    if os.path.exists(logo) and report_type != 0:  # 如果存在logo并且报告类型不是AI报告，则会添加logo
        if data['database'] == 'ay2fy':
            c.drawImage(logo, x_point + 220, y_point - 10, height=30, width=120)  # 200 270
        else:
            c.drawImage(logo, x_point + 250, y_point - 5, height=20, width=90)  # 200 270

    # 温馨提示
    c.setFont('song', 10)
    tips = '*该诊断报告只提供参考性建议，请勿将该报告作为对您健康状况的最终结论。'
    tips_height = height - 780  # height:为A4纸的高度
    tips_width = 10
    c.drawString(tips_width, tips_height, tips)  # 温馨提示
    if data['report_module'] == 'module2':
        if '糖尿病' in data['left_diagnose'] or '糖尿病' in data['right_diagnose']:
            c.showPage()
            tw1 = settings.BASE_DIR + '/media/image/tw_01.png'
            c.drawImage(tw1, 0, 0, height=height, width=width)
            c.showPage()
            tw2 = settings.BASE_DIR + '/media/image/tw_02.png'
            c.drawImage(tw2, 0, 0, height=height, width=width)
        if '豹纹' in data['left_diagnose'] or '豹纹' in data['right_diagnose']:
            c.showPage()
            bw = settings.BASE_DIR + '/media/image/bw_01.png'
            c.drawImage(bw, 0, 0, height=height, width=width)
    c.save()


# 这是微清专用
def create_pdf2(data):
    diseases_dict = read_xml(settings.BASE_DIR + '/media/xml_file/diseases.xml')
    dir = settings.BASE_DIR + "/media/patient_pdf/" + data['database']
    mkdir(dir)
    pdf_name = dir + '/' + data['patient_name'].strip() + '_' + data['patient_id'] + '.pdf'
    pdfmetrics.registerFont(TTFont('msyh', font_position))
    pdfmetrics.registerFont(TTFont('msyh-bold', bold_font_position))
    c = canvas.Canvas(pdf_name)
    width, height = A4
    subtitle = "眼底检查风险评估报告"
    title = "Null"
    title_len = len(title) / 3
    subtitle_len = len(subtitle)
    print('len(subtitle)', len(subtitle))
    title_size = 20
    subtitle_size = 15
    left_img_exist = False
    right_img_exist = False
    left_dr = False
    right_dr = False
    left_pm = False
    right_pm = False
    left_rm = False
    right_rm = False
    left_warning = False
    right_warning = False
    tw = False
    blxjs = False
    bwzyd = False

    if data['left_dr'] or data['right_dr']:
        tw = True
    if data['left_pm'] or data['right_pm']:
        blxjs = True
    if data['left_rm'] or data['right_rm']:
        bwzyd = True

    if data['left_dr']:
        left_dr = True
    if data['right_dr']:
        right_dr = True
    if data['left_pm']:
        left_pm = True
    if data['right_pm']:
        right_pm = True
    if data['left_rm']:
        left_rm = True
    if data['right_rm']:
        right_rm = True
    if data['left_warning']:
        left_warning = True
    if data['right_warning']:
        right_warning = True

    # 写了一个小标题
    c.setFont('msyh', subtitle_size)
    x_point = width / 2 - (subtitle_len * subtitle_size) / 2
    y_point = height - 1.5 * subtitle_size - 10
    c.drawString(x_point, y_point, subtitle)

    # 放置logo
    logo = settings.BASE_DIR + '/media/image/' + data['database'] + '_logo.jpg'
    wq_logo = settings.BASE_DIR + '/media/image/wqyl_logo.jpg'
    if os.path.exists(logo):
        c.drawImage(logo, x_point + 240, y_point - 5, height=20, width=90)  # 200 270
    elif data['is_staff'] == 1:
        c.drawImage(wq_logo, x_point + 240, y_point - 5, height=20, width=90)  # 200 270

    # 画了一条分割线
    c.line(0, y_point - 1.5 * subtitle_size, width, y_point - 1.5 * subtitle_size)

    name = '姓名:'
    gender = '性别:'
    age = '年龄:'
    diagnose_date = '日期:'
    statement = '眼底采集设备：微清医疗FC系列'
    if data['diagnose_time']:
        diagnose_time = data['diagnose_time']
    else:
        diagnose_time = ' '
    basic_info_height = y_point - 1.5 * subtitle_size - 10  # 分割线高度
    name_height = y_point - 1.5 * subtitle_size - 20
    name_width = 20
    gender_height = y_point - 1.5 * subtitle_size - 20
    gender_width = 160
    age_height = y_point - 1.5 * subtitle_size - 20
    age_width = 300
    diagnose_date_height = y_point - 1.5 * subtitle_size - 20
    diagnose_date_width = 440

    c.drawString(name_width - 8, name_height, name)  # 姓名
    patient_name = data['patient_name']
    if len(patient_name) > 5:
        c.setFont('msyh', 10)
    c.drawString(name_width + 27, name_height, patient_name)  # 姓名

    c.setFont('msyh', 15)
    c.drawString(gender_width - 10, gender_height, gender)  # 性别
    if data['patient_gender'] == 0:
        patient_gender = '男'
    else:
        patient_gender = '女'
    c.drawString(gender_width + 25, gender_height, patient_gender)  # 性别

    c.drawString(age_width - 10, age_height, age)  # 年龄
    patient_age = str(data['patient_age'])
    c.drawString(age_width + 25, age_height, patient_age)  # 年龄

    c.drawString(diagnose_date_width - 17, diagnose_date_height, diagnose_date)  # 日期
    c.setFont('msyh', 15)
    c.drawString(diagnose_date_width + 18, diagnose_date_height, diagnose_time)  # 日期

    # 微清说明
    c.drawString(name_width - 8, basic_info_height - 1.5 * subtitle_size - 10, statement)
    basic_info_height = basic_info_height - 20

    # 画了一条分割线
    c.line(0, basic_info_height - 1.5 * subtitle_size, width, basic_info_height - 1.5 * subtitle_size)

    # OD OS标志位置 (A4纸 宽595 高841)
    c.setFont('msyh', 15)
    od_os_height = basic_info_height - 1.5 * subtitle_size - 20
    od_width = 125
    os_width = width - 125 - 60
    single_pic_width = width / 2 - 30
    OD = 'OD(右眼)'
    OS = 'OS(左眼)'

    # 眼部照片位置
    picture_height = od_os_height - 210  # 眼底照片底部位置
    right_picture_width = 20

    left_picture_width = width - 270 - 20

    single_picture_width = width / 2 - 135

    right_origin_src = data['right_origin_src']
    left_origin_src = data['left_origin_src']
    right_output_file = right_origin_src
    left_output_file = left_origin_src
    left_origin_format = os.path.splitext(left_output_file)[-1]
    right_origin_format = os.path.splitext(right_output_file)[-1]

    left_pdf_jpg = data['patient_id'] + '_left_pdf' + left_origin_format

    right_pdf_jpg = data['patient_id'] + '_right_pdf' + right_origin_format

    if 'noimg' in left_origin_src:
        right_img_exist = True
        retention_tag(right_output_file, right_pdf_jpg)
        c.drawString(single_pic_width, od_os_height, OD)
        c.drawImage(right_pdf_jpg, single_picture_width, picture_height, height=200, width=270)  # 150 200
        os.remove(right_pdf_jpg)
    elif 'noimg' in right_origin_src:
        left_img_exist = True
        retention_tag(left_output_file, left_pdf_jpg)
        c.drawString(single_pic_width, od_os_height, OS)
        c.drawImage(left_pdf_jpg, single_picture_width, picture_height, height=200, width=270)  # 150 200
        os.remove(left_pdf_jpg)
    else:
        left_img_exist = True
        right_img_exist = True
        retention_tag(right_output_file, right_pdf_jpg)
        c.drawImage(right_pdf_jpg, right_picture_width, picture_height, height=200, width=270)  # 150 200
        retention_tag(left_output_file, left_pdf_jpg)
        c.drawImage(left_pdf_jpg, left_picture_width, picture_height, height=200, width=270)  # 200 270
        c.drawString(od_width, od_os_height, OD)  # 右眼OD
        c.drawString(os_width, od_os_height, OS)  # 左眼OS
        os.remove(left_pdf_jpg)
        os.remove(right_pdf_jpg)

    # 眼底照片下方画了一条分割线
    c.line(0, picture_height - 20, width, picture_height - 20)

    # 三高并发症标题
    c.setFont('msyh-bold', 15)
    sensation = '三高眼底并发症:'
    sensation_height = picture_height - 40
    sensation_width = 20
    c.drawString(sensation_width, sensation_height, sensation)

    # 糖尿病视网膜病变标题
    dr = '糖尿病视网膜病变'
    dr_height = picture_height - 70
    dr_width = 30

    # 左右眼是否病变

    b = 0
    if not tw:
        c.setFont('msyh', 13)
        dr_right, dr_left = get_result(left_img_exist, right_img_exist, left_dr, right_dr, left_warning, right_warning)
    else:
        b = b + 1
        c.setFont('msyh-bold', 13)
        dr_right, dr_left = get_result(left_img_exist, right_img_exist, left_dr, right_dr, left_warning, right_warning)

    dr_result_width = dr_width + 200
    c.drawString(dr_width, dr_height, dr)
    if '异 常' in dr_right:
        c.setFont('msyh-bold', 13)
    else:
        c.setFont('msyh', 13)

    c.drawString(dr_result_width + 5, dr_height, dr_right)

    if '异 常' in dr_left:
        c.setFont('msyh-bold', 13)
    else:
        c.setFont('msyh', 13)
    c.drawString(dr_result_width + 185, dr_height, dr_left)

    # 近视眼并发症标题
    c.setFont('msyh-bold', 15)
    myopia = '近视眼底并发症:'
    myopia_height = dr_height - 30
    myopia_width = 20
    c.drawString(myopia_width, myopia_height, myopia)

    # 病理性近视标题
    pm = '病理性近视'
    pm_height = myopia_height - 30
    pm_width = 30

    if not blxjs:
        c.setFont('msyh', 13)
        pm_right, pm_left = get_result(left_img_exist, right_img_exist, left_pm, right_pm, left_warning, right_warning)
    else:
        b = b + 1
        c.setFont('msyh-bold', 13)
        pm_right, pm_left = get_result(left_img_exist, right_img_exist, left_pm, right_pm, left_warning, right_warning)

    c.drawString(pm_width, pm_height, pm)
    if '异 常' in pm_right:
        c.setFont('msyh-bold', 13)
    else:
        c.setFont('msyh', 13)
    c.drawString(dr_result_width + 5, pm_height, pm_right)

    if '异 常' in pm_left:
        c.setFont('msyh-bold', 13)
    else:
        c.setFont('msyh', 13)
    c.drawString(dr_result_width + 185, pm_height, pm_left)

    # 豹纹状眼底标题
    tr = '豹纹状眼底'
    tr_height = pm_height - 30
    tr_width = 30

    if not bwzyd:
        c.setFont('msyh', 13)
        tr_right, tr_left = get_result(left_img_exist, right_img_exist, left_rm, right_rm, left_warning, right_warning)
    else:
        b = b + 1
        c.setFont('msyh-bold', 13)
        tr_right, tr_left = get_result(left_img_exist, right_img_exist, left_rm, right_rm, left_warning, right_warning)

    c.drawString(tr_width, tr_height, tr)

    if '异 常' in tr_right:
        c.setFont('msyh-bold', 13)
    else:
        c.setFont('msyh', 13)
    c.drawString(dr_result_width + 5, tr_height, tr_right)

    if '异 常' in tr_left:
        c.setFont('msyh-bold', 13)
    else:
        c.setFont('msyh', 13)
    c.drawString(dr_result_width + 185, tr_height, tr_left)

    # 豹纹状眼底下方画了一条分割线
    c.line(0, tr_height - 10, width, tr_height - 10)

    c.setFont('msyh-bold', 15)
    subnormal_title = '异常项(' + str(b) + '):'
    # subnormal_height = 4.6 * inch
    subnormal_height = tr_height - 30
    subnormal_width = 0.25 * inch
    c.drawString(subnormal_width, subnormal_height, subnormal_title)

    styleSheet = getSampleStyleSheet()
    style = styleSheet['BodyText']

    style.fontName = 'msyh'
    style.fontSize = 11
    # 设置行距
    style.leading = 15
    # 首行缩进
    style.firstLineIndent = 22

    if tw:
        c.setFont('msyh-bold', 13)
        dr_title = '糖尿病视网膜病变'
        subnormal_height = subnormal_height - 20
        dr_title_width = subnormal_width
        c.drawString(dr_title_width, subnormal_height, dr_title)
        dr_pa = Paragraph(
            diseases_dict['dr'], style)
        dr_pa.wrapOn(c, 7.8 * inch, 10 * inch)
        subnormal_height = subnormal_height - 70
        dr_pa.drawOn(c, 0.25 * inch, subnormal_height)

    if blxjs:
        c.setFont('msyh-bold', 13)
        pm_title = '病理性近视'
        subnormal_height = subnormal_height - 20
        pm_title_width = 0.25 * inch
        c.drawString(pm_title_width, subnormal_height, pm_title)

        pm_pa = Paragraph(
            diseases_dict['pm'], style)
        pm_pa.wrapOn(c, 7.8 * inch, 10 * inch)
        subnormal_height = subnormal_height - 40
        pm_pa.drawOn(c, 0.25 * inch, subnormal_height)

    if bwzyd:
        c.setFont('msyh-bold', 13)
        tr_title = '豹纹状眼底'
        subnormal_height = subnormal_height - 20
        tr_title_width = 0.25 * inch
        c.drawString(tr_title_width, subnormal_height, tr_title)

        tr_pa = Paragraph(
            diseases_dict['tr'], style)
        tr_pa.wrapOn(c, 7.8 * inch, 10 * inch)
        subnormal_height = subnormal_height - 40
        tr_pa.drawOn(c, 0.25 * inch, subnormal_height)

    c.setFont('msyh-bold', 15)
    tr_title = '建议:'
    subnormal_height = subnormal_height - 20
    tr_title_width = 0.25 * inch
    c.drawString(tr_title_width, subnormal_height, tr_title)

    if tw:
        c.setFont('msyh-bold', 13)
        tr_title = '糖尿病视网膜病变'
        subnormal_height = subnormal_height - 20
        tr_title_width = 0.25 * inch
        c.drawString(tr_title_width, subnormal_height, tr_title)
        Pa = Paragraph(
            diseases_dict['dr_suggestion'], style)
        subnormal_height = subnormal_height - 20
        Pa.wrapOn(c, 7.8 * inch, 10 * inch)
        Pa.drawOn(c, 0.25 * inch, subnormal_height)

    if blxjs:
        c.setFont('msyh-bold', 13)
        tr_title = '病理性近视'
        subnormal_height = subnormal_height - 20
        tr_title_width = 0.25 * inch
        c.drawString(tr_title_width, subnormal_height, tr_title)

        Pa = Paragraph(
            diseases_dict['pm_suggestion'], style)
        subnormal_height = subnormal_height - 20
        Pa.wrapOn(c, 7.8 * inch, 10 * inch)
        Pa.drawOn(c, 0.25 * inch, subnormal_height)

    if bwzyd:
        c.setFont('msyh-bold', 13)
        tr_title = '豹纹状眼底'
        subnormal_height = subnormal_height - 20
        tr_title_width = 0.25 * inch
        c.drawString(tr_title_width, subnormal_height, tr_title)

        Pa = Paragraph(
            diseases_dict['tr_suggestion'], style)
        subnormal_height = subnormal_height - 20
        Pa.wrapOn(c, 7.8 * inch, 10 * inch)
        Pa.drawOn(c, 0.25 * inch, subnormal_height)

    if b == 0:
        if left_warning and right_warning:
            diagnose_result = '重新拍摄眼底照片'
        elif not left_img_exist and right_warning:
            diagnose_result = '重新拍摄眼底照片'
        elif not right_img_exist and left_warning:
            diagnose_result = '重新拍摄眼底照片'
        else:
            diagnose_result = '未检测出糖网、豹纹状眼底和病理性近视'
        subnormal_height = subnormal_height - 20
        Pa = Paragraph(
            diagnose_result, style)
        Pa.wrapOn(c, 7.8 * inch, 10 * inch)
        Pa.drawOn(c, 0.25 * inch, subnormal_height)

    if b > 2:
        c.showPage()
        Pa = Paragraph(
            diseases_dict['tr_suggestion'], style)
        subnormal_height = height - 20
        Pa.wrapOn(c, 7.8 * inch, 10 * inch)
        Pa.drawOn(c, 0.25 * inch, subnormal_height)

    # 眼底照片下方画了一条分割线
    subnormal_height = subnormal_height - 20
    c.line(0, subnormal_height, width, subnormal_height)

    # 免责声明
    subnormal_height = subnormal_height - 20
    style.fontSize = 10
    statement = '*以上评估结果均以上传图像为依据，仅供参考。不涉及任何形式的诊断和治疗内容，亦不包括任何形式的用药建议'
    Pa = Paragraph(statement, style)
    subnormal_height = subnormal_height - 10
    Pa.wrapOn(c, 7.8 * inch, 10 * inch)
    Pa.drawOn(c, 0.25 * inch, subnormal_height)

    # statement_orbis = '*软件技术支持：合肥奥比斯科技'
    # Pa_w = Paragraph(statement_weiqing, style)
    # Pa_o = Paragraph(statement_orbis, style)
    # orbis_height = subnormal_height - 15
    # weiqing_height = orbis_height - 15
    # Pa_w.wrapOn(c, 7.8 * inch, 10 * inch)
    # Pa_w.drawOn(c, 0.25 * inch, weiqing_height)
    # Pa_o.wrapOn(c, 7.8 * inch, 10 * inch)
    # Pa_o.drawOn(c, 0.25 * inch, orbis_height)
    if tw:
        c.showPage()
        tw1 = settings.BASE_DIR + '/media/image/tw_01.png'
        c.drawImage(tw1, 0, 0, height=height, width=width)
        c.showPage()
        tw2 = settings.BASE_DIR + '/media/image/tw_02.png'
        c.drawImage(tw2, 0, 0, height=height, width=width)
    if bwzyd:
        c.showPage()
        bw = settings.BASE_DIR + '/media/image/bw_01.png'
        c.drawImage(bw, 0, 0, height=height, width=width)
    c.save()


class PdfMaker:
    def __init__(self, data):
        self.data = data
        self.dir = settings.BASE_DIR + "/media/patient_pdf/" + data['database']
        self.pdf_name = self.dir + '/' + data['patient_name'].strip() + '_' + str(data['pk_patient_id']) + '.pdf'
        self.width, self.height = A4

    def wrap_text(self, c, font, font_size, text, x1, y1, x2, y2):
        '''

        :param c: canvas
        :param font: 字体
        :param font_size: 字体大小
        :param text: 文本
        :param x1: 决定文本卷曲的位置，越大卷曲的位置越长
        :param y1: 决定不了什么
        :param x2: 决定文字的横向位置，越大离左边越远
        :param y2: 决定文字纵向的位置，越大离下边越远
        :return:
        '''
        styleSheet = getSampleStyleSheet()
        style = styleSheet['BodyText']
        style.fontName = font
        style.fontSize = font_size
        # 设置行距
        style.leading = 15
        # 首行缩进
        style.firstLineIndent = 0
        Pa = Paragraph(text, style)
        Pa.wrapOn(c, x1 * inch, y1 * inch)
        Pa.drawOn(c, x2 * inch, y2 * inch)

    @staticmethod
    def cut_text(text, length):
        textArr = re.findall('.{' + str(length) + '}', text)
        textArr.append(text[(len(textArr) * length):])
        return textArr

    @staticmethod
    def draw_text():
        style = getSampleStyleSheet()

        # 常规字体(非粗体或斜体)

        ct = style['Normal']

        # 使用的字体s

        ct.fontName = 'font_style9'

        ct.fontSize = 14

        # 设置自动换行

        ct.wordWrap = 'CJK'

        # 居左对齐

        ct.alignment = 0

        # 第一行开头空格

        ct.firstLineIndent = 32

        # 设置行距

        ct.leading = 30

        text = Paragraph(
            '程序员，是互联网、移动互联网和即将到来的物联网时期的弄潮儿。这群特立独行的人才，不知平时最喜欢什么?他们的兴趣真想让人一探究竟。经过七七49天的调研，终于形成了一份不具备权威性的统计报告，现公布给大家。', ct)

        return text

    def create_pdf(self):
        data = self.data
        patient_id = str(data['patient_id'])
        report_type = 3  # 由此得知报告类型是AI报告还是非AI报告，0代表AI报告
        if 'reportType' in data:
            report_type = data['reportType']
        dir = settings.BASE_DIR + "/media/patient_pdf/" + data['database']
        mkdir(dir)
        pdf_name = dir + '/' + data['patient_name'].strip() + '_' + patient_id + '.pdf'
        reportlab.pdfbase.pdfmetrics.registerFont(
            reportlab.pdfbase.ttfonts.TTFont('song', font_position))  # 注册字体
        c = canvas.Canvas(pdf_name)
        width, height = A4
        print('width,height', width, height)
        # title and subtitle
        subtitle = "眼底检查报告"
        title = "合肥高新区天乐社区卫生服务中心"
        title_len = len(title) / 3
        subtitle_len = len(subtitle)
        print('len(subtitle)', len(subtitle))
        title_size = 20
        subtitle_size = 15

        # 写了一个小标题
        c.setFont('song', subtitle_size)
        x_point = width / 2 - (subtitle_len * subtitle_size) / 2
        y_point = height - 1.5 * subtitle_size - 10
        c.drawString(x_point, y_point, subtitle)

        # 画了一条分割线
        c.line(0, y_point - 1.5 * subtitle_size, width, y_point - 1.5 * subtitle_size)

        name = '姓名:'
        gender = '性别:'
        age = '年龄:'
        diagnose_date = '日期:'
        print('data[diagnose_time]', data['diagnose_time'])
        if data['diagnose_time']:
            diagnose_time = data['diagnose_time']
        else:
            diagnose_time = ' '
        basic_info_height = y_point - 1.5 * subtitle_size - 10  # 分割线高度
        name_height = y_point - 1.5 * subtitle_size - 20
        name_width = 20
        gender_height = y_point - 1.5 * subtitle_size - 20
        gender_width = 160
        age_height = y_point - 1.5 * subtitle_size - 20
        age_width = 300
        diagnose_date_height = y_point - 1.5 * subtitle_size - 20
        diagnose_date_width = 440

        c.drawString(name_width - 8, name_height, name)  # 姓名
        patient_name = data['patient_name']
        if len(patient_name) > 5:
            c.setFont('song', 10)
        c.drawString(name_width + 27, name_height, patient_name)  # 姓名

        c.setFont('song', 15)
        c.drawString(gender_width - 10, gender_height, gender)  # 性别
        if data['patient_gender'] == '0':
            patient_gender = '男'
        else:
            patient_gender = '女'
        c.drawString(gender_width + 25, gender_height, patient_gender)  # 性别

        c.drawString(age_width - 10, age_height, age)  # 年龄
        patient_age = str(data['patient_age'])
        c.drawString(age_width + 25, age_height, patient_age)  # 年龄

        c.drawString(diagnose_date_width - 17, diagnose_date_height, diagnose_date)  # 日期
        c.setFont('song', 15)
        c.drawString(diagnose_date_width + 18, diagnose_date_height, diagnose_time)  # 日期

        # 画了一条分割线
        c.line(0, basic_info_height - 1.5 * subtitle_size, width, basic_info_height - 1.5 * subtitle_size)

        # OD OS标志位置 (A4纸 宽595 高841)
        c.setFont('song', 15)
        od_os_height = basic_info_height - 1.5 * subtitle_size - 20
        od_width = 270
        os_width = 270
        left_iqa_score = str(data['left_iqa_score'])
        right_iqa_score = str(data['right_iqa_score'])
        # OD = 'OD(图像质量:'+right_iqa_score+')'
        # OS = 'OS(图像质量:'+left_iqa_score+')'
        OD = 'OD(右眼)'
        OS = 'OS(左眼)'
        c.drawString(od_width + 150, od_os_height - 20, OS)  # 左眼OS
        c.drawString(os_width - 150, od_os_height - 20, OD)  # 右眼OD

        # 眼部照片位置
        picture_height = od_os_height - 210  # 眼底照片底部位置
        left_picture_width = 160
        right_picture_width = 160
        right_output_file = data['right_origin_src']
        left_output_file = data['left_origin_src']
        left_origin_format = os.path.splitext(left_output_file)[-1]
        right_origin_format = os.path.splitext(right_output_file)[-1]

        left_pdf_jpg = settings.BASE_DIR + \
                       "/media/patient_img/" + patient_id + '_left_pdf' + left_origin_format

        right_pdf_jpg = settings.BASE_DIR + \
                        "/media/patient_img/" + patient_id + '_right_pdf' + right_origin_format

        retention_tag(left_output_file, left_pdf_jpg)
        c.drawImage(left_pdf_jpg, right_picture_width + 150, picture_height - 20, height=200, width=270)  # 200 270

        retention_tag(right_output_file, right_pdf_jpg)
        c.drawImage(right_pdf_jpg, left_picture_width - 150, picture_height - 20, height=200, width=270)  # 150 200

        os.remove(left_pdf_jpg)
        os.remove(right_pdf_jpg)

        # AI照片位置
        AIpicture_height = picture_height - 20  # 眼底照片底部位置
        # 先画条线
        line_height = AIpicture_height - 30  # 照片顶端位置加上照片长度再向下偏移20
        print('picture_height', picture_height, basic_info_height - 1.5 * subtitle_size)
        c.line(0, line_height, width, line_height)

        # 影像发现位置
        find = '影像所见:'
        find_height = line_height - 35
        c.drawString(20, find_height, find)  # 类别

        find_height = find_height - 25

        # 影像发现下的右眼
        c.setFont('song', 12)
        right_eye = '右眼:'
        right_des_height = line_height - 60
        right_eye_width = 20
        c.drawString(right_eye_width, right_des_height, right_eye)  # 右眼
        c.drawString(right_eye_width + 35, right_des_height,
                     '无' if (data['right_desc'] == '' or data['right_desc'] is None) else data[
                         'right_desc'])  # 右眼

        # 影像发现下的左眼
        left_eye = '左眼:'
        left_des_height = right_des_height - 25
        left_eye_width = 20
        c.drawString(left_eye_width, left_des_height, left_eye)  # 左眼
        c.drawString(left_eye_width + 35, left_des_height,
                     '无' if (data['left_desc'] == '' or data['left_desc'] is None) else data['left_desc'])  # 左眼
        # 建议

        # 类别
        # type = '类别'
        # c.setFont('song', 12)
        type_height = find_height - 20
        # type_width = 20
        # c.drawString(type_width, type_height, type)  # 类别
        # amount = '数量(个)'
        # c.setFont('song', 12)

        square = '总面积mm'
        c.setFont('song', 12)
        square_height = type_height
        square_width = 320

        max_square = '最大面积mm'
        c.setFont('song', 12)
        max_square_height = type_height
        max_square_width = 480
        # 出血
        blood = '出血'
        blood_height = type_height - 20
        blood_width = 20
        # c.drawString(blood_width, blood_height, blood)  # 出血

        # 渗出
        ooze = '渗出'
        ooze_height = blood_height - 20
        ooze_width = 20
        # c.drawString(ooze_width, ooze_height, ooze)  # 渗出

        # # 影像发现下的右眼
        left_eye_height = blood_height
        # 诊断
        c.setFont('song', 15)
        sensation = '初步印象:'
        sensation_height = left_eye_height - 20
        sensation_width = 20
        c.drawString(sensation_width, sensation_height, sensation)  # 诊断

        # 诊断发现下的右眼
        c.setFont('song', 12)
        right_eye = '右眼:'
        right_eye_height = sensation_height - 25
        right_eye_width = 20
        c.drawString(right_eye_width, right_eye_height, right_eye)  # 右眼
        c.drawString(right_eye_width + 35, right_eye_height,
                     '无' if (data['right_diagnose'] == '' or data['right_diagnose'] is None) else data[
                         'right_diagnose'])  # 右眼

        # 诊断发现下的左眼
        left_eye = '左眼:'
        left_eye_height = right_eye_height - 25
        left_eye_width = 20
        c.drawString(left_eye_width, left_eye_height, left_eye)  # 左眼
        c.drawString(left_eye_width + 35, left_eye_height,
                     '无' if (data['left_diagnose'] == '' or data['left_diagnose'] is None) else data[
                         'left_diagnose'])  # 左眼
        # 建议
        c.setFont('song', 15)
        suggestion = '建议:'
        suggestion_height = left_eye_height - 40
        suggestion_width = 20
        # if data['other_advice']:
        #     other_advice = data['other_advice']
        # else:
        #     other_advice = ''
        #
        # if data['other_advice'] == '无':
        #     other_advice = ''

        c.drawString(suggestion_width, suggestion_height, suggestion)  # 建议
        c.setFont('song', 12)
        try:
            review_time = data['review_time']
        except Exception as e:
            print(e)
            review_time = ''
        print('意思', data['diagnose_advice'], review_time)
        if review_time:
            print(data['diagnose_advice'], review_time)
            diagnose_advice = '建议' + data['review_time'] + '前复诊'
            c.drawString(suggestion_width, suggestion_height - 25, diagnose_advice)  # 建议
        else:
            c.drawString(suggestion_width, suggestion_height - 25, data['diagnose_advice'])  # 建议
        # 再画条线
        line_height = suggestion_height - 50  # 建议下方的横线
        c.line(0, line_height, width, line_height)
        # 医院
        hospital = '医院:'
        hospital_height = line_height - 25
        hospital_width = 20
        if report_type != 0:  # 如果报告类型不是AI报告，则会添加医院信息
            if data['hospital']:
                hospital_name = data['hospital']
            else:
                hospital_name = 'xx社区'
            c.drawString(hospital_width, hospital_height, hospital)  # 医院
            c.drawString(hospital_width + 28, hospital_height, hospital_name)  # 医院

        # 医生
        # doctor = '医生(签字):'
        doctor = '医生:'
        doctor_height = hospital_height
        # doctor_width = 440
        doctor_width = 505
        # c.drawString(doctor_width, doctor_height, doctor)  # 医生

        signature = data['doctor_name']
        # if signature:
        #     c.drawString(doctor_width + 30, doctor_height, signature)  # 医生姓名
        # c.drawString(doctor_width+60, doctor_height, signature)  # 医生姓名

        # 放置二维码
        code_jpg = settings.BASE_DIR + '/media/image/code.jpg'
        code_jpg_width = max_square_width + 20
        code_jpg_height = suggestion_height - 30
        c.drawImage(code_jpg, code_jpg_width, code_jpg_height, height=50, width=50)  # 200 270

        # 放置logo
        logo = settings.BASE_DIR + '/media/image/' + data['database'] + '_logo.jpg'
        if os.path.exists(logo) and report_type != 0:  # 如果存在logo并且报告类型不是AI报告，则会添加logo
            if data['database'] == 'ay2fy':
                c.drawImage(logo, x_point + 220, y_point - 10, height=30, width=120)  # 200 270
            else:
                c.drawImage(logo, x_point + 250, y_point - 5, height=20, width=90)  # 200 270

        # 温馨提示
        c.setFont('song', 10)
        tips = '*该诊断报告只提供参考性建议，请勿将该报告作为对您健康状况的最终结论。'
        tips_height = height - 780  # height:为A4纸的高度
        tips_width = 10
        c.drawString(tips_width, tips_height, tips)  # 温馨提示
        if data['report_module'] == 'module2':
            if '糖尿病' in data['left_diagnose'] or '糖尿病' in data['right_diagnose']:
                c.showPage()
                tw1 = settings.BASE_DIR + '/media/image/tw_01.png'
                c.drawImage(tw1, 0, 0, height=height, width=width)
                c.showPage()
                tw2 = settings.BASE_DIR + '/media/image/tw_02.png'
                c.drawImage(tw2, 0, 0, height=height, width=width)
            if '豹纹' in data['left_diagnose'] or '豹纹' in data['right_diagnose']:
                c.showPage()
                bw = settings.BASE_DIR + '/media/image/bw_01.png'
                c.drawImage(bw, 0, 0, height=height, width=width)
        c.save()

    def create_pdf3(self):
        data = self.data
        mkdir(self.dir)
        pdfmetrics.registerFont(TTFont('msyh', font_position))
        pdfmetrics.registerFont(TTFont('msyh-bold', bold_font_position))
        pdfmetrics.registerFont(TTFont('font_style9', font_style9))
        patient_id = str(data['pk_patient_id'])

        create_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

        if 'patient_count' in data:
            patient_count = str(data['patient_count'])
            pdf_name = self.dir + '/' + data['patient_name'].strip() + '_' + str(patient_id) + '_' + str(
                patient_count) + '_' + create_time + '_' + '.pdf'
        else:
            patient_count = patient_id
            pdf_name = self.dir + '/' + data['patient_name'].strip() + '_' + str(patient_id) \
                       + '_' + create_time + '_' + '.pdf'

        c = canvas.Canvas(pdf_name)
        # check_num = PatientInfo.objects.filter(patient_id=data['patient_id'])[0].check_num
        print(data)
        check_num = data['check_num']
        # title and subtitle
        subtitle = "新生儿眼底筛查报告单"
        if data['report_title']:
            title = data['report_title']
        else:
            title = "安徽妇幼保健医院"
        title_len = len(title)
        subtitle_len = len(subtitle)
        title_size = 13
        subtitle_size = 12

        id = '筛查编号:'
        num = '检查单号:'

        # 大标题位置
        c.setFont('msyh-bold', title_size)
        x_point = self.width / 2 - (title_len * title_size) / 2
        y_point = self.height - 1.5 * title_size - 10
        c.drawString(x_point, y_point, title)

        # 小标题位置
        c.setFont('msyh-bold', subtitle_size)
        x_point = self.width / 2 - (subtitle_len * subtitle_size) / 2
        y_point = self.height - 1.5 * title_size - 30
        c.drawString(x_point, y_point, subtitle)

        # 画了一条分割线
        c.line(20, y_point - 1.5 * subtitle_size, self.width - 20, y_point - 1.5 * subtitle_size)

        basic_info_height = y_point - 1.5 * subtitle_size - 10  # 分割线高度

        id_height = y_point - 1.5 * subtitle_size - 15
        id_width = 20

        num_width = self.width / 2 - id_width

        c.setFont('font_style9', 10)

        # 筛查编号位置
        c.drawString(id_width, id_height, id)  # 筛查编号
        # c.drawString(id_width + 50, id_height, patient_id)  # 筛查编号
        c.drawString(id_width + 50, id_height, patient_count)  # 筛查编号

        # 检查单号位置
        c.drawString(num_width, id_height, num)  # 检查单号
        c.drawString(num_width + 50, id_height, str(check_num))  # 检查单号

        # 姓名位置
        name_height = id_height - 15
        name_width = 20
        if 'parent_name' in data:
            patient_name = data['parent_name'] + '/' + data['patient_name']
            name = '姓名(母亲/儿童):'
            specific_name_width = name_width + 85
        else:
            patient_name = data['patient_name']
            name = '姓名:'
            specific_name_width = name_width + 27

        c.drawString(name_width, name_height, name)  # 姓名标题
        if len(patient_name) > 5:
            c.setFont('font_style9', 8)
        c.drawString(specific_name_width, name_height, patient_name)  # 具体姓名

        c.setFont('font_style9', 10)  # 将字体恢复，防止因名字过长改变字体
        # 年龄位置
        age = '年龄:'
        age_height = name_height - 15
        age_width = name_width
        c.drawString(age_width, age_height, age)  # 年龄
        print(data['patient_age'])
        patient_age = str(data['patient_age']) + '天'
        c.drawString(age_width + 35, age_height, patient_age)  # 年龄

        # 矫正孕周位置
        refine_weeks_title = '矫正孕周:'
        regine_weeks = str(data['refine_weeks']) + '周' + str(data['refine_days']) + '天'
        refine_height = age_height - 15
        refine_width = name_width
        c.drawString(refine_width, refine_height, refine_weeks_title)  # 矫正孕周标题
        c.drawString(refine_width + 50, refine_height, regine_weeks)  # 矫正孕周

        # 性别位置
        gender = '性别:'
        gender_height = name_height
        gender_width = self.width / 2 - name_width
        c.drawString(gender_width, gender_height, gender)  # 性别
        if data['patient_gender'] == 0:
            patient_gender = '男'
        else:
            patient_gender = '女'
        c.drawString(gender_width + 35, gender_height, patient_gender)  # 性别

        # 出生体重位置
        birth_weight_title = '出生体重:'
        birth_weight = str(data['birth_weight']) + '克'
        birth_weight_height = name_height - 15
        birth_weight_width = self.width / 2 - name_width
        c.drawString(birth_weight_width, birth_weight_height, birth_weight_title)  # 出生体重标题
        c.drawString(birth_weight_width + 50, birth_weight_height, birth_weight)  # 出生体重

        # 出生孕周
        birth_weeks_title = '出生孕周:'
        birth_weeks = str(data['birth_weeks']) + '周' + str(data['birth_days']) + '天'
        birth_weeks_height = name_height - 30
        birth_weeks_width = self.width / 2 - name_width
        c.drawString(birth_weeks_width, birth_weeks_height, birth_weeks_title)  # 出生孕周标题
        c.drawString(birth_weeks_width + 50, birth_weeks_height, birth_weeks)  # 出生孕周

        # 画了一条分割线
        line2_height = birth_weeks_height - 10
        c.line(20, line2_height, self.width - 20, line2_height)

        # OD OS标志位置 (A4纸 宽595 高841)
        c.setFont('font_style9', 12)
        od_os_height = line2_height - 20
        od_width = 270
        os_width = 270
        # left_iqa_score = str(data['left_iqa_score'])
        # right_iqa_score = str(data['right_iqa_score'])
        # OD = 'OD(图像质量:'+right_iqa_score+')'
        # OS = 'OS(图像质量:'+left_iqa_score+')'
        OD = 'OD(右眼)'
        OS = 'OS(左眼)'
        c.drawString(od_width + 150, od_os_height, OS)  # 左眼OS
        c.drawString(os_width - 150, od_os_height, OD)  # 右眼OD

        # 眼部照片位置
        picture_height = od_os_height - 210  # 眼底照片底部位置
        left_picture_width = 160
        right_picture_width = 160
        right_output_file = data['right_origin_src']
        left_output_file = data['left_origin_src']

        left_origin_format = os.path.splitext(left_output_file)[-1]
        right_origin_format = os.path.splitext(right_output_file)[-1]

        left_pdf_jpg = settings.BASE_DIR + \
                       "/media/patient_img/" + patient_id + '_left_pdf' + left_origin_format

        right_pdf_jpg = settings.BASE_DIR + \
                        "/media/patient_img/" + patient_id + '_right_pdf' + right_origin_format

        # retention_tag(left_output_file, left_pdf_jpg)
        # c.drawImage(left_pdf_jpg, right_picture_width + 160, picture_height - 35, height=188, width=250)  # 200 270
        c.drawImage(left_output_file, right_picture_width + 145, picture_height - 20, height=210, width=280)  # 200 270

        # retention_tag(right_output_file, right_pdf_jpg)
        # c.drawImage(right_pdf_jpg, left_picture_width - 135, picture_height - 35, height=188, width=250)  # 150 200
        c.drawImage(right_output_file, left_picture_width - 150, picture_height - 20, height=210, width=280)  # 150 200

        # os.remove(left_pdf_jpg)
        # os.remove(right_pdf_jpg)

        # AI照片位置
        AIpicture_height = picture_height - 20  # 眼底照片底部位置
        # 先画条线
        line_height = AIpicture_height - 30  # 照片顶端位置加上照片长度再向下偏移20

        c.line(20, line_height, self.width - 20, line_height)

        # 影像发现位置
        c.setFont('msyh-bold', 12)
        find = '影像所见:'
        find_height = line_height - 35
        c.drawString(20, find_height, find)  # 类别

        find_height = find_height - 25

        # 影像发现下的右眼
        c.setFont('font_style9', 12)
        right_eye = '右眼:'
        right_des_height = line_height - 60
        right_eye_width = 20
        c.drawString(right_eye_width, right_des_height, right_eye)  # 右眼
        r_y2 = 4.6
        l_y2 = 4.455
        i = 0
        if len(data['right_desc']) > 47:
            texts = self.cut_text(data['right_desc'], 47)
            right_eye_width = right_eye_width + 35
            for tx in texts:
                # c.drawString(right_eye_width, right_des_height - i*15, tx)
                i = i + 1
            if i == 0:
                r_y2 = r_y2
                l_y2 = l_y2
            elif i == 1:
                r_y2 = 4.6
                l_y2 = 3.6
            elif i == 2:
                r_y2 = 4.806
                l_y2 = 4.04
            elif i == 3:
                r_y2 = 4.6
                l_y2 = 3.63

            self.wrap_text(c, 'font_style9', 12, data['right_desc'], 7.45, 4, 0.7, r_y2)
            right_des_height = right_des_height - i * 15

        else:
            l_y2 = 4.25
            c.drawString(right_eye_width + 35, right_des_height,
                         '无' if (data['right_desc'] == '' or data['right_desc'] is None) else data[
                             'right_desc'])  # 右眼
        # 影像发现下的左眼
        left_eye = '左眼:'
        left_des_height = right_des_height - 25
        left_eye_width = 20
        c.drawString(left_eye_width, left_des_height, left_eye)  # 左眼
        j = 0
        if len(data['left_desc']) > 47:
            texts = self.cut_text(data['left_desc'], 47)
            left_eye_width = left_eye_width + 35
            for tx in texts:
                # c.drawString(left_eye_width, left_des_height - i*15, tx)
                j = j + 1

            if i == 0 and j == 2:  # 如果右眼诊断为一行且左眼为两行
                l_y2 = 4.45

            if i == 2 and j == 3:  # 如果右眼诊断为二行且左眼为三行
                l_y2 = 3.84

            if i == 3 and j == 2:  # 如果右眼诊断为二行且左眼为三行
                l_y2 = 3.835
            self.wrap_text(c, 'font_style9', 12, data['left_desc'], 7.45, 4, 0.7, l_y2)
            left_des_height = left_des_height - j * 15

        else:
            c.drawString(left_eye_width + 35, left_des_height,
                         '无' if (data['left_desc'] == '' or data['left_desc'] is None) else data['left_desc'])  # 左眼
        # 建议

        # 类别
        # type = '类别'
        # c.setFont('song', 12)
        type_height = find_height - 20
        # type_width = 20
        # c.drawString(type_width, type_height, type)  # 类别
        # amount = '数量(个)'
        # c.setFont('song', 12)

        square = '总面积mm'
        c.setFont('msyh-bold', 12)
        square_height = type_height
        square_width = 320

        max_square = '最大面积mm'
        c.setFont('msyh-bold', 12)
        max_square_height = type_height
        max_square_width = 480
        # 出血
        blood = '出血'
        blood_height = type_height - 20
        blood_width = 20
        # c.drawString(blood_width, blood_height, blood)  # 出血

        # 渗出
        ooze = '渗出'
        ooze_height = blood_height - 20
        ooze_width = 20
        # c.drawString(ooze_width, ooze_height, ooze)  # 渗出

        # # 影像发现下的左眼
        left_eye_height = left_des_height - 10
        # 诊断
        c.setFont('msyh-bold', 12)
        sensation = '初步印象:'
        sensation_height = left_eye_height - 10
        sensation_width = 20
        c.drawString(sensation_width, sensation_height, sensation)  # 诊断

        # 诊断发现下的右眼
        c.setFont('font_style9', 12)
        right_eye = '右眼:'
        right_eye_height = sensation_height - 25
        right_eye_width = 20
        c.drawString(right_eye_width, right_eye_height, right_eye)  # 右眼
        c.drawString(right_eye_width + 35, right_eye_height,
                     '无' if (data['right_diagnose'] == '' or data['right_diagnose'] is None) else data[
                         'right_diagnose'])  # 右眼

        # 诊断发现下的左眼
        left_eye = '左眼:'
        left_eye_height = right_eye_height - 25
        left_eye_width = 20
        c.drawString(left_eye_width, left_eye_height, left_eye)  # 左眼
        c.drawString(left_eye_width + 35, left_eye_height,
                     '无' if (data['left_diagnose'] == '' or data['left_diagnose'] is None) else data[
                         'left_diagnose'])  # 左眼
        # 建议
        c.setFont('msyh-bold', 12)
        suggestion = '建议:'
        # suggestion_height = left_eye_height - 40
        suggestion_height = right_eye_height - 50
        # suggestion_width = 20
        suggestion_width = 20
        # if data['other_advice']:
        #     other_advice = data['other_advice']
        # else:
        #     other_advice = ''
        #
        # if data['other_advice'] == '无':
        #     other_advice = ''

        c.drawString(suggestion_width, suggestion_height, suggestion)  # 建议
        c.setFont('font_style9', 12)
        try:
            review_time = data['review_time']
        except Exception as e:
            print(e)
            review_time = ''
        if review_time:
            diagnose_advice = '建议' + data['review_time'] + '前复诊'
            c.drawString(suggestion_width, suggestion_height - 25, diagnose_advice)  # 建议
        else:
            m = re.search("(\d{4}-\d{1,2}-\d{1,2})", data['diagnose_advice'])
            if m:
                str_date = m.group(1)
                _diagnose_advice = data['diagnose_advice'].replace('(' + str_date + ')', '')

            else:
                _diagnose_advice = data['diagnose_advice']

            c.drawString(suggestion_width, suggestion_height - 25, _diagnose_advice)  # 建议

        # 再画条线
        line_height = suggestion_height - 80  # 建议下方的横线
        c.line(20, line_height, self.width - 20, line_height)

        # 医院
        # hospital = '医院:'
        # hospital_height = line_height - 25
        # hospital_height = self.height - 745
        # hospital_width = 20

        diagnose_height = line_height + 15 - 2

        doctor_height = diagnose_height + 20

        # 医生
        # doctor = '医生(签字):'

        # doctor_height = line_height + 40 - 2
        # doctor_width = 20
        # c.drawString(self.width - 170, doctor_height, doctor)  # 医生
        doctor = '报告医师:'
        doctor_width = 20
        c.drawString(doctor_width, doctor_height, doctor)  # 医生
        c.drawString(self.width - 170, doctor_height, '审核医师:')  # 医生
        signature = data['doctor_name']

        c.drawString(doctor_width + 55, doctor_height, signature)  # 医生
        diagnose_time1 = '诊断时间:'
        diagnose_time2 = data['diagnose_time']

        c.drawString(doctor_width, diagnose_height, diagnose_time1)  # 诊断时间
        c.drawString(doctor_width + 55, diagnose_height, diagnose_time2)  # 诊断时间

        check_time2 = '-'

        check_doctor = '-'

        if 'check_time' in data:
            check_time2 = data['check_time']
            if check_time2:
                if 'check_doctor' in data:

                    check_doctor = data['check_doctor']['last_name'] + data['check_doctor']['first_name']
                    if not check_doctor:
                        check_doctor = '-'

            else:

                return self.create_pdf5()

                # check_time2 = '-'

                # check_doctor = '-'

        c.drawString(self.width - 170 + 55, doctor_height, check_doctor)  # 审核医生姓名

        c.drawString(self.width - 170, diagnose_height, '审核时间:')  # 审核时间
        c.drawString(self.width - 170 + 55, diagnose_height, check_time2)  # 审核时间

        # 放置图片
        # code_jpg = settings.BASE_DIR + '/media/image/tips6.png'
        # code_jpg_width = self.width - 20 - 50
        # code_jpg_width = diagnose_width
        # code_jpg_height = self.height - 790
        # c.drawImage(code_jpg, code_jpg_width, code_jpg_height, height=60, width=560)  # 200 270

        # 放置logo
        # logo = settings.BASE_DIR + '/media/image/' + data['database'] + '_logo.jpg'

        # 温馨提示
        c.setFont('font_style9', 7)
        tips = '本次检查结果只反映孩子目前的眼底情况。' \
               '特别是3岁以前，眼睛的结构和功能都在迅速发育，' \
               '眼底检查正常并不意味着生长发育过程中不会出现其他眼底问题。' \
               '一些发育性眼病如斜视、弱视，屈光不正等，要到一定年龄才能被发现，' \
               '定期对儿童进行眼保健检查，发现视功能异常，及时干预。'

        tips2 = '- 复查请提前三天电话预约'
        tips3 = '- 院本部 儿童眼保健门诊：周一至周五 工作时间；周六、周日 上午（节假日除外） 预约电话：0551-69118113，0551-69118289'
        tips4 = '- 院西区 儿童眼保健门诊：周一至周五工作时间（节假日除外） 预约电话：0551-62160092'
        tips5 = '- 院东区 儿童眼保健门诊：周一、周四 （节假日除外） 预约电话：0551-69118737'

        tips_height = line_height - 25  # height:横线的高度减去15
        styleSheet = getSampleStyleSheet()
        style = styleSheet['BodyText']
        style.fontName = 'font_style9'
        style.fontSize = 8
        # 设置行距
        style.leading = 10
        # 首行缩进
        style.firstLineIndent = 22
        Pa = Paragraph(tips, style)
        Pa.wrapOn(c, 7.8 * inch, 10 * inch)
        Pa.drawOn(c, 0.25 * inch, tips_height)

        style.firstLineIndent = 0  # 缩进为0

        Pa = Paragraph(tips2, style)
        Pa.wrapOn(c, 7.8 * inch, 10 * inch)
        Pa.drawOn(c, 0.25 * inch, tips_height - 15)

        Pa = Paragraph(tips3, style)
        Pa.wrapOn(c, 7.8 * inch, 10 * inch)
        Pa.drawOn(c, 0.25 * inch, tips_height - 25)

        Pa = Paragraph(tips4, style)
        Pa.wrapOn(c, 7.8 * inch, 10 * inch)
        Pa.drawOn(c, 0.25 * inch, tips_height - 35)

        Pa = Paragraph(tips5, style)
        Pa.wrapOn(c, 7.8 * inch, 10 * inch)
        Pa.drawOn(c, 0.25 * inch, tips_height - 45)

        if data['report_module'] == 'module2':
            if '糖尿病' in data['left_diagnose'] or '糖尿病' in data['right_diagnose']:
                c.showPage()
                tw1 = settings.BASE_DIR + '/media/image/tw_01.png'
                c.drawImage(tw1, 0, 0, height=self.height, width=self.width)
                c.showPage()
                tw2 = settings.BASE_DIR + '/media/image/tw_02.png'
                c.drawImage(tw2, 0, 0, height=self.height, width=self.width)
            if '豹纹' in data['left_diagnose'] or '豹纹' in data['right_diagnose']:
                c.showPage()
                bw = settings.BASE_DIR + '/media/image/bw_01.png'
                c.drawImage(bw, 0, 0, height=self.height, width=self.width)
        c.save()
        print('返回了', pdf_name)
        return pdf_name

    def create_pdf4(self):
        data = self.data
        mkdir(self.dir)
        pdfmetrics.registerFont(TTFont('msyh', font_position))
        pdfmetrics.registerFont(TTFont('msyh-bold', bold_font_position))
        # pdfmetrics.registerFont(TTFont('font_style1', font_style1))
        # pdfmetrics.registerFont(TTFont('font_style2', font_style2))
        # pdfmetrics.registerFont(TTFont('font_style3', font_style3))
        # pdfmetrics.registerFont(TTFont('font_style4', font_style4))
        # pdfmetrics.registerFont(TTFont('font_style5', font_style5))
        # pdfmetrics.registerFont(TTFont('font_style6', font_style6))
        # pdfmetrics.registerFont(TTFont('font_style7', font_style7))
        # pdfmetrics.registerFont(TTFont('font_style8', font_style8))
        pdfmetrics.registerFont(TTFont('font_style9', font_style9))
        # pdfmetrics.registerFont(TTFont('font_style10', font_style10))
        # pdfmetrics.registerFont(TTFont('font_style11', font_style11))
        patient_id = str(data['patient_id'])
        if 'patient_count' in data:
            patient_count = str(data['patient_count'])
            pdf_name = self.dir + '/' + data['patient_name'].strip() + '_' + str(patient_id) + '_' + str(
                patient_count) + '.pdf'
        else:
            patient_count = patient_id
            pdf_name = self.dir + '/' + data['patient_name'].strip() + '_' + str(patient_id) + '.pdf'
        c = canvas.Canvas(pdf_name)
        check_num = PatientInfo.objects.filter(patient_id=data['patient_id'])[0].check_num
        # title and subtitle
        subtitle = "新生儿眼底筛查报告单"
        if data['report_title']:
            title = data['report_title']
        else:
            title = "安徽妇幼保健医院"
        title_len = len(title)
        subtitle_len = len(subtitle)
        title_size = 13
        subtitle_size = 12

        id = '筛查编号:'
        num = '检查单号:'

        # 大标题位置
        c.setFont('msyh-bold', title_size)
        x_point = self.width / 2 - (title_len * title_size) / 2
        y_point = self.height - 1.5 * title_size - 10
        c.drawString(x_point, y_point, title)

        # 小标题位置
        c.setFont('msyh-bold', subtitle_size)
        x_point = self.width / 2 - (subtitle_len * subtitle_size) / 2
        y_point = self.height - 1.5 * title_size - 30
        c.drawString(x_point, y_point, subtitle)

        # 画了一条分割线
        c.line(20, y_point - 1.5 * subtitle_size, self.width - 20, y_point - 1.5 * subtitle_size)

        basic_info_height = y_point - 1.5 * subtitle_size - 10  # 分割线高度

        id_height = y_point - 1.5 * subtitle_size - 15
        id_width = 20

        num_width = self.width / 2 - id_width

        c.setFont('font_style9', 10)

        # 筛查编号位置
        c.drawString(id_width, id_height, id)  # 筛查编号
        # c.drawString(id_width + 50, id_height, patient_id)  # 筛查编号
        c.drawString(id_width + 50, id_height, patient_count)  # 筛查编号

        # 检查单号位置
        c.drawString(num_width, id_height, num)  # 检查单号
        c.drawString(num_width + 50, id_height, str(check_num))  # 检查单号

        # 姓名位置
        name = '姓名:'
        name_height = id_height - 15
        name_width = 20
        c.drawString(name_width, name_height, name)  # 姓名标题
        patient_name = data['patient_name']
        if len(patient_name) > 5:
            c.setFont('font_style9', 8)
        c.drawString(name_width + 35, name_height, patient_name)  # 姓名

        c.setFont('font_style9', 10)  # 将字体恢复，防止因名字过长改变字体
        # 年龄位置
        age = '年龄:'
        age_height = name_height - 15
        age_width = name_width
        c.drawString(age_width, age_height, age)  # 年龄
        patient_age = str(data['patient_age']) + '天'
        c.drawString(age_width + 35, age_height, patient_age)  # 年龄

        # 矫正孕周位置
        refine_weeks_title = '矫正孕周:'
        regine_weeks = str(data['refine_weeks']) + '周' + str(data['refine_days']) + '天'
        refine_height = age_height - 15
        refine_width = name_width
        c.drawString(refine_width, refine_height, refine_weeks_title)  # 矫正孕周标题
        c.drawString(refine_width + 50, refine_height, regine_weeks)  # 矫正孕周

        # 性别位置
        gender = '性别:'
        gender_height = name_height
        gender_width = self.width / 2 - name_width
        c.drawString(gender_width, gender_height, gender)  # 性别
        if data['patient_gender'] == '0':
            patient_gender = '男'
        else:
            patient_gender = '女'
        c.drawString(gender_width + 35, gender_height, patient_gender)  # 性别

        # 出生体重位置
        birth_weight_title = '出生体重:'
        birth_weight = str(data['birth_weight']) + '克'
        birth_weight_height = name_height - 15
        birth_weight_width = self.width / 2 - name_width
        c.drawString(birth_weight_width, birth_weight_height, birth_weight_title)  # 出生体重标题
        c.drawString(birth_weight_width + 50, birth_weight_height, birth_weight)  # 出生体重

        # 出生孕周
        birth_weeks_title = '出生孕周:'
        birth_weeks = str(data['birth_weeks']) + '周' + str(data['birth_days']) + '天'
        birth_weeks_height = name_height - 30
        birth_weeks_width = self.width / 2 - name_width
        c.drawString(birth_weeks_width, birth_weeks_height, birth_weeks_title)  # 出生孕周标题
        c.drawString(birth_weeks_width + 50, birth_weeks_height, birth_weeks)  # 出生孕周

        # 画了一条分割线
        line2_height = birth_weeks_height - 10
        c.line(20, line2_height, self.width - 20, line2_height)

        # OD OS标志位置 (A4纸 宽595 高841)
        c.setFont('font_style9', 12)
        od_os_height = line2_height - 20
        od_width = 270
        os_width = 270
        left_iqa_score = str(data['left_iqa_score'])
        right_iqa_score = str(data['right_iqa_score'])
        # OD = 'OD(图像质量:'+right_iqa_score+')'
        # OS = 'OS(图像质量:'+left_iqa_score+')'
        OD = 'OD(右眼)'
        OS = 'OS(左眼)'
        c.drawString(od_width + 150, od_os_height, OS)  # 左眼OS
        c.drawString(os_width - 150, od_os_height, OD)  # 右眼OD

        # 眼部照片位置
        picture_height = od_os_height - 210  # 眼底照片底部位置
        left_picture_width = 160
        right_picture_width = 160
        right_output_file = data['right_origin_src']
        left_output_file = data['left_origin_src']
        left_origin_format = os.path.splitext(left_output_file)[-1]
        right_origin_format = os.path.splitext(right_output_file)[-1]

        left_pdf_jpg = settings.BASE_DIR + \
                       "/media/patient_img/" + patient_id + '_left_pdf' + left_origin_format

        right_pdf_jpg = settings.BASE_DIR + \
                        "/media/patient_img/" + patient_id + '_right_pdf' + right_origin_format

        retention_tag(left_output_file, left_pdf_jpg)
        # c.drawImage(left_pdf_jpg, right_picture_width + 160, picture_height - 35, height=188, width=250)  # 200 270
        c.drawImage(left_pdf_jpg, right_picture_width + 145, picture_height - 20, height=210, width=280)  # 200 270

        retention_tag(right_output_file, right_pdf_jpg)
        # c.drawImage(right_pdf_jpg, left_picture_width - 135, picture_height - 35, height=188, width=250)  # 150 200
        c.drawImage(right_pdf_jpg, left_picture_width - 150, picture_height - 20, height=210, width=280)  # 150 200

        os.remove(left_pdf_jpg)
        os.remove(right_pdf_jpg)

        # AI照片位置
        AIpicture_height = picture_height - 20  # 眼底照片底部位置
        # 先画条线
        line_height = AIpicture_height - 30  # 照片顶端位置加上照片长度再向下偏移20
        print('picture_height', picture_height, basic_info_height - 1.5 * subtitle_size)
        c.line(20, line_height, self.width - 20, line_height)

        # 影像发现位置
        c.setFont('msyh-bold', 12)
        find = '影像所见:'
        find_height = line_height - 35
        c.drawString(20, find_height, find)  # 类别

        find_height = find_height - 25

        # 影像发现下的右眼
        c.setFont('font_style9', 12)
        right_eye = '右眼:'
        right_des_height = line_height - 60
        right_eye_width = 20
        c.drawString(right_eye_width, right_des_height, right_eye)  # 右眼
        r_y2 = 4.6
        l_y2 = 4.455
        i = 0
        if len(data['right_desc']) > 47:
            texts = self.cut_text(data['right_desc'], 47)
            right_eye_width = right_eye_width + 35
            for tx in texts:
                # c.drawString(right_eye_width, right_des_height - i*15, tx)
                i = i + 1
            if i == 0:
                r_y2 = r_y2
                l_y2 = l_y2
            elif i == 1:
                r_y2 = 4.6
                l_y2 = 3.6
            elif i == 2:
                r_y2 = 4.806
                l_y2 = 4.04
            elif i == 3:
                r_y2 = 4.6
                l_y2 = 3.63

            self.wrap_text(c, 'font_style9', 12, data['right_desc'], 7.45, 4, 0.7, r_y2)
            right_des_height = right_des_height - i * 15

        else:
            l_y2 = 4.25
            c.drawString(right_eye_width + 35, right_des_height,
                         '无' if (data['right_desc'] == '' or data['right_desc'] is None) else data[
                             'right_desc'])  # 右眼
        # 影像发现下的左眼
        left_eye = '左眼:'
        left_des_height = right_des_height - 25
        left_eye_width = 20
        c.drawString(left_eye_width, left_des_height, left_eye)  # 左眼
        j = 0
        if len(data['left_desc']) > 47:
            texts = self.cut_text(data['left_desc'], 47)
            print(texts)
            left_eye_width = left_eye_width + 35
            for tx in texts:
                # c.drawString(left_eye_width, left_des_height - i*15, tx)
                j = j + 1

            if i == 0 and j == 2:  # 如果右眼诊断为一行且左眼为两行
                l_y2 = 4.45

            if i == 2 and j == 3:  # 如果右眼诊断为二行且左眼为三行
                l_y2 = 3.84

            if i == 3 and j == 2:  # 如果右眼诊断为二行且左眼为三行
                l_y2 = 3.835
            self.wrap_text(c, 'font_style9', 12, data['left_desc'], 7.45, 4, 0.7, l_y2)
            left_des_height = left_des_height - j * 15

        else:
            c.drawString(left_eye_width + 35, left_des_height,
                         '无' if (data['left_desc'] == '' or data['left_desc'] is None) else data['left_desc'])  # 左眼
        # 建议

        # 类别
        # type = '类别'
        # c.setFont('song', 12)
        type_height = find_height - 20
        # type_width = 20
        # c.drawString(type_width, type_height, type)  # 类别
        # amount = '数量(个)'
        # c.setFont('song', 12)

        square = '总面积mm'
        c.setFont('msyh-bold', 12)
        square_height = type_height
        square_width = 320

        max_square = '最大面积mm'
        c.setFont('msyh-bold', 12)
        max_square_height = type_height
        max_square_width = 480
        # 出血
        blood = '出血'
        blood_height = type_height - 20
        blood_width = 20
        # c.drawString(blood_width, blood_height, blood)  # 出血

        # 渗出
        ooze = '渗出'
        ooze_height = blood_height - 20
        ooze_width = 20
        # c.drawString(ooze_width, ooze_height, ooze)  # 渗出

        # # 影像发现下的左眼
        left_eye_height = left_des_height - 10
        # 诊断
        c.setFont('msyh-bold', 12)
        sensation = '初步印象:'
        sensation_height = left_eye_height - 20
        sensation_width = 20
        c.drawString(sensation_width, sensation_height, sensation)  # 诊断

        # 诊断发现下的右眼
        c.setFont('font_style9', 12)
        right_eye = '右眼:'
        right_eye_height = sensation_height - 25
        right_eye_width = 20
        c.drawString(right_eye_width, right_eye_height, right_eye)  # 右眼
        c.drawString(right_eye_width + 35, right_eye_height,
                     '无' if (data['right_diagnose'] == '' or data['right_diagnose'] is None) else data[
                         'right_diagnose'])  # 右眼

        # 诊断发现下的左眼
        left_eye = '左眼:'
        left_eye_height = right_eye_height - 25
        left_eye_width = 20
        c.drawString(left_eye_width, left_eye_height, left_eye)  # 左眼
        c.drawString(left_eye_width + 35, left_eye_height,
                     '无' if (data['left_diagnose'] == '' or data['left_diagnose'] is None) else data[
                         'left_diagnose'])  # 左眼
        # 建议
        c.setFont('msyh-bold', 12)
        suggestion = '建议:'
        suggestion_height = left_eye_height - 40
        suggestion_width = 20
        # if data['other_advice']:
        #     other_advice = data['other_advice']
        # else:
        #     other_advice = ''
        #
        # if data['other_advice'] == '无':
        #     other_advice = ''

        c.drawString(suggestion_width, suggestion_height, suggestion)  # 建议
        c.setFont('font_style9', 12)
        try:
            review_time = data['review_time']
        except Exception as e:
            print(e)
            review_time = ''
        if review_time:
            diagnose_advice = '建议' + data['review_time'] + '前复诊'
            c.drawString(suggestion_width, suggestion_height - 25, diagnose_advice)  # 建议
        else:
            c.drawString(suggestion_width, suggestion_height - 25, data['diagnose_advice'])  # 建议
        # 再画条线
        line_height = suggestion_height - 50  # 建议下方的横线
        c.line(20, self.height - 790, self.width - 20, self.height - 790)
        # 医院
        hospital = '医院:'
        hospital_height = line_height - 25
        hospital_width = 20

        # 医生
        # doctor = '医生(签字):'
        doctor = '报告医师:'
        doctor_height = hospital_height
        doctor_width = 20
        c.drawString(doctor_width, doctor_height, doctor)  # 医生

        signature = data['doctor_name']
        # if signature:
        #     c.drawString(doctor_width + 30, doctor_height, signature)  # 医生姓名
        c.drawString(doctor_width + 55, doctor_height, signature)  # 医生姓名

        diagnose_time1 = '诊断时间:'
        diagnose_time2 = data['diagnose_time']
        diagnose_height = doctor_height - 20
        diagnose_width = 20
        c.drawString(diagnose_width, diagnose_height, diagnose_time1)  # 医生
        c.drawString(diagnose_width + 55, diagnose_height, diagnose_time2)  # 医生姓名

        # 放置二维码
        code_jpg = settings.BASE_DIR + '/media/image/code.jpg'
        code_jpg_width = self.width - 20 - 50
        code_jpg_height = self.height - 780
        # c.drawImage(code_jpg, code_jpg_width, code_jpg_height, height=50, width=50)  # 200 270

        # 放置logo
        logo = settings.BASE_DIR + '/media/image/' + data['database'] + '_logo.jpg'

        # 温馨提示
        c.setFont('font_style9', 7)
        tips = '本次检查结果只反映孩子目前的眼底情况。' \
               '特别是3岁以前，眼睛的结构和功能都在迅速发育，' \
               '眼底检查正常并不意味着生长发育过程中不会出现其他眼底问题。' \
               '一些发育性眼病如斜视、弱视，屈光不正等，要到一定年龄才能被发现，' \
               '定期对儿童进行眼保健检查，发现视功能异常，及时干预。'

        tips_height = self.height - 830  # height:为A4纸的高度
        styleSheet = getSampleStyleSheet()
        style = styleSheet['BodyText']
        style.fontName = 'font_style9'
        style.fontSize = 8
        # 设置行距
        style.leading = 15
        # 首行缩进
        style.firstLineIndent = 22
        Pa = Paragraph(tips, style)
        Pa.wrapOn(c, 7.8 * inch, 10 * inch)
        Pa.drawOn(c, 0.25 * inch, tips_height)

        if data['report_module'] == 'module2':
            if '糖尿病' in data['left_diagnose'] or '糖尿病' in data['right_diagnose']:
                c.showPage()
                tw1 = settings.BASE_DIR + '/media/image/tw_01.png'
                c.drawImage(tw1, 0, 0, height=self.height, width=self.width)
                c.showPage()
                tw2 = settings.BASE_DIR + '/media/image/tw_02.png'
                c.drawImage(tw2, 0, 0, height=self.height, width=self.width)
            if '豹纹' in data['left_diagnose'] or '豹纹' in data['right_diagnose']:
                c.showPage()
                bw = settings.BASE_DIR + '/media/image/bw_01.png'
                c.drawImage(bw, 0, 0, height=self.height, width=self.width)
        c.save()

    def create_pdf5(self):
        data = self.data
        mkdir(self.dir)
        pdfmetrics.registerFont(TTFont('msyh', font_position))
        pdfmetrics.registerFont(TTFont('msyh-bold', bold_font_position))

        pdfmetrics.registerFont(TTFont('font_style9', font_style9))

        patient_id = str(data['patient_id'])

        # create_time = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")

        if 'patient_count' in data:
            patient_count = str(data['patient_count'])
            pdf_name = self.dir + '/' + data['patient_name'].strip() + '_' + str(patient_id) + '_' + str(
                patient_count) + '.pdf'
        else:
            patient_count = patient_id
            pdf_name = self.dir + '/' + data['patient_name'].strip() + '_' + str(
                patient_id) + '.pdf'

        c = canvas.Canvas(pdf_name)
        check_num = PatientInfo.objects.filter(patient_id=data['patient_id'])[0].check_num
        # title and subtitle
        subtitle = "新生儿眼底筛查报告单"
        if data['report_title']:
            title = data['report_title']
        else:
            title = "安徽妇幼保健医院"
        title_len = len(title)
        subtitle_len = len(subtitle)
        title_size = 13
        subtitle_size = 12

        id = '筛查编号:'
        num = '检查单号:'

        # 大标题位置
        c.setFont('msyh-bold', title_size)
        x_point = self.width / 2 - (title_len * title_size) / 2
        y_point = self.height - 1.5 * title_size - 10
        c.drawString(x_point, y_point, title)

        # 小标题位置
        c.setFont('msyh-bold', subtitle_size)
        x_point = self.width / 2 - (subtitle_len * subtitle_size) / 2
        y_point = self.height - 1.5 * title_size - 30
        c.drawString(x_point, y_point, subtitle)

        # 画了一条分割线
        c.line(20, y_point - 1.5 * subtitle_size, self.width - 20, y_point - 1.5 * subtitle_size)

        basic_info_height = y_point - 1.5 * subtitle_size - 10  # 分割线高度

        id_height = y_point - 1.5 * subtitle_size - 15
        id_width = 20

        num_width = self.width / 2 - id_width

        c.setFont('font_style9', 10)

        # 筛查编号位置
        c.drawString(id_width, id_height, id)  # 筛查编号
        # c.drawString(id_width + 50, id_height, patient_id)  # 筛查编号
        c.drawString(id_width + 50, id_height, patient_count)  # 筛查编号

        # 检查单号位置
        c.drawString(num_width, id_height, num)  # 检查单号
        c.drawString(num_width + 50, id_height, str(check_num))  # 检查单号

        # 姓名位置
        name_height = id_height - 15
        name_width = 20
        if 'parent_name' in data:
            patient_name = data['parent_name'] + '/' + data['patient_name']
            name = '姓名(母亲/儿童):'
            specific_name_width = name_width + 85
        else:
            patient_name = data['patient_name']
            name = '姓名:'
            specific_name_width = name_width + 27

        c.drawString(name_width, name_height, name)  # 姓名标题
        if len(patient_name) > 5:
            c.setFont('font_style9', 8)
        c.drawString(specific_name_width, name_height, patient_name)  # 具体姓名

        c.setFont('font_style9', 10)  # 将字体恢复，防止因名字过长改变字体
        # 年龄位置
        age = '年龄:'
        age_height = name_height - 15
        age_width = name_width
        c.drawString(age_width, age_height, age)  # 年龄
        patient_age = str(data['patient_age']) + '天'
        c.drawString(age_width + 35, age_height, patient_age)  # 年龄

        # 矫正孕周位置
        refine_weeks_title = '矫正孕周:'
        regine_weeks = str(data['refine_weeks']) + '周' + str(data['refine_days']) + '天'
        refine_height = age_height - 15
        refine_width = name_width
        c.drawString(refine_width, refine_height, refine_weeks_title)  # 矫正孕周标题
        c.drawString(refine_width + 50, refine_height, regine_weeks)  # 矫正孕周

        # 性别位置
        gender = '性别:'
        gender_height = name_height
        gender_width = self.width / 2 - name_width
        c.drawString(gender_width, gender_height, gender)  # 性别
        if data['patient_gender'] == '0':
            patient_gender = '男'
        else:
            patient_gender = '女'
        c.drawString(gender_width + 35, gender_height, patient_gender)  # 性别

        # 出生体重位置
        birth_weight_title = '出生体重:'
        birth_weight = str(data['birth_weight']) + '克'
        birth_weight_height = name_height - 15
        birth_weight_width = self.width / 2 - name_width
        c.drawString(birth_weight_width, birth_weight_height, birth_weight_title)  # 出生体重标题
        c.drawString(birth_weight_width + 50, birth_weight_height, birth_weight)  # 出生体重

        # 出生孕周
        birth_weeks_title = '出生孕周:'
        birth_weeks = str(data['birth_weeks']) + '周' + str(data['birth_days']) + '天'
        birth_weeks_height = name_height - 30
        birth_weeks_width = self.width / 2 - name_width
        c.drawString(birth_weeks_width, birth_weeks_height, birth_weeks_title)  # 出生孕周标题
        c.drawString(birth_weeks_width + 50, birth_weeks_height, birth_weeks)  # 出生孕周

        # 画了一条分割线
        line2_height = birth_weeks_height - 10
        c.line(20, line2_height, self.width - 20, line2_height)

        # OD OS标志位置 (A4纸 宽595 高841)
        c.setFont('font_style9', 12)
        od_os_height = line2_height - 20
        od_width = 270
        os_width = 270
        left_iqa_score = str(data['left_iqa_score'])
        right_iqa_score = str(data['right_iqa_score'])
        # OD = 'OD(图像质量:'+right_iqa_score+')'
        # OS = 'OS(图像质量:'+left_iqa_score+')'
        OD = 'OD(右眼)'
        OS = 'OS(左眼)'
        c.drawString(od_width + 150, od_os_height, OS)  # 左眼OS
        c.drawString(os_width - 150, od_os_height, OD)  # 右眼OD

        # 眼部照片位置
        picture_height = od_os_height - 210  # 眼底照片底部位置
        left_picture_width = 160
        right_picture_width = 160
        right_output_file = data['right_origin_src']
        left_output_file = data['left_origin_src']
        left_origin_format = os.path.splitext(left_output_file)[-1]
        right_origin_format = os.path.splitext(right_output_file)[-1]

        left_pdf_jpg = settings.BASE_DIR + \
                       "/media/patient_img/" + patient_id + '_left_pdf' + left_origin_format

        right_pdf_jpg = settings.BASE_DIR + \
                        "/media/patient_img/" + patient_id + '_right_pdf' + right_origin_format

        retention_tag(left_output_file, left_pdf_jpg)
        # c.drawImage(left_pdf_jpg, right_picture_width + 160, picture_height - 35, height=188, width=250)  # 200 270
        c.drawImage(left_pdf_jpg, right_picture_width + 145, picture_height - 20, height=210, width=280)  # 200 270

        retention_tag(right_output_file, right_pdf_jpg)
        # c.drawImage(right_pdf_jpg, left_picture_width - 135, picture_height - 35, height=188, width=250)  # 150 200
        c.drawImage(right_pdf_jpg, left_picture_width - 150, picture_height - 20, height=210, width=280)  # 150 200

        os.remove(left_pdf_jpg)
        os.remove(right_pdf_jpg)

        # AI照片位置
        AIpicture_height = picture_height - 20  # 眼底照片底部位置
        # 先画条线
        line_height = AIpicture_height - 30  # 照片顶端位置加上照片长度再向下偏移20
        print('picture_height', picture_height, basic_info_height - 1.5 * subtitle_size)
        c.line(20, line_height, self.width - 20, line_height)

        # 影像发现位置
        c.setFont('msyh-bold', 12)
        find = '影像所见:'
        find_height = line_height - 35
        c.drawString(20, find_height, find)  # 类别

        find_height = find_height - 25

        # 影像发现下的右眼
        c.setFont('font_style9', 12)
        right_eye = '右眼:'
        right_des_height = line_height - 60
        right_eye_width = 20
        c.drawString(right_eye_width, right_des_height, right_eye)  # 右眼
        r_y2 = 4.6
        l_y2 = 4.455
        i = 0
        if len(data['right_desc']) > 47:
            texts = self.cut_text(data['right_desc'], 47)
            right_eye_width = right_eye_width + 35
            for tx in texts:
                # c.drawString(right_eye_width, right_des_height - i*15, tx)
                i = i + 1
            if i == 0:
                r_y2 = r_y2
                l_y2 = l_y2
            elif i == 1:
                r_y2 = 4.6
                l_y2 = 3.6
            elif i == 2:
                r_y2 = 4.806
                l_y2 = 4.04
            elif i == 3:
                r_y2 = 4.6
                l_y2 = 3.63

            self.wrap_text(c, 'font_style9', 12, data['right_desc'], 7.45, 4, 0.7, r_y2)
            right_des_height = right_des_height - i * 15

        else:
            l_y2 = 4.25
            c.drawString(right_eye_width + 35, right_des_height,
                         '无' if (data['right_desc'] == '' or data['right_desc'] is None) else data[
                             'right_desc'])  # 右眼
        # 影像发现下的左眼
        left_eye = '左眼:'
        left_des_height = right_des_height - 25
        left_eye_width = 20
        c.drawString(left_eye_width, left_des_height, left_eye)  # 左眼
        j = 0
        if len(data['left_desc']) > 47:
            texts = self.cut_text(data['left_desc'], 47)
            left_eye_width = left_eye_width + 35
            for tx in texts:
                # c.drawString(left_eye_width, left_des_height - i*15, tx)
                j = j + 1

            if i == 0 and j == 2:  # 如果右眼诊断为一行且左眼为两行
                l_y2 = 4.45

            if i == 2 and j == 3:  # 如果右眼诊断为二行且左眼为三行
                l_y2 = 3.84

            if i == 3 and j == 2:  # 如果右眼诊断为二行且左眼为三行
                l_y2 = 3.835
            self.wrap_text(c, 'font_style9', 12, data['left_desc'], 7.45, 4, 0.7, l_y2)
            left_des_height = left_des_height - j * 15

        else:
            c.drawString(left_eye_width + 35, left_des_height,
                         '无' if (data['left_desc'] == '' or data['left_desc'] is None) else data['left_desc'])  # 左眼
        # 建议

        # 类别
        # type = '类别'
        # c.setFont('song', 12)
        type_height = find_height - 20
        # type_width = 20
        # c.drawString(type_width, type_height, type)  # 类别
        # amount = '数量(个)'
        # c.setFont('song', 12)

        square = '总面积mm'
        c.setFont('msyh-bold', 12)
        square_height = type_height
        square_width = 320

        max_square = '最大面积mm'
        c.setFont('msyh-bold', 12)
        max_square_height = type_height
        max_square_width = 480
        # 出血
        blood = '出血'
        blood_height = type_height - 20
        blood_width = 20
        # c.drawString(blood_width, blood_height, blood)  # 出血

        # 渗出
        ooze = '渗出'
        ooze_height = blood_height - 20
        ooze_width = 20
        # c.drawString(ooze_width, ooze_height, ooze)  # 渗出

        # # 影像发现下的左眼
        left_eye_height = left_des_height - 10
        # 诊断
        c.setFont('msyh-bold', 12)
        sensation = '初步印象:'
        sensation_height = left_eye_height - 20
        sensation_width = 20
        c.drawString(sensation_width, sensation_height, sensation)  # 诊断

        # 诊断发现下的右眼
        c.setFont('font_style9', 12)
        right_eye = '右眼:'
        right_eye_height = sensation_height - 25
        right_eye_width = 20
        c.drawString(right_eye_width, right_eye_height, right_eye)  # 右眼
        c.drawString(right_eye_width + 35, right_eye_height,
                     '无' if (data['right_diagnose'] == '' or data['right_diagnose'] is None) else data[
                         'right_diagnose'])  # 右眼

        # 诊断发现下的左眼
        left_eye = '左眼:'
        left_eye_height = right_eye_height - 25
        left_eye_width = 20
        c.drawString(left_eye_width, left_eye_height, left_eye)  # 左眼
        c.drawString(left_eye_width + 35, left_eye_height,
                     '无' if (data['left_diagnose'] == '' or data['left_diagnose'] is None) else data[
                         'left_diagnose'])  # 左眼
        # 建议
        c.setFont('msyh-bold', 12)
        suggestion = '建议:'
        suggestion_height = left_eye_height - 40
        suggestion_width = 20
        # if data['other_advice']:
        #     other_advice = data['other_advice']
        # else:
        #     other_advice = ''
        #
        # if data['other_advice'] == '无':
        #     other_advice = ''

        c.drawString(suggestion_width, suggestion_height, suggestion)  # 建议
        c.setFont('font_style9', 12)
        try:
            review_time = data['review_time']
        except Exception as e:
            print(e)
            review_time = ''
        if review_time:
            diagnose_advice = '建议' + data['review_time'] + '前复诊'
            c.drawString(suggestion_width, suggestion_height - 25, diagnose_advice)  # 建议
        else:
            c.drawString(suggestion_width, suggestion_height - 25, data['diagnose_advice'])  # 建议

        # 再画条线
        line_height = self.height - 745  # 建议下方的横线
        c.line(20, line_height, self.width - 20, line_height)

        # 医院
        hospital = '医院:'
        # hospital_height = line_height - 25
        # hospital_height = self.height - 745
        hospital_width = 20

        diagnose_height = line_height + 40 - 2

        doctor_height = diagnose_height + 20

        # 医生
        # doctor = '医生(签字):'
        doctor = '报告医师:'
        # doctor_height = line_height + 40 - 2
        doctor_width = 20
        c.drawString(self.width - 170, doctor_height, doctor)  # 医生

        signature = data['doctor_name']
        # if signature:
        #     c.drawString(doctor_width + 30, doctor_height, signature)  # 医生姓名
        c.drawString(self.width - 170 + 55, doctor_height, signature)  # 医生姓名

        diagnose_time1 = '诊断时间:'
        diagnose_time2 = data['diagnose_time']
        # diagnose_height = doctor_height + 20
        diagnose_width = 20
        c.drawString(self.width - 170, diagnose_height, diagnose_time1)  # 医生
        c.drawString(self.width - 170 + 55, diagnose_height, diagnose_time2)  # 医生姓名

        # 放置图片
        code_jpg = settings.BASE_DIR + '/media/image/tips6.png'
        # code_jpg_width = self.width - 20 - 50
        code_jpg_width = diagnose_width
        code_jpg_height = self.height - 790
        # c.drawImage(code_jpg, code_jpg_width, code_jpg_height, height=60, width=560)  # 200 270

        # 放置logo
        logo = settings.BASE_DIR + '/media/image/' + data['database'] + '_logo.jpg'

        # 温馨提示
        c.setFont('font_style9', 7)
        tips = '本次检查结果只反映孩子目前的眼底情况。' \
               '特别是3岁以前，眼睛的结构和功能都在迅速发育，' \
               '眼底检查正常并不意味着生长发育过程中不会出现其他眼底问题。' \
               '一些发育性眼病如斜视、弱视，屈光不正等，要到一定年龄才能被发现，' \
               '定期对儿童进行眼保健检查，发现视功能异常，及时干预。'

        tips2 = '- 复查请提前三天电话预约'
        tips3 = '- 院本部 儿童眼保健门诊：周一至周五 工作时间；周六、周日 上午（节假日除外） 预约电话：0551-69118113，0551-69118289'
        tips4 = '- 院西区 儿童眼保健门诊：周一至周五工作时间（节假日除外） 预约电话：0551-62160092'
        tips5 = '- 院东区 儿童眼保健门诊：周一、周四 （节假日除外） 预约电话：0551-69118737'

        tips_height = self.height - 770  # height:为A4纸的高度
        styleSheet = getSampleStyleSheet()
        style = styleSheet['BodyText']
        style.fontName = 'font_style9'
        style.fontSize = 8
        # 设置行距
        style.leading = 10
        # 首行缩进
        style.firstLineIndent = 22
        Pa = Paragraph(tips, style)
        Pa.wrapOn(c, 7.8 * inch, 10 * inch)
        Pa.drawOn(c, 0.25 * inch, tips_height)

        style.firstLineIndent = 0  # 缩进为0

        Pa = Paragraph(tips2, style)
        Pa.wrapOn(c, 7.8 * inch, 10 * inch)
        Pa.drawOn(c, 0.25 * inch, tips_height - 15)

        Pa = Paragraph(tips3, style)
        Pa.wrapOn(c, 7.8 * inch, 10 * inch)
        Pa.drawOn(c, 0.25 * inch, tips_height - 25)

        Pa = Paragraph(tips4, style)
        Pa.wrapOn(c, 7.8 * inch, 10 * inch)
        Pa.drawOn(c, 0.25 * inch, tips_height - 35)

        Pa = Paragraph(tips5, style)
        Pa.wrapOn(c, 7.8 * inch, 10 * inch)
        Pa.drawOn(c, 0.25 * inch, tips_height - 45)

        if data['report_module'] == 'module2':
            if '糖尿病' in data['left_diagnose'] or '糖尿病' in data['right_diagnose']:
                c.showPage()
                tw1 = settings.BASE_DIR + '/media/image/tw_01.png'
                c.drawImage(tw1, 0, 0, height=self.height, width=self.width)
                c.showPage()
                tw2 = settings.BASE_DIR + '/media/image/tw_02.png'
                c.drawImage(tw2, 0, 0, height=self.height, width=self.width)
            if '豹纹' in data['left_diagnose'] or '豹纹' in data['right_diagnose']:
                c.showPage()
                bw = settings.BASE_DIR + '/media/image/bw_01.png'
                c.drawImage(bw, 0, 0, height=self.height, width=self.width)
        c.save()
        return pdf_name


def opt_create_pdf(data):
    dir = settings.BASE_DIR + "/media/patient_pdf/"
    mkdir(dir)
    pdf_name = dir + '/' + data['patient_name'].strip() + '_' + str(data['patient_id']) + '.pdf'
    reportlab.pdfbase.pdfmetrics.registerFont(
        reportlab.pdfbase.ttfonts.TTFont('song', font_position))  # 注册字体
    c = canvas.Canvas(pdf_name)
    width, height = A4
    print('width,height', width, height)
    # title and subtitle
    subtitle = "视光检查报告"
    title = "合肥高新区天乐社区卫生服务中心"
    title_len = len(title) / 3
    subtitle_len = len(subtitle)
    print('len(subtitle)', len(subtitle))
    title_size = 20
    subtitle_size = 15

    # 写了一个小标题
    c.setFont('song', subtitle_size)
    x_point = width / 2 - (subtitle_len * subtitle_size) / 2
    y_point = height - 1.5 * subtitle_size - 10
    c.drawString(x_point, y_point, subtitle)

    # 画了一条分割线
    c.line(0, y_point - 1.5 * subtitle_size, width, y_point - 1.5 * subtitle_size)

    name = '姓名:'
    gender = '性别:'
    age = '年龄:'
    diagnose_date = '日期:'
    diagnose_time = data['diagnose_time']
    basic_info_height = y_point - 1.5 * subtitle_size - 10  # 分割线高度
    name_height = y_point - 1.5 * subtitle_size - 20
    name_width = 20
    gender_height = y_point - 1.5 * subtitle_size - 20
    gender_width = 160
    age_height = y_point - 1.5 * subtitle_size - 20
    age_width = 300
    diagnose_date_height = y_point - 1.5 * subtitle_size - 20
    diagnose_date_width = 440

    c.drawString(name_width - 8, name_height, name)  # 姓名
    patient_name = data['patient_name']
    if len(patient_name) > 5:
        c.setFont('song', 10)
    c.drawString(name_width + 27, name_height, patient_name)  # 姓名

    c.setFont('song', 15)
    c.drawString(gender_width - 10, gender_height, gender)  # 性别
    if data['patient_gender'] == '0':
        patient_gender = '男'
    else:
        patient_gender = '女'
    c.drawString(gender_width + 25, gender_height, patient_gender)  # 性别

    c.drawString(age_width - 10, age_height, age)  # 年龄
    patient_age = str(data['patient_age'])
    c.drawString(age_width + 25, age_height, patient_age)  # 年龄

    c.drawString(diagnose_date_width - 17, diagnose_date_height, diagnose_date)  # 日期
    c.setFont('song', 15)
    c.drawString(diagnose_date_width + 18, diagnose_date_height, diagnose_time)  # 日期

    c.drawString(name_width, diagnose_date_height - 30, '眼外观:')

    c.setFont('song', 10)
    c.drawString(name_width, diagnose_date_height - 50, '眼睑:')
    c.drawString(name_width + 40, diagnose_date_height - 50, '未见异常' if data['yanjian'] == '0' else '异常')

    c.drawString(name_width, diagnose_date_height - 70, '角膜:')
    c.drawString(name_width + 40, diagnose_date_height - 70, '未见异常' if data['jiaomo'] == '0' else '异常')

    c.drawString(name_width, diagnose_date_height - 90, '结膜:')
    c.drawString(name_width + 40, diagnose_date_height - 90, '未见异常' if data['jiemo'] == '0' else '异常')

    c.drawString(name_width, diagnose_date_height - 110, '瞳孔:')
    c.drawString(name_width + 40, diagnose_date_height - 110, '未见异常' if data['tongkong'] == '0' else '异常')

    c.drawString(name_width, diagnose_date_height - 130, '其他:')
    c.drawString(name_width + 40, diagnose_date_height - 130, '未见异常' if data['opt_others'] == '0' else '异常')

    yanwaiguan_height = diagnose_date_height - 150

    quguang_width = name_width + 50

    quguang_width2 = name_width + 250

    c.setFont('song', 15)
    c.drawString(name_width, yanwaiguan_height - 20, '屈光:')

    c.setFont('song', 10)
    c.drawString(name_width, yanwaiguan_height - 40, '球镜右:')
    c.drawString(quguang_width, yanwaiguan_height - 40, str(data['right_qiujing']))

    c.drawString(name_width, yanwaiguan_height - 60, '柱镜右:')
    c.drawString(quguang_width, yanwaiguan_height - 60, str(data['right_zhujing']))

    c.drawString(name_width, yanwaiguan_height - 80, '轴位右:')
    c.drawString(quguang_width, yanwaiguan_height - 80, str(data['right_zhouwei']))

    c.drawString(quguang_width2, yanwaiguan_height - 40, '球镜左:')
    c.drawString(quguang_width2 + 50, yanwaiguan_height - 40, str(data['left_qiujing']))

    c.drawString(quguang_width2, yanwaiguan_height - 60, '柱镜左:')
    c.drawString(quguang_width2 + 50, yanwaiguan_height - 60, str(data['left_zhujing']))

    c.drawString(quguang_width2, yanwaiguan_height - 80, '轴位左:')
    c.drawString(quguang_width2 + 50, yanwaiguan_height - 80, str(data['left_zhouwei']))

    conclusion_height = yanwaiguan_height - 80
    c.drawString(name_width, conclusion_height - 20, '结论:')
    if data['opt_conclusion'] == '0':
        opt_conclusion = '正常'
    elif data['opt_conclusion'] == '1':
        opt_conclusion = '异常'
    else:
        opt_conclusion = '远视储备低'
    c.drawString(name_width + 40, conclusion_height - 20, opt_conclusion)

    c.setFont('song', 15)
    quguang_height = conclusion_height - 60
    c.drawString(name_width, quguang_height, '眼位:')

    c.setFont('song', 10)
    c.drawString(name_width, quguang_height - 20, 'HT(角膜映光法)' if data['yanwei'] == '0' else 'ACT(交替遮盖法)')
    c.drawString(name_width, quguang_height - 40, '未见异常' if data['yanwei'] == '0' else '异常')

    c.drawString(name_width, quguang_height - 60, '备注:')
    c.drawString(name_width, quguang_height - 80, '无' if data['beizhu'] == '' else data['beizhu'])

    c.setFont('song', 15)
    c.drawString(name_width, quguang_height - 120, '初筛结果:')

    c.setFont('song', 10)
    c.drawString(name_width, quguang_height - 140, '通过' if data['result'] == '0' else '检出阳性')

    c.setFont('song', 15)
    c.drawString(name_width, quguang_height - 170, '医生嘱咐:')
    c.setFont('song', 10)
    c.drawString(name_width, quguang_height - 190, data['doctor_advice'])

    if 'next_check_time' in data:
        c.setFont('song', 15)
        c.drawString(name_width, quguang_height - 220, '下次检查时间:')
        c.setFont('song', 10)
        c.drawString(name_width, quguang_height - 240, data['next_check_time'])

    c.save()
