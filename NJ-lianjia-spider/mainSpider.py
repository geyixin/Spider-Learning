#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
__author__ = 'geyixin'

import requests
import time
import re
from lxml import etree


# 获取某市区域的所有链接
def get_areas(url):
    print('start grabing areas')
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'}
    resposne = requests.get(url, headers=headers)
    content = etree.HTML(resposne.text)
    # print('content:', content)  # <Element html at 0xc258c3a788>
    areas = content.xpath("//dd[@data-index = '0']//div[@class='option-list']/a/text()")
    print('areas:',areas)
    areas_link = content.xpath("//dd[@data-index = '0']//div[@class='option-list']/a/@href")
    print('areas_link:', areas_link)
    for i in range(1, len(areas)):
        area = areas[i]
        area_link = areas_link[i]
        link = 'https://nj.lianjia.com' + area_link
        print('link:', link)
        print("开始抓取页面")
        get_pages(area, link)


# 通过获取某一区域的页数，来拼接某一页的链接
def get_pages(area, area_link):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'}
    resposne = requests.get(area_link, headers=headers)
    try:
        pages = int(re.findall("page-data=\'{\"totalPage\":(\d+),\"curPage\"", resposne.text)[0])
        print("这个区域有" + str(pages) + "页")
        for page in range(1, pages + 1):
            url = area_link + 'pg/' + str(page)
            print('url:', url)
            print("开始抓取" + str(page) + "的信息")
            get_house_info(area, url)
    except:
        return


# 获取某一区域某一页的详细房租信息
def get_house_info(area, url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'}
    time.sleep(2)

    try:
        resposne = requests.get(url, headers=headers, timeout=10)
        content = etree.HTML(resposne.text)
        # total_rooms = content.xpath("//div[@class='list-head clear']/h2/span/text()")
        # print('total_rooms:', total_rooms[0])
        # info = []
        # if page < pages:
        #     LL = 30
        # if page == pages:
        #     LL = total_rooms - (pages-1)*30
        # print('LL:', LL)
        # print('page,pages:', page, pages)
        for i in range(30):
            title = content.xpath("//div[@class='where']/a/span/text()")[i]
            # print('title:', title)
            room_type = content.xpath("//div[@class='where']/span[1]/span/text()")[i]
            # print('room_type:', room_type)
            square = re.findall("(\d+)", content.xpath("//div[@class='where']/span[2]/text()")[i])[0]
            # print('square:',square)
            # pon = content.xpath("//div[@class='where']/span[3]/text()")[i]
            position = content.xpath("//div[@class='where']/span[3]/text()")[i].replace(" ", "")
            # print(pon, position)
            try:
                #  [\u4E00-\u9FA5] :中文的 unicode 编码范围 主要在 [\u4e00-\u9fa5]
                detail_place = \
                re.findall("([\u4E00-\u9FA5]+)租房", content.xpath("//div[@class='other']/div/a/text()")[i])[0]
            except Exception as e:
                detail_place = ""
            floor = re.findall("([\u4E00-\u9FA5]+)\(", content.xpath("//div[@class='other']/div/text()[1]")[i])[0]
            total_floor = re.findall("(\d+)", content.xpath("//div[@class='other']/div/text()[1]")[i])[0]
            try:
                house_year = re.findall("(\d+)", content.xpath("//div[@class='other']/div/text()[2]")[i])[0]
            except Exception as e:
                house_year = ""
            price = content.xpath("//div[@class='col-3']/div/span/text()")[i]
            # open('链家北京租房.txt', 'a', encoding='utf-8') 第二个参数是打开的模式
            # 'r'：只读（缺省。如果文件不存在，则抛出错误）
            # 'w'：只写（如果文件不存在，则自动创建文件）
            # 'a'：附加到文件末尾
            # 'r+'：读写
            with open('链家南京租房.txt', 'a', encoding='utf-8') as f:
                f.write(area + ',' + title + ',' + room_type + ',' + square + ',' + position +
                        ',' + detail_place + ',' + floor + ',' + total_floor + ',' + price + ',' + house_year + '\n')

            print('writing work has done!continue the next page')

    except Exception as e:
        print('ooops! connecting error, retrying.....')
        pass
        # time.sleep(20)
        # # return
        # return get_house_info(area, url)


def main():
    print('start!')
    url = 'https://nj.lianjia.com/zufang'
    get_areas(url)
    print('END----------------')


if __name__ == '__main__':
    main()