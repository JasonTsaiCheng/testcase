# -*- coding:utf-8 -*-
__author__ = 'Jason'
__date__ = '2019/7/15 20:26'
import xadmin

from .models import Pictures


class PicturesAdmin(object):
    list_display = ['pic_name', 'upload_time', 'task']
    search_fields = ['pic_name', 'upload_time', 'task']
    list_filter = ['pic_name', 'upload_time', 'task']

xadmin.site.register(Pictures, PicturesAdmin)

