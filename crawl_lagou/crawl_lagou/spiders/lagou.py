# -*- coding: utf-8 -*-
import scrapy


# class LagouSpider(scrapy.Spider):
#     name = 'lagou'
#     allowed_domains = ['lagou.com']
#     start_urls = ['http://lagou.com/']

#     def parse(self, response):
#         pass
# # -*-coding:utf-8-*-  
  
from scrapy.spiders import Spider  
from scrapy import FormRequest  
from scrapy.selector import Selector  
# from crawl_lagou.items import LagouItem  
  
import random  
import json  
import time  
  
class LagouItem(scrapy.Item):  
    # 城市  
    city = scrapy.Field()  
  
    # 公司  
    companyFullName = scrapy.Field()  
  
    # 公司规模  
    companySize = scrapy.Field()  
  
    # 地区  
    district = scrapy.Field()  
  
    # 教育程度  
    education = scrapy.Field()  
  
    # 地点  
    linestaion = scrapy.Field()  
  
    # 招聘职务  
    positionName = scrapy.Field()  
  
    # 招聘要求  
    jobNature = scrapy.Field()  
  
    # 工资  
    salary = scrapy.Field()  
  
    # 工作经验  
    workYear = scrapy.Field()  
  
    # 岗位发布时间  
    createTime = scrapy.Field() 

class LagouSpider(Spider):  
    # 爬虫名字，重要  
    name = 'lagou'  
    headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',  
                'Referer': 'https://www.lagou.com/jobs/list_Python?labelWords=&fromSearch=true&suginput=1'}  
    allow_domains = ['lagou.com']  
    url = "https://www.lagou.com/jobs/positionAjax.json?" # &needAddtionalResult=true&isSchoolJob=0"  
    page = 1  
    allpage = 0  
  
    def start_requests(self):  
  
        yield FormRequest(self.url, headers=self.headers,  
                                formdata={  
                                    'first': 'false',  
                                    'pn': str(self.page),  
                                    'kd': 'Python',  
                                    'city':'广州'  
  
                                }, callback=self.parse  
                              )  
  
    def parse(self, response): 
        print(response.body.decode('utf-8'),'lidongdongdongdong') 
        item = LagouItem()  
        data = json.loads(response.body.decode('utf-8'))  
        result = data['content']['positionResult']['result']  
        totalCount = data['content']['positionResult']['totalCount']  
        resultSize = data['content']['positionResult']['resultSize']  
        for each in result:  
            item['city'] = each['city']  
            item['companyFullName'] = each['companyFullName']  
            item['companySize'] = each['companySize']  
            item['district'] = each['district']  
            item['education'] = each['education']  
            item['linestaion'] = each['linestaion']  
            item['positionName'] = each['positionName']  
            item['jobNature'] = each['jobNature']  
            item['salary'] = each['salary']  
            item['createTime'] = each['createTime']  
            item['workYear'] = each['workYear']  
            yield item  
        time.sleep(5)
  
        if int(resultSize):  
            self.allpage = int(totalCount) / int(resultSize) + 1  
            if self.page < self.allpage:  
                self.page += 1  
                yield FormRequest(self.url, headers=self.headers,  
                    formdata={  
                        'first': 'false',  
                        'pn': str(self.page),  
                        'kd': 'Python',  
                        'city':'广州'  
                    }, callback=self.parse  
                    )  