#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
__author__ = 'geyixin'

'''
tesserocr
'''
import tesserocr
from PIL import Image

# image = Image.open('22.jpg')
# res = tesserocr.image_to_text(image)
# print(res)

'''
flask
'''

# from flask import Flask
# app = Flask(__name__)
#
# @app.route("/")
# def hello():
#     return "Hello World"
#
# if __name__ == "__main__":
#     app.run()

'''
tornado
'''

import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello world!")

def make_app():
    return tornado.web.Application([(r"/", MainHandler), ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()











