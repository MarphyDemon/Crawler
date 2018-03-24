# -*- coding: utf-8 -*-
# Author: waltsmith
# Date: 2018-01-03
# Function:
#   1. 抓取腾讯招聘网站hr.tencent.com的所有招聘信息
#   2. 提供两种保存数据形式：
#           1. 采用utf-8编码，写入csv文件；
#           2. 采用utf-8编码，写入MySQL数据库；要注意设置数据库编码为utf-8

# 导入模块
from scrapy.spiders.crawl import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import pymysql
import time


class TencentJobsSpider(CrawlSpider):
    name = 'tencent_jobs'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['http://hr.tencent.com/position.php?&start=0#a']
    # 定义link_extractor
    # 入口地址和详细页面链接
    main_page = LinkExtractor(allow='&start=\d+#a', restrict_xpaths='//*[@id="next"]')
    page_info = LinkExtractor(allow='id=\d+&keywords=')
    rules = (
        Rule(main_page, follow=True),
        Rule(page_info, callback='parse_item', follow=True)
    )


    def parse_item(self, response):
        # 职位名称、工作地点、职位类别、招聘人数
        try:
            job_name = response.xpath('//*[@id="sharetitle"]/text()').extract()[0]
        except:
            job_name = 'UNKNOWN'
        # print(response.xpath('//*[@id="sharetitle"]/text()').extract()[0],"lidd")
        # print(job_name,"lidongdong")
        try:
            job_location = response.xpath('//tr[2]/td[1]/text()').extract()[0]
        except:
            job_location = 'UNKNOWN'
        try:
            job_type = response.xpath('//tr[2]/td[2]/text()').extract()[0]
        except:
            job_type = 'UNKNOWN'
        try:
            job_needed_people_num = response.xpath('//tr[2]/td[3]/text()').extract()[0]
        except:
            job_needed_people_num = 'UNKNOWN'
        try:
            job_duty = response.xpath('string(//tr[3]/td/ul)').extract()[0]
        except:
            job_duty = 'UNKNOWN'
        try:
            job_requirement = response.xpath('string(//tr[4]/td/ul)').extract()[0]
        except:
            job_requirement = ''

        ## 写入文件
        # params = [job_name, job_type, job_location, job_needed_people_num, job_duty, job_requirement]
        # with open('tencent_jobs.txt', 'a+') as f:
        #     f.write(str(params[0]) + ', ' + str(params[1]) + ', ' + str(params[2]) + ', ' + str(params[3]) + ', ' + str(params[4]) + ', ' + str(params[5]) + '\n')


        # ## 写入数据库
        param = [job_name, job_location, job_type,
                      job_needed_people_num, job_duty, job_requirement]
        # 连接数据库
        with pymysql.connect(database='tencent', host='localhost', user='root', password='marphy0817', charset='utf8') as cursor:
            # 向表中插入数据的sql语句
            sql_insert = '''
                    insert into jobs (job_name, location, type, needed_people_num, duty, requirement) VALUES (
                    %s, %s, %s, %s, %s, %s
                    )
                '''
            try:
                cursor.execute(sql_insert, param)
            except:
                print("============数据库插入失败！=============")
                time.sleep(5)
                pass 