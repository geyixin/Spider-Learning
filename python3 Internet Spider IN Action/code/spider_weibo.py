#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
__author__ = 'geyixin'

"""
爬取带有Ajax的微博页面
"""

from urllib.parse import urlencode
import requests
from pyquery import PyQuery as pq
from pymongo import MongoClient

URL = 'https://m.weibo.cn/api/container/getIndex?'

headers = {
    'Host': 'm.weibo.cn',
    'Referer': 'https://m.weibo.cn/u/2830678474',
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
    'X-Requested-With': 'XMLHttpRequest',
}
client = MongoClient()
db = client['weibo']
collection = db['weibo']
max_page = 10


def get_pages(page):
    params = {
        'type': 'uid',
        'value': '2830678474',
        'containerid': '1076032830678474',
        'page': page
    }
    url = URL + urlencode(params)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:     # 200表示服务器已成功处理了请求
            return response.json()
    except requests.ConnectionError as e:
        print('Error', e.args)


def paser_page(json):
    if json:
        items = json.get('data').get('cards')
        for index, item in enumerate(items):
            if page == 1 and index == 1:
                continue
            else:
                item = item.get('mblog')
                weibo = {}
                weibo['id'] = item.get('id')
                weibo['text'] = pq(item.get('text')).text()
                weibo['attitudes'] = item.get('attitudes_count')
                weibo['comments'] = item.get('comments_count')
                weibo['reposts'] = item.get('reposts_count')
                yield weibo


def save_to_mongdb(res):
    if collection.insert(res):
        print('Saved!')


if __name__ == '__main__':
    for page in range(1, max_page+1):
        json = get_pages(page)
        ress = paser_page(json)
        for res in ress:
            print(res)
            save_to_mongdb(res)
































