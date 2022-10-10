# -*- coding:utf-8 -*-
__author__ = 'Jason'
__date__ = '2019/7/15 19:35'
import xadmin
from xadmin import views
from xadmin.plugins.auth import UserAdmin
from .models import *


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "奥比斯后台管理系统"
    site_footer = "合肥奥比斯科技有限公司"
    # menu_style = "accordion"


class TaskTableAdmin(object):
    list_display = ['task_name', 'marker', 'create_time', 'task_state', 'arbitrate_status', 'arbitrate_rules']
    search_fields = ['task_name', 'marker', 'create_time', 'task_state', 'arbitrate_status', 'arbitrate_rules']
    list_filter = ['task_name', 'marker', 'create_time', 'task_state', 'arbitrate_status', 'arbitrate_rules']


class TaskFinishStatusAdmin(object):
    list_display = ['task', 'marker',  'task_finish_status']
    search_fields = ['task', 'marker',  'task_finish_status']
    list_filter = ['task', 'marker',  'task_finish_status']


xadmin.site.register(TaskTable, TaskTableAdmin)
# xadmin.site.register(TaskFinishStatus, TaskFinishStatusAdmin)
# xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
