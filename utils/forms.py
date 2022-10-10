# -*- coding:utf-8 -*-
__author__ = 'Jason'
__date__ = '2020/7/10 10:23'
from django.contrib.auth.forms import UserCreationForm
from users.models import UserProfile


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserProfile
        fields = ("username", "email")


class ResetPwdForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserProfile
        fields = ("password",)