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
from Configs.StaticFunc import ErrorCode

class ApiException(Exception):
    '''全局错误码exception，搭配ErrorCode使用'''
    @staticmethod
    def get_message(errorCode):
        return ErrorCode.ERROR_MESSAGE.get(errorCode, 2000)

    @staticmethod
    def get_error_result(errorCode):
        return {
            "msg": ApiException.get_message(errorCode),
            "errorCode": str(errorCode),
        }

    @property
    def error_result(self):
        return self.get_error_result(self.errorCode)

    def __init__(self, errorCode=None):
        self.errorCode = errorCode
        self.message = self.get_message(self.errorCode)
