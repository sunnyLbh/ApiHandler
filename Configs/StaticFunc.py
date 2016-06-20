# -*- coding: utf-8 -*-
"""
__author__ = 'Sunny'
__mtime__ = '4/15/2016'

                ┏┓     ┏┓
              ┏┛┻━━━┛┻┓
             ┃     ☃     ┃
             ┃ ┳┛  ┗┳  ┃
            ┃     ┻     ┃
            ┗━┓     ┏━┛
               ┃     ┗━━━┓
              ┃  神兽保佑   ┣┓
             ┃　永无BUG！  ┏┛
            ┗┓┓┏━┳┓┏┛
             ┃┫┫  ┃┫┫
            ┗┻┛  ┗┻┛
"""
import hashlib
import time
from datetime import datetime,timedelta
from math import radians, cos, sin, asin, sqrt,acos

class ErrorCode():
    NoneData = 1002                  # 没有数据
    DataUnSave = 1003                # 数据无法保存
    JsonError = 1004                 #接收的JSON格式出错
    MethodError = 1006               #错误的请求方式
    Error404 = 404                  #404

    ParameterError = 1100            #参数错误
    ParameterMiss = 1101             #参数缺失
    ErrorRequest = 1102              #错误的请求

    ErrorFindCode = 2000             #未识别错误码

    ERROR_MESSAGE = {

        NoneData: u"没有数据",

        DataUnSave: u"数据无法保存",

        JsonError : u"接收的JSON格式出错",

        MethodError : u"请求方式出错",

        ParameterError: u"不合法的参数",

        ParameterMiss: u"参数缺失",

        ErrorRequest : u"请求错误",

        ErrorFindCode : u"未识别错误码",

        Error404 : u"无效的url"
    }

#设置返回值
#forUser是显示给用户看的文字，forWorker是显示提供给后台程序员看的字段
#ret代表成功或者失败，data代表返回值，result代表错误代码
def Set_return_dicts(data=None,msg='',code=200,ret='success',Json=False):
    if data == None:
       ret = 'failure'
       data = {'value':'error'}
    return_dicts = {
        'data' : data,
        'code' : code,
        'ret' : ret,
        'version' : '1.0',
        'msg' : msg,
        'Json':Json
    }
    return return_dicts
