#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from lxml import etree
import re

HEADERS = {
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36"
    "(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
}

START_URL = 'https://nj.lianjia.com/zufang/'


def get_all_areas():
    print('-----spider begin----------')
    response = requests.get(START_URL, headers=HEADERS)
    content = etree.HTML(response.text)
    areas = content.xpath("//dd[@data-index='0']//div[@class='option-list']/a/text()")
    # print(areas)
    '''
    ['不限', '鼓楼', '建邺', '秦淮', '玄武', '雨花台', '栖霞', '江宁', '浦口', '六合', '溧水', '高淳']
    '''
    areas_link = content.xpath("//dd[@data-index='0']//div[@class='option-list']/a/@href")
    # print(areas_link)
    '''
    ['/zufang/', '/zufang/gulou/', '/zufang/jianye/', '/zufang/qinhuai/', '/zufang/xuanwu/', '/zufang/yuhuatai/',
    '/zufang/qixia/', '/zufang/jiangning/', '/zufang/pukou/', '/zufang/liuhe/', '/zufang/lishui/', '/zufang/gaochun/']
    '''
    for i in range(9, len(areas)):
        area = areas[i]
        area_link = areas_link[i]
        link = 'https://nj.lianjia.com' + area_link
        print('---Begin to grasp area: {area} ------'.format(area=area))
        get_each_area(area, link)


def get_each_area(area, area_url):
    response2 = requests.get(area_url, headers=HEADERS)
    try:
        total_pages = int(re.findall("page-data='{\"totalPage\":(\d+)", response2.text)[0])
    except:
        total_pages = 0
    if total_pages > 0:
        for page in range(1, total_pages+1):
            each_area_url = area_url + 'pg/' + str(page)
            print('--- Begin grasp , page: {page}, area:{area} ------'.format(page=page, area=area))
            get_each_page_house(area, each_area_url)
    else:
        print('没有房源可租，，，')


def get_each_page_house(area, url):
    response3 = requests.get(url, headers=HEADERS)
    content = etree.HTML(response3.text)
    for i in range(30):
        try:
            title = content.xpath("//div[@class='where']/a/span/text()")[i]
            zone = content.xpath("//div[@class='where']/span[1]/span/text()")[i]
            meters = content.xpath("//div[@class='where']/span[2]/text()")[i]
            meter = re.findall("(\d+)", meters)[0]  # 去掉平方两个字
            area_details = content.xpath("//div[@class='con']/a/text()")[i]
            area_detail = re.findall("([\u4E00-\u9FA5]+)租房", area_details)[0] #[\u4E00-\u9FA5]:匹配中文
            price = content.xpath("//div[@class='price']/span/text()")[i]
            with open('链家南京.txt', 'a', encoding='utf-8') as f:
                f.write(area + '\t' + title + '\t' + zone + '\t' + meter + '\t' +
                        area_detail + '\t' + price + '\n')
        except:
            pass


if __name__ == '__main__':
    get_all_areas()