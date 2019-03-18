#-*- coding:utf-8 -*-
import jieba
import json
# 获得文本的所有信息
with open('te_pipline1.json','r') as f:
    data = f.readlines()
# data_title = data[:]['title']
title_sum = ''
for i in data:
    title = i.split('title": "')[1][:-3]
    # print(title)
    title_sum = title_sum+title
# print('title_sum',title_sum)

#利用结巴分词模块，获得词频统计
word_list = jieba.cut(title_sum,True)


#利用word词云模块，来进行信息提取
import wordcloud
w = wordcloud.WordCloud(width=800,height=800,background_color='white',font_path='c:\windows\Fonts\simhei.ttf',stopwords=['amp','mdash'])#CREATE a wordcloud OBJECT
w.generate(title_sum)
w.to_file('title_nowcoder_emplyee_3.jpg')


# jieba.cut()