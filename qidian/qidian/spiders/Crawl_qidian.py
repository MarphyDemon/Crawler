# -*- coding: utf-8 -*-
# 
#   author：lidongdong
#   create：2018-09-10 
# 
import scrapy
from scrapy.spiders.crawl import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import time


class CrawlQidianSpider(CrawlSpider):
    name = 'Crawl-qidian'
    allowed_domains = ['www.qidian.com', 'book.qidian.com']
    # start_urls = ['http://www.qidian.com/']
    start_urls = ['https://www.qidian.com/finish?action=hidden&orderId=&style=1&pageSize=20&siteid=1&pubflag=0&hiddenField=2&page=1']
    # 定义link_extractor
    # 入口地址和详细页面链接
    main_page = LinkExtractor(allow='action=hidden&orderId=&style=1&pageSize=20&siteid=1&pubflag=0&hiddenField=2&page=\d', restrict_xpaths='//*[@class="lbf-pagination-next"]')
    page_info = LinkExtractor(allow='//book.qidian.com/info/\d')
    rules = (
        Rule(main_page, follow=False),
        Rule(page_info, callback='parse_item', follow=True)
    )

    def parse_item(self, response):
        try:
            book_name = response.xpath(".//*[@class='book-info ']/h1/em/text()").extract()[0]
        except:
            book_name = 'noknow'
        try:
            book_author = response.xpath(".//*[@class='book-info ']/h1/span/a/text()").extract()[0]
        except:
            book_author = 'noknow'
        try:
            book_span_tags = response.xpath(".//*[@class='book-info ']/p[@class='tag']/span/text()").extract()
        except:
            book_span_tags = 'noknow'
        try:
            book_a_tags = response.xpath(".//*[@class='book-info ']/p[@class='tag']/a/text()").extract()
        except:
            book_a_tags = 'unknow'
        try:
            book_intro = response.xpath(".//*[@class='book-info ']/p[@class='intro']/text()").extract()[0]
        except:
            book_intro = 'unknow'
        try:
            book_score_str = response.xpath(".//*[@id='j_bookScore']")
            book_score = book_score_str.xpath(".//span/*[@id='score1']/text()").extract()[0]+book_score_str.xpath(".//span/em/text()").extract()[0]+book_score_str.xpath(".//*[@id='score2']/text()").extract()[0]
        except:
            book_score = 'unknow'
        # print(response.body)
        print(book_name,book_author,book_span_tags,book_a_tags,book_intro)
        pass
