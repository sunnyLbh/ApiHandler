# -*- coding: utf-8 -*-
"""
__author__ = 'Sunny'
__mtime__ = '5/27/2016'

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
from Control.BaseHandler import Base_Handler
from Configs.StaticFunc import Set_return_dicts,ErrorCode
from Configs.MyExecption import ApiException
import requests
import json
class Main_Handler(Base_Handler):
  def __init__(self,application,request,**kwargs):
    super(Main_Handler,self).__init__(application,request,**kwargs)
    self.func = self.Main
    self.html = 'main.html'

  def makeList(self,resultList,result,padding):
      result.append({'value':'[','type':'start','padding':padding*20})
      for number in range(len(resultList)):
          if type(resultList[number]) not in [list,dict]:
              if type(resultList[number]) == str:
                  result.append({'value':"\""+resultList[number]+"\"",'type':'listStr',
                                 'padding':(padding+1)*20,'valueClass':'text-danger'})
              elif type(resultList[number]) in [int,float]:
                  result.append({'value':resultList[number],'type':'listStr',
                                 'padding':(padding+1)*20,'valueClass':'text-primary'})

          elif type(resultList[number]) == list:
              self.makeList(resultList[number],result,padding+1)

          elif type(resultList[number]) == dict:
              self.makeDick(resultList[number],result,padding+1)
      result.append({'type':'end','value':']','padding':padding*20})


  def makeDick(self,resultDick,result,padding):
      result.append({'type':'start','value':'{','padding':padding*20})
      for k,v in resultDick.items():
          if type(v) not in [list,dict]:
              if type(v) == str:
                  result.append({'key':"\""+k+"\"",'value':"\""+v+"\"",'type':'dictStr',
                                 'padding':(padding+1)*20,'valueClass':'text-danger'})
              elif type(v) in [int,float]:
                  result.append({'key':"\""+k+"\"",'value':v,'type':'dictStr',
                                 'padding':(padding+1)*20,'valueClass':'text-primary'})

          elif type(v) == list:
              result.append({'key':"\""+k+"\"",'type':'list','padding':(padding+1)*20})
              self.makeList(v,result,padding+1)

          elif type(v) == dict:
              result.append({'key':"\""+k+"\"",'type':'dict','padding':(padding+1)*20})
              self.makeDick(v,result,padding+1)

      result.append({'type':'end','value':'}','padding':padding*20})


  def Main(self,getData={}):
    result = dict()
    try:
        if getData:
            url = getData.get('url').replace(' ','')
            if not url.startswith('http://'):
                url = 'http://' + url
            method = getData.get('method')
            try:
                if getData.get('data'):
                    data = getData.get('data').replace(' ','').replace('\\r','').replace('\\n','')
                    data = json.loads(data)
            except:
                raise ApiException(ErrorCode.JsonError)

            result = dict()
            try:
                if method == 'get':
                    req = requests.get(url)
                elif method == 'post':
                    req = requests.post(url=url,data=json.dumps(data))
                elif method == 'delete':
                    req = requests.delete(url=url)
                elif method == 'put':
                    req = requests.put(url=url,data=json.dumps(data))
                else:
                    raise
            except:
                raise ApiException(ErrorCode.ErrorRequest)
            try:
                content = json.loads(req.content.decode())
            except:
                raise ApiException(ErrorCode.Error404)
            result['url'] = req.url

            result['contentType'] = req.headers.get('content-type')
            result['statusCode'] = req.status_code
            result['method'] = method.upper()
            contentList = list()
            self.makeDick(content,contentList,1)
            result['content'] = contentList
            return Set_return_dicts(data=result)
        else:
            return Set_return_dicts(data={'value':'success'})

    except ApiException as e:
       result['contentType'] = 'application/json'
       result['statusCode'] = 500
       content = Set_return_dicts(msg=e.error_result['msg'],
                               code=e.error_result['errorCode'])
       contentList = list()
       self.makeDick(content,contentList,1)
       result['content'] = contentList
       result['method'] = method.upper()
       result['url'] = url
       return Set_return_dicts(data=result)