# -*- coding: utf-8 -*-
import scrapy


class BossJobsSpider(scrapy.Spider):
    name = 'boss_jobs'
    allowed_domains = ['zhipin.com']
    
    start_urls = 'https://www.zhipin.com/c'+city+'/h_'+city+'/?page='+page+'&ka=page-'+page

    def parse(self, response):

        pass
