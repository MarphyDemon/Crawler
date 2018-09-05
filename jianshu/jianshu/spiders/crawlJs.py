# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from jianshu.items import JianshuUserItem

class CrawljsSpider(scrapy.Spider):
    name = 'CrawlJs'
    allowed_domains = ['www.jianshu.com']
    # start_urls = ['https://www.jianshu.com/']
    start_urls = ['https://www.jianshu.com/u/31defe23d40b']

    pattern = '.*jianshu.com/u/*.'
    pagelink = LinkExtractor(allow=pattern)

    # 可以写多个rule规则
    rules = [
        # 只要符合匹配规则，在rule中都会发送请求，同是调用回调函数处理响应
        # rule就是批量处理请求
        Rule(pagelink, callback='parse_item', follow=True),
    ]

    # 不能写parse方法，因为源码中已经有了，会覆盖导致程序不能跑
    def parse_item(self, response):
        for each in response.xpath("//div[@class='main-top']"):
            item = JianshuUserItem()
            # 用户名称
            item['name'] = each.xpath("./div[@class='title']/a/text()").extract()[0]
            # 关注数
            item['followNumber'] = each.xpath("./div[@class='info']/ul/li[1]//a/p/text()").extract()[0]
            # 粉丝数
            item['fansNumber'] = each.xpath("./div[@class='info']/ul/li[2]//a/p/text()").extract()[0]
            # 文章数
            item['articleNumber'] = each.xpath("./div[@class='info']/ul/li[3]//a/p/text()").extract()[0]
            # 字数
            item['wordCount'] = each.xpath("./div[@class='info']/ul/li[4]//p/text()").extract()[0]
            # 收获喜欢数
            item['likeNumber'] = each.xpath("./div[@class='info']/ul/li[5]//p/text()").extract()[0]

            # 把数据交给管道文件
            yield item