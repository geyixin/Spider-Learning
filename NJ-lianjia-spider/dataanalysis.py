#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
__author__ = 'geyixin'


import pandas as pd
from pyecharts import Bar, Line, Overlap, Pie


f = open('链家南京租房.txt', 'r', encoding='UTF-8')

df = pd.read_csv(f, sep=',', header=None, encoding='utf-8',
                 names=['area', 'title', 'room_type', 'square', 'position',
                        'detail_place', 'floor', 'total_floor', 'price', 'house_year'])

print(df.describe())


# 北京路段_房屋均价分布图

detail_place = df.groupby(['detail_place'])  # 按detail_place分组 基于 行/index 的聚合
house_com = detail_place['price'].agg(['mean','count'])  # agg(['mean','count'])，基于列的聚合操作
# print('第一次：',house_com)
house_com.reset_index(inplace=True)
# print('第二次：',house_com)   # reset_index可使dataframe数据规整
detail_place_main = house_com.sort_values('count',ascending=False)[0:20]
# sort_values('A',ascending=False)，按A列降序排。
# print(detail_place_main)

attr = detail_place_main['detail_place']
# print('第一次attr:', attr)
v1 = detail_place_main['count']
# print('V1:', v1)
v2 = detail_place_main['mean']
# print('v2:', v2)

line = Line("南京主要路段房租均价")
line.add("路段",attr,v2,is_stack=True,xaxis_rotate=30,yaxix_min=4.2,
    mark_point=['min','max'],xaxis_interval=0,line_color='lightblue',
    line_width=4,mark_point_textcolor='black',mark_point_color='lightblue',
    is_splitline_show=False)

bar = Bar("南京主要路段房屋数量")
bar.add("路段",attr,v1,is_stack=True,xaxis_rotate=30,yaxix_min=4.2,
    xaxis_interval=0,is_splitline_show=False)

# Overlap 结合不同类型图表叠加画在同张图上
overlap = Overlap()
overlap.add(bar)
overlap.add(line,yaxis_index=1,is_add_yaxis=True)  # is_add_yaxis=True,增加一排y坐标
overlap.render('南京路段_房屋均价分布图.html')
# overlap.render()


# 房源价格区间分布图
price_info = df[['area', 'price']]
# print('price_info', price_info)

# 对价格分区
bins = [0,1000,1500,2000,2500,3000,4000,5000,6000,8000,10000]
level = ['0-1000','1000-1500', '1500-2000', '2000-3000', '3000-4000',
         '4000-5000', '5000-6000', '6000-8000', '8000-1000','10000以上']
price_stage = pd.cut(price_info['price'], bins=bins, labels=level).value_counts().sort_index()
# print('price_stage:', price_stage)
attr = price_stage.index
# print('对价格分区attr:', attr)
v1 = price_stage.values

bar = Bar("价格区间&房源数量分布")
bar.add("",attr,v1,is_stack=True,xaxis_rotate=30,yaxix_min=4.2,
    xaxis_interval=0,is_splitline_show=False)

overlap = Overlap()
overlap.add(bar)
overlap.render('价格区间&房源数量分布.html')
# overlap.render() # 生成html格式的图


# 房屋面积分布
bins = [0,30,60,90,120,150,200,300,400,700]
level = ['0-30', '30-60', '60-90', '90-120', '120-150', '150-200',
         '200-300','300-400','400+']
df['square_level'] = pd.cut(df['square'], bins=bins, labels=level)  # 在 df 中多加一列

# print('df:', df)

df_digit = df[['area', 'room_type', 'square', 'position', 'total_floor',
               'floor', 'house_year', 'price', 'square_level']]
s = df_digit['square_level'].value_counts()

# print('s:', s)

attr = s.index
# print('房屋面积attr:', attr)
v1 = s.values
# print('v1:', v1)

pie = Pie("房屋面积分布", title_pos='center')

pie.add("",attr,v1,radius=[40, 75],label_text_color=None,
        is_label_show=True,legend_orient="vertical",legend_pos="left",)

overlap = Overlap()
overlap.add(pie)
overlap.render('房屋面积分布.html')


# 房屋面积&价位分布
bins = [0,30,60,90,120,150,200,300,400,700]
level = ['0-30', '30-60', '60-90', '90-120', '120-150', '150-200',
         '200-300','300-400','400+']
df['square_level'] = pd.cut(df['square'], bins=bins, labels=level)

df_digit = df[['area', 'room_type', 'square', 'position', 'total_floor', 'floor',
               'house_year', 'price', 'square_level']]

square = df_digit[['square_level','price']]
prices = square.groupby('square_level').mean().reset_index()
amount = square.groupby('square_level').count().reset_index()

attr = prices['square_level']
v1 = prices['price']

pie = Pie("房屋面积&价位分布-pie", title_pos='center')
pie.add("", attr, v1, is_label_show=True,legend_orient="vertical", legend_pos="left")
pie.render('房屋面积&价位分布-pie.html')

bar = Bar("房屋面积&价位分布-bar")
bar.add("",attr,v1,is_stack=True,xaxis_rotate=30,yaxix_min=4.2,
    xaxis_interval=0,is_splitline_show=False)

overlap = Overlap()
overlap.add(bar)
overlap.render('房屋面积&价位分布-bar.html')


