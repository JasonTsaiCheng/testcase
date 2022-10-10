"""orbis_marker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
# from django.contrib import admin
from django.conf.urls import include
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
# from pictures.views import PatientsListView

from users.views import *
from pictures.views import *
import xadmin
import operation.views as views
from operation.views import *
from rest_framework_jwt.views import obtain_jwt_token
from django.views.decorators.cache import cache_page
from django.views.static import serve
from orbis_marker.settings import MEDIA_ROOT
from django.conf import settings
from django.contrib import admin
from operation.views import PasswordView

router = DefaultRouter()
# router.register(r'patients', PatientsListView)
# router.register(r'doctorDiagnose', DoctorDiagnoseListView)
# router.register(r'optDiagnose', DoctorOptDiagnoseListView)
# router.register(r'task_finis_status', TaskFinishStatusListView)

cache_page(0)

urlpatterns = [

    url(r'^', include(router.urls)),

    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),

    url(r'^admin/', admin.site.urls),

    # 患者信息序列化
    # url(r'patients/$', PatientsListView.as_view(), name="patients-list"),

    url(r'^tasks/$', TaskTableListView.as_view({'get': 'list', 'post': 'create',
                                                'put': 'update', 'delete': 'destroy'})),

    # 用户信息序列化
    url(r'users/$', UserListView.as_view({'get': 'list', 'post': 'create',
                                          'put': 'update', 'delete': 'destroy'})),

    url(r'mark_pictures/$', PicturesListView.as_view({'get': 'list', 'post': 'create', 'put': 'update'})),


    url(r'mark_result/$', MarkResultListView.as_view({'get': 'list', 'post': 'create', 'put': 'update'})),

    url(r'picture_label_result/$', PictureLabelResult.as_view({'post': 'create', })),

    # 用户注册视图
    url(r'register/', UserRegisterView.as_view(), name="user-register"),

    # 社区医院信息序列化
    # url(r'hospital_list/$', HospitalListView.as_view(), name="hospital-list"),

    # 诊断结论热词序列化
    # url(r'diagnosis/$', DiagnoseConclusionListView.as_view(), name="diagnosis-list"),

    url(r'captcha/', include('captcha.urls')),

    url(r'pwd', PasswordView.as_view(), name='password-process'),

    url(r'xadmin/', xadmin.site.urls),

    url(r'^operation/(?P<order>\w+)/$', views.user_operation, name="UserOperation"),

    # '''登录外事件'''
    url(r'^logoutOperation/(?P<order>\w+)/$', views.user_logout_operation, name="logoutOperation"),


    url('^getCaptcha/', CaptchaView.as_view()),


    url(r'^login', obtain_jwt_token),

    # 修改密码
    # url(r'modifyPwd', PasswordView.as_view(), name='modify-pwd')

    # 登录外事件
    # url(r'^logoutOperation/(?P<order>\w+)/$', views.user_logout_operation, name="logoutOperation"),

    # 清楚缓存
    # url(r'^clear', views.clear_cache, name='clearCache')

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

