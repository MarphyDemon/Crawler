# -*- coding: utf-8 -*-
import scrapy


class CrawlQidianSpider(scrapy.Spider):
    name = 'Crawl-qidian'
    allowed_domains = ['www.qidian.com']
    # start_urls = ['http://www.qidian.com/']
    start_urls = ['https://www.qidian.com/finish?action=hidden&orderId=&style=1&pageSize=20&siteid=1&pubflag=0&hiddenField=2&page=3']
    

    def parse(self, response):
        # print(response.xpath(".//ul/li"),"dsads")
        # .extract()[0].xpath(".//div[@class='test]/h4/a").text()
        aa = response.xpath(".//ul/li")
        bb = aa.xpath(".//div[@class='book-mid-info']/h4/a/text()").extract()[0]
        print(bb,'sss')
        pass
