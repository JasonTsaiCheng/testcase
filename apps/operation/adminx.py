# -*- coding:utf-8 -*-
__author__ = 'Jason'
__date__ = '2019/7/16 13:51'
import xadmin

from .models import MarkResult


class MarkResultAdmin(object):
    list_display = ['picture', 'mark_result', 'mark_time', 'marker',
                    'arbitrate_status', 'arbitrate_result', 'arbitrator', 'task_id']

    search_fields = ['picture', 'mark_result', 'mark_time', 'marker',
                     'arbitrate_status', 'arbitrate_result', 'arbitrator', 'task_id']

    list_filter = ['picture',  'mark_result', 'mark_time', 'marker',
                   'arbitrate_status', 'arbitrate_result', 'arbitrator', 'task_id']


xadmin.site.register(MarkResult, MarkResultAdmin)
