# -*- coding: utf-8 -*-
import scrapy
import pymysql
import json

class BossCityCrawlSpider(scrapy.Spider):
    name = 'boss_city_crawl'
    allowed_domains = ['zhipin.com']
    start_urls = ['https://www.zhipin.com/common/data/city.json']

    def parse(self, response):
        print(,'lidongdong08171001')
        # for tr in response.xpath('.//table[2]/tr'):
        #     # print(tr.xpath('.//td[1]/div/span/text()').extract()[0],'lidongdong')
        #     py = tr.xpath('.//td[1]/div/span/text()').extract()[0]
        #     # print(py)
        #     for li in tr.xpath('.//td[2]/ul/li'):
        #         city = li.xpath('.//a/text()').extract()[0]
        #         # print(city)
        #         param = [city,py]
        #         with pymysql.connect(database='lagouone', host='localhost', user='root', password='marphy0817', charset='utf8') as cursor:
        #             # 向表中插入数据的sql语句
        #             sql_insert = '''
        #                     insert into citylist (city, letter) VALUES (
        #                     %s, %s
        #                     )
        #                 '''
        #             try:
        #                 cursor.execute(sql_insert, param)
        #             except:
        #                 print("============数据库插入失败！=============")
        #                 pass 
                    # sql = "select city from citylist"  
                    # try:  
                    #     cursor.execute(sql)    #执行sql语句  
                    #     results = cursor.fetchall()
                    #     for row in results:
                    #         print(row[0])
                    # except:
                    #     pass
                    # sql = "select city from citylist"  
                    # try:  
                    #     cursor.execute(sql)    #执行sql语句  
                    #     results = cursor.fetchall()
                    #     print(results)
                    # except:
                    #     pass