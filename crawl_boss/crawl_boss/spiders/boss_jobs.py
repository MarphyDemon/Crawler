# 搜索北京产品经理生活服务
# https://www.zhipin.com/job_detail/?query=&scity=101010100&industry=100007&position=110101
# 点击第二页
# https://www.zhipin.com/i100007-c101010100-p110101/h_101010100/?page=2&ka=page-2
# https://www.zhipin.com/i industry -c city -p position/h_ city /?page=2&ka=page-2

# -*- coding: utf-8 -*-
import scrapy
import pymysql
from scrapy.http import Request
import time

class BossJobsSpider(scrapy.Spider):
    name = 'boss_jobs'
    allowed_domains = ['zhipin.com']
    
    # start_urls = 'https://www.zhipin.com/i'+industry+'-c'+city+'-p'+position+'/h_'+city+'/?page='+page+'&ka=page-'+page
    # 发送 header，伪装为浏览器
    headers = {
        'x-devtools-emulate-network-conditions-client-id': "5f2fc4da-c727-43c0-aad4-37fce8e3ff39",
        'upgrade-insecure-requests': "1",
        'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'dnt': "1",
        'accept-encoding': "gzip, deflate",
        'accept-language': "zh-CN,zh;q=0.8,en;q=0.6",
        'cookie': "__c=1501326829; lastCity=101020100; __g=-; __l=r=https%3A%2F%2Fwww.google.com.hk%2F&l=%2F; __a=38940428.1501326829..1501326829.20.1.20.20; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1501326839; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1502948718; __c=1501326829; lastCity=101020100; __g=-; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1501326839; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1502954829; __l=r=https%3A%2F%2Fwww.google.com.hk%2F&l=%2F; __a=38940428.1501326829..1501326829.21.1.21.21",
        'cache-control': "no-cache",
        'postman-token': "76554687-c4df-0c17-7cc0-5bf3845c9831"
    }
# 获取城市
    # def getCity():
    #     with pymysql.connect(database='lagouone', host='localhost', user='root', password='marphy0817', charset='utf8') as cursor:
    #         sqlExit = "select name,code from bosscity"
    #         res = cursor.execute(sqlExit)
    #         results = cursor.fetchall()
    #         cityList = []
    #         for (i,j) in results:
    #             print(i,j)
    #             cityList.append(i,j)
    #     return cityList
    
    # def getIndustry():
    #     with pymysql.connect(database='lagouone', host='localhost', user='root', password='marphy0817', charset='utf8') as cursor:
    #         sqlExit = "select name,code from industry"
    #         res = cursor.execute(sqlExit)
    #         results = cursor.fetchall()
    #         industryList = []
    #         for (i,j) in results:
    #             print(i,j)
    #             industryList.append(i,j)
    #     return industryList
# 获取职位
    # def getPosition():
    #     with pymysql.connect(database='lagouone', host='localhost', user='root', password='marphy0817', charset='utf8') as cursor:
    #         sqlExit = "select name,code from post"
    #         res = cursor.execute(sqlExit)
    #         results = cursor.fetchall()
    #         positionList = []
    #         for (i,j) in results:
    #             print(i,j)
    #             positionList.append(i,j)
    #     return positionList
# 重写
    def start_requests(self):
        with pymysql.connect(database='lagouone', host='localhost', user='root', password='marphy0817', charset='utf8') as cursor:
            sqlPost = "select name,code from post"
            res1 = cursor.execute(sqlPost)
            positionList = cursor.fetchall()
            sqlCity = "select name,code from bosscity"
            res2 = cursor.execute(sqlCity)
            cityList = cursor.fetchall()
            sqlIndustry = "select name,code from industry"
            res3 = cursor.execute(sqlIndustry)
            IndustryList = cursor.fetchall()
            for (cityName,cityCode) in cityList:
                for (industryName,industryCode) in IndustryList:
                    for (positionName,positionCode) in positionList:
                        for page in range(1,11):
                            url = 'https://www.zhipin.com/i'+str(industryCode)+'-c'+str(cityCode)+'-p'+str(positionCode)+'/h_'+str(cityCode)+'/?page='+str(page)+'&ka=page-'+str(page)
                            print('现在抓取的是'+str(cityName)+','+str(industryName)+','+str(positionName)+'下第'+str(page)+'页')
                            time.sleep(2)
                            yield Request(url)

    def parse(self, response):
        # print(response.xpath('.//div[@id="main"]'),"32323")
        main = response.xpath('./div[@id="main"]')
        print(main,"rere")
        for li in main.xpath('.//ul/li'):
            print(li,"0909898")
            positionName = li.xpath('.//div[1]/div[1]/h3[1]/a/div[1]/text()').extract()
            print(positionName,"erwer")
            # companyIdInLagou = li.xpath('.//div/div[1]/h3/a[contains(@href, "data-jobid")]/@data-jobid').extract()[0]
            # print(companyIdInLagou)
        time.sleep(2)
        return 0
        pass



