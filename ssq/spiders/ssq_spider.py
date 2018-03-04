# -*- coding: utf-8 -*-

import scrapy
import re

class SsqSpider(scrapy.Spider):
    name = "ssq_data"
    allowed_domains = ["500.com"]
    start_urls = []
    # for i in range(15001, 15200):
    #     start_urls.append("http://kaijiang.500.com/shtml/ssq/"+str(i)+".shtml")
    #
    # for i in range(16001, 16200):
    #     start_urls.append("http://kaijiang.500.com/shtml/ssq/"+str(i)+".shtml")
    #
    # for i in range(17001, 17200):
    #     start_urls.append("http://kaijiang.500.com/shtml/ssq/"+str(i)+".shtml")
    #
    for i in range(18001, 18200):
        start_urls.append("http://kaijiang.500.com/shtml/ssq/"+str(i)+".shtml")

    # start_urls = [
    #     "http://kaijiang.500.com/shtml/ssq/18002.shtml"
    # ]

    def parse(self, response):
        result = []
        filename = response.url.split("/")[-1]
        content = str(response.body)
        content_list = content.split('<div class="ball_box01">')[1].split('</ul>')
        pattern = re.compile(r'\d+')
        per_result = pattern.findall(content_list[0])
        print(per_result)

        # with open(filename, 'wb') as f:
        #     f.write(response.body)
