# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql 
class CrawlLagouPipeline(object):
    def process_item(self, item, spider):  
        # 如果爬虫名是movie  
        if spider.name == 'lagou':  
            try:  
                self.cursor.execute("insert into Lagou (city, companyName, companySize, district, \  
                 linestaion, positionName, jobNature, education, salary, workYear, showTime) \  
                        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (item['city'], item['companyFullName'], \  
                        item['companySize'], item['district'], item['linestaion'], item['positionName'], \  
                        item['jobNature'], item['education'], item['salary'], item['workYear'], item['createTime']))  
                self.conn.commit()  
            except pymysql.Error:  
                print("Error%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" % (item['city'], item['companyFullName'], \  
                        item['companySize'], item['district'], item['linestaion'], item['positionName'],\  
                        item['jobNature'], item['education'], item['salary'], item['workYear'], item['createTime']))  
            return item  