# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2022-09-26 14:27
from __future__ import unicode_literals

import datetime
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_ranks', models.IntegerField(choices=[(0, '其他'), (1, '住院医师'), (2, '主治医师'), (3, '副主任医师'), (4, '主任医师')], default=1, verbose_name='医生职称')),
                ('user_role', models.IntegerField(choices=[(0, '医生'), (1, '护士')], default=0, verbose_name='角色')),
                ('account_type', models.IntegerField(choices=[(0, '眼底'), (1, '眼视光')], default=0, verbose_name='账户类型')),
                ('user_gender', models.IntegerField(choices=[(0, '男'), (1, '女')], default=0, verbose_name='性别')),
                ('user_mobile', models.CharField(blank=True, max_length=11, verbose_name='手机号')),
                ('user_mode', models.IntegerField(choices=[(0, '单模态'), (1, '双模态'), (2, '多模态')], default=0, verbose_name='模态')),
                ('report_module', models.IntegerField(choices=[(0, '版本1'), (1, '版本2'), (2, '版本3'), (3, '版本4'), (4, '版本5'), (5, '版本6')], default=0, verbose_name='报告模板')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
            ],
            options={
                'verbose_name': '用户信息',
                'verbose_name_plural': '用户信息',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital_name', models.CharField(max_length=20, verbose_name='医院名称')),
                ('simplify_name', models.CharField(max_length=20, verbose_name='医院简称')),
                ('hospital_degree', models.CharField(blank=True, max_length=10, verbose_name='医院等级')),
                ('hospital_address', models.CharField(blank=True, max_length=30, verbose_name='医院地址')),
                ('hospital_ip_address', models.CharField(blank=True, max_length=15, verbose_name='医院ip地址')),
                ('hospital_logo', models.ImageField(blank=True, upload_to='logo/%Y/%m', verbose_name='医院logo')),
            ],
            options={
                'verbose_name': '医院信息',
                'verbose_name_plural': '医院信息',
            },
        ),
        migrations.CreateModel(
            name='HospitalArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_name', models.CharField(max_length=20, verbose_name='院区名称')),
                ('simplify_area_name', models.CharField(max_length=20, verbose_name='院区简称')),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hospital_area', to='users.Hospital', verbose_name='所属医院名称')),
            ],
            options={
                'verbose_name': '院区信息',
                'verbose_name_plural': '院区信息',
            },
        ),
        migrations.CreateModel(
            name='TaskTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=50, verbose_name='任务名称')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')),
                ('marker', models.ManyToManyField(related_name='picture_maker', to=settings.AUTH_USER_MODEL, verbose_name='标注者')),
            ],
            options={
                'verbose_name': '任务表',
                'verbose_name_plural': '任务表',
            },
        ),
        migrations.AddField(
            model_name='userprofile',
            name='hospital',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Hospital', verbose_name='所属医院(三甲医院)'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user_hospital_area',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.HospitalArea', verbose_name='所属院区'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]