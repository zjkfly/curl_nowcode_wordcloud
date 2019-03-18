# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy import Item
from nowcoder.items import NowcoderItem
class NowcodeSpider(scrapy.Spider):
    name = 'nowcode'
    allowed_domains = ['www.nowcoder.com']
    start_urls = ['https://www.nowcoder.com/discuss?type=7&order=0']

    def parse(self, response):
        #换行符需要匹配
        res = re.findall('<div class="discuss-main clearfix">\n<a href="(.*?)"\ntarget="_blank">\n(.*?)\n<',response.text)
        is_end = re.findall('href="(.*?)">下一页</a></li>',response.text)
        for url_title in res:
            item = NowcoderItem()
            url1 = 'https://www.nowcoder.com'+url_title[0]
            # title = url_title[1]
            item['url'] = url1
            item['title'] = url_title[1]
            print('*'*20)
            yield item
        #判断是否到尾页
        if len(is_end):
            print('正在爬取网页','https://www.nowcoder.com'+is_end[0])
            yield scrapy.Request(url='https://www.nowcoder.com'+is_end[0],callback=self.parse)



