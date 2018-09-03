# -*- coding: utf-8 -*-
import scrapy


class CrawlerjsSpider(scrapy.Spider):
    name = 'Crawlerjs'
    allowed_domains = ['www.jianshu.com']
    start_urls = ["https://www.jianshu.com/search/do?q=%E5%B0%8F%E7%A8%8B%E5%BA%8F&type=note&page=1&order_by=default"]
    # url = "https://www.jianshu.com/search/do"
    # inputCon = input("请输入要查询的问题：")
    # print(inputCon)
    headers = {'Referer':'https://www.jianshu.com/search?q=%E5%B0%8F%E7%A8%8B%E5%BA%8F&page=1&type=note',               'Origin':'https://www.jianshu.com',                'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
        'Accept':'application/json, gzip, deflate, br, zh-CN,zh;q=0.9',
        'Cookie':'read_mode=day; default_font=font2; locale=zh-CN; _m7e_session=a6a215704a0d038733652a976ef512dc; Hm_lvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1533799464,1535706151,1535958599; Hm_lpvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1535958599; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221653b72051978d-081b9b4620e30b-34677908-1764000-1653b72051a129%22%2C%22%24device_id%22%3A%221653b72051978d-081b9b4620e30b-34677908-1764000-1653b72051a129%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.google.com.hk%2F%22%2C%22%24latest_referrer_host%22%3A%22www.google.com.hk%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_utm_source%22%3A%22desktop%22%2C%22%24latest_utm_medium%22%3A%22search-trending%22%7D%7D; signin_redirect=https%3A%2F%2Fwww.jianshu.com%2Fsearch%3Fq%3D%25E5%25B0%258F%25E7%25A8%258B%25E5%25BA%258F%26page%3D1%26type%3Dnote'
        },

    # def  start_requests(self):
    #     yield FormRequest(self.url)
    # 重写start_request函数
    def start_requests(self):
        '''
        重写start_requests函数，发送自定义请求

        :return:
        return scrapy.Request(self.start_urls[0],method='POST
        '''
        # FormRequest是专门用来发送post请求的函数
        yield scrapy.FormRequest(
            self.start_urls[0],
            # formdata为字典，
            formdata={ 'q': '小程序',
            'type': 'note',
            'page': '1',
            'order_by': 'default'},
            # 重写了start_requests函数，记得以一定要重定义callback函数，使其指向parse，进行数据处理
            callback = self.parse
        )

    def parse(self, response):
        print(response.body,'dlddddddd')
        pass
