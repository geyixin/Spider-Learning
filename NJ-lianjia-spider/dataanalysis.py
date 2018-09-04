#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import pandas as pd
from pyecharts import Bar, Line, Overlap, Pie

f = open('链家南京.txt', 'r', encoding='utf-8')

df = pd.read_csv(f, sep='\t', names=['area', 'title', 'zone', 'meter', 'area_detail', 'price'])

# print(df)
# print(df.describe())

#  南京市各个主要路段租房均价和数量
area_detail_price = df.groupby(['area_detail'])
house = area_detail_price['price'].agg(['mean', 'count'])
# print(len(house))
# print(house)
"""
# house显示就是下面这样 ：
                     mean  count
area_detail                     
万寿            2200.000000    138
万达广场          5602.824859    177
三牌楼           3200.000000    182
东山镇           2866.666667    261
"""
house.reset_index(inplace=True)
area_detail_price_count = house.sort_values('count', ascending=False)[0:45]
# print(area_detail_price_mean)
attr = area_detail_price_count['area_detail']
v1 = area_detail_price_count['count']
v2 = area_detail_price_count['mean']
line = Line("南京主要路段房屋均价")
line.add("均价", attr, v2, xaxis_rotate=80, mark_point=['min','max'], line_color='lightblue',
         xaxis_interval=0, line_width=4)
bar = Bar("南京主要路段房屋数量&均价")  # 会覆盖掉 Line("南京主要路段房屋均价") 的文字
bar.add("路段", attr, v1, xaxis_rotate=90, xaxis_interval=0)
overlap = Overlap()
overlap.add(bar)
overlap.add(line, yaxis_index=1,is_add_yaxis=True)
overlap.render('南京主要路段房屋数量&均价.html')


# 不同价格区间内房源数量
# area_price = df[['area', 'price']]  # 只取 area、price 两列
bins = [0,1000,1500,2000,2500,3000,4000,5000,6000,8000,10000]
level = ['0-1000', '1000-1500', '1500-2000', '2000-2500', '2500-3000',
         '3000-4000', '4000-5000', '5000-6000', '6000-8000', '8000以上']
price_level = pd.cut(df['price'], bins=bins, labels=level).value_counts().sort_index()
"""
value_counts():统计value出现次数，在此即为价格区间内的房源数量
sort_index()：以value排序
bins是统计的界限
labels是横坐标的显示结果。labels一定要和bins对应起来。
"""
# print(area_price_level)
attr = price_level.index
v1 = price_level.values
"""
每个价格区间内的数量: [ 526  194  999 2488 3179 2675 1680 1259 2113  576]
"""

bar = Bar("价格区间&房源数量")
bar.add("", attr, v1, xaxis_rotate=30)
overlap = Overlap()
overlap.add(bar)
overlap.render('价格区间&房源数量.html')


# 房屋面积分布
bins = [0,30,60,90,120,150,200,300,400,700]
level = ['0-30', '30-60', '60-90', '90-120', '120-150', '150-200',
         '200-300', '300-400', '400+']
meter_level = pd.cut(df['meter'], bins=bins, labels=level).value_counts().sort_index()
# print(meter_level)
attr = meter_level.index
v1 = meter_level.values
pie = Pie("房屋面积分布", title_pos='center')
pie.add("", attr, v1, legend_pos="left", legend_orient="vertical",
        is_label_show=True, radius=[40, 75])
"""
radius=[40, 75]:            空心圆
legend_pos="left":          legend放在左边
legend_orient="vertical"：   legend垂直放置
"""
overlap = Overlap()
overlap.add(pie)
overlap.render('房屋面积分布.html')