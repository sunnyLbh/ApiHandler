# -*- coding: utf-8 -*-
"""
__author__ = 'Sunny'
__mtime__ = '4/14/2016'

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
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define,options
import os
from Configs.Urls import route

define("port",default=8888,help="run for the backend",type="int")
if __name__ == "__main__":
  settings = {'template_path' : os.path.join(os.path.dirname(__file__),"templates"),
              'static_path' : os.path.join(os.path.dirname(__file__),"static"),}

  route.append((r"/(favicon\.ico)", tornado.web.StaticFileHandler, dict(path=settings['static_path'])))

  tornado.options.parse_command_line()
  app = tornado.web.Application(
   handlers = route,
   **settings
  )
  http_server = tornado.httpserver.HTTPServer(app)
  http_server.listen(options.port)
  tornado.ioloop.IOLoop.instance().start()
