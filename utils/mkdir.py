# -*- coding:utf-8 -*-
__author__ = 'Jason'
__date__ = '2019/9/5 14:09'
import os

def mkdir(path):
    path = path.strip() # 去除首位空格
    path = path.rstrip("\\") # 去除尾部 \ 符号
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)
        print(path + 'create successfully')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path + 'file already exist')
        return False