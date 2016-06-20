# -*- coding: utf-8 -*-
"""
__author__ = 'sunny'
__mtime__ = '15/10/20'

　            ┏━┓　 ┏━┓+ +
 　　　　　　　┏┛ ┻━━━┛ ┻┓ + +
 　　　　　　　┃　　　　　 ┃ 　
 　　　　　　　┃　　　━　　┃ ++ + + +
 　　　　　　 ████━████  ┃+
 　　　　　　　┃　　　　　 ┃ +
 　　　　　　　┃　　┻　　  ┃
 　　　　　　　┃　　　　　 ┃ + +
 　　　　　　　┗━┓　　　┏━┛
 　　　　　　　　┃　　　┃　　　　　　　　　　　
 　　　　　　　　┃　　　┃ + + + +
 　　　　　　　　┃　　　┃　　　　Code is far away from bug with the animal protecting　　　　　　　
 　　　　　　　　┃　　　┃ + 　　　　
 　　　　　　　　┃　　　┃
 　　　　　　　　┃　　　┃　　+　　　　　　　　　
 　　　　　　　　┃　 　　┗━━━┓ + +
 　　　　　　　　┃ 　　　　　 ┣┓
 　　　　　　　　┃ 　　　　　 ┏┛
 　　　　　　　　┗┓┓┏━━┳┓┏━━┛ + + + +
 　　　　　　　　 ┃┫┫　┃┫┫
 　　　　　　　　 ┗┻┛　┗┻┛+ + + +

"""
import tornado
from tornado import web,gen,ioloop
import time
import json
from Configs.MyExecption import ApiException
from Configs import StaticFunc

class Base_Handler(web.RequestHandler):
   def __init__(self,application,request,**kwargs):
     super(Base_Handler,self).__init__(application,request,**kwargs)
     self.__keyWord = None
     self.func = None
     self.html = None

   def set_default_headers(self):
     self.set_header('Access-Control-Allow-Origin','*')
     self.set_header('Access-Control-Allow-Headers','*')
     # self.set_header('Content-type','application/json')

   def get_all_argument(self):
     argument = self.request.arguments
     result = dict()
     for name,value in argument.items():
       if len(value) == 1:
         result[name] = value[0].decode()
       else:
         result[name] = value
     return result

   @web.asynchronous
   @gen.coroutine
   def get(self,*args,**kwargs):
       # try:
       yield tornado.gen.Task(ioloop.IOLoop.instance().add_timeout,time.time())
       get_result = self.get_all_argument()
       if self.func:
           print('get:',get_result)
           result = self.func(get_result)

           print ("get_send:",result)
           if result.get('Json'):
               self.write(result)
           else:
               return self.render(self.html,result=result.get('data',{}))
       else:
           return self.render(self.html)

       # except:
       #      result = StaticFunc.Set_return_dicts(forWorker=StaticFunc.ErrorCode.ErrorRequest,forUser='请求错误',
       #              result=StaticFunc.ErrorCode.ERROR_MESSAGE.get(StaticFunc.ErrorCode.ErrorRequest))
       #
       #      self.write(result)


   @web.asynchronous
   @gen.coroutine
   def post(self,*args,**kwargs):
     # try:
         yield tornado.gen.Task(ioloop.IOLoop.instance().add_timeout,time.time())
         result = dict()
         get_result = self.get_all_argument()
         print ('post:{}'.format(get_result))
         if self.func:
            result = self.func(get_result)
            print ('post_send:{}'.format(result))
            if result.get('Json'):
               self.write(result)
            else:
               return self.render(self.html,result=result.get('data'))
         else:
              return self.render(self.html)

     # except:
     #      result = StaticFunc.Set_return_dicts(forWorker=StaticFunc.ErrorCode.ErrorRequest,forUser='请求错误',
     #              result=StaticFunc.ErrorCode.ERROR_MESSAGE.get(StaticFunc.ErrorCode.ErrorRequest))
     #      self.write(result)

