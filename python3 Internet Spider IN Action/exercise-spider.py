#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
__author__ = 'geyixin'

# '''
# tesserocr
# '''
# import tesserocr
# from PIL import Image

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

# import tornado.ioloop
# import tornado.web
#
# class MainHandler(tornado.web.RequestHandler):
#     def get(self):
#         self.write("Hello world!")
#
# def make_app():
#     return tornado.web.Application([(r"/", MainHandler), ])
#
# if __name__ == "__main__":
#     app = make_app()
#     app.listen(8888)
#     tornado.ioloop.IOLoop.current().start()
#

'''
带账号密码的界面
'''
# from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
# from urllib.error import URLError
#
# username = 'username'
# password = 'pwd'
#
# url = 'http://ids6.njupt.edu.cn/authserver/login?service=http://my.njupt.edu.cn/login.do'
#
# p = HTTPPasswordMgrWithDefaultRealm()
# p.add_password(None, url, username, password)
# auth_handler = HTTPBasicAuthHandler(p)
# opener = build_opener(auth_handler)
#
# try:
#     res = opener.open(url)
#     html = res.read().decode('utf-8')
#     print(html)
# except URLError as e:
#     print(e.reason)


'''
代理(貌似并没有啥用)
'''
# from urllib.error import URLError
# from urllib.request import ProxyHandler, build_opener
#
# proxy_hander = ProxyHandler({
#     'http': 'http://127.0.0.1:9743',
#     'https': 'http://127.0.0.1:9743',
# })
# opener = build_opener(proxy_hander)
# try:
#     res = opener.open('https://sh.lianjia.com/')
#     print(res.read().decode('utf-8'))
# except URLError as e:
#     print(e.reason)

'''
requests 中的cookie
'''
# import requests
#
# HEADERS = {
#     'Cookie': 'x',
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36"
#     "(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
# }
# r = requests.get("http://www.baidu.com", headers=HEADERS)
# print(r.text)
# for key, value in r.cookies.items():
#     print(key + '=' + value)
#

# from pyquery import PyQuery as pq
# res = pq(html)
# # res = pq(url='https://www.baidu.com')
# print(res('li'))

'''
json
'''
# import json
#
# str = '[{"a":1,"b":2},{"A":11,"B":22}]'
# print(type(str))
# data = json.loads(str)  # json编码
# print(data)
# print(type(data))
# print(data[0]['a'])
# print(data[1].get('A'))
# print(data[1].get('A', 2))
# print(data[1].get('C', 2))
# da = json.dumps(data)   # json解码
# print(da)
# print(type(da))

# import json
#
# str = '[{"a":1,"b":2},{"A":11,"B":22}]'
# with open('data.json', 'w', encoding='utf-8') as f:
#     f.write(json.dumps(str, indent=2, ensure_ascii=False))  # indent=2,缩进两个字符

'''
CSV
'''
#
# import csv
#
# with open('data.csv', 'w', newline='', encoding='utf-8') as cv:
#     writer = csv.writer(cv, delimiter=' ')
#     writer.writerow(['id', 'name', 'age'])
#     writer.writerow(['1', 'tom', '12'])
#     writer.writerow(['2', 'mike', '13'])
#     writer.writerows([['3', 'tt', '12'],['4', 'mm', '12']])


# import csv
#
# with open('data.csv', 'r', encoding='utf-8') as cv:
#     read = csv.reader(cv)
#     for row in read:
#         print(row)

# import pandas
#
# df = pandas.read_csv('data.csv')
# print(df)
#
























































