# -*- coding: utf-8 -*-
from scrapy import Request
from scrapy.selector import Selector
from scrapy.spiders import Spider

from woaidu.items import WoaiduItem
from woaidu.utils.select_result import list_first_item, clean_url


class WoaiduSpider(Spider):
    name = "woaidu"
    start_urls = [
        'http://www.woaidu.org/sitemap_1.html',
    ]

    def parse(self,response):
        response_selector = Selector(response)
        next_link = list_first_item(response_selector.xpath(u'//div[@class="k2"]/div/a[text()="下一页"]/@href').extract())
        if next_link:
            next_link = clean_url(response.url,next_link,response.encoding)
            yield Request(url=next_link, callback=self.parse)

        for detail_link in response_selector.xpath(u'//div[contains(@class,"sousuolist")]/a/@href').extract():
            if detail_link:
                detail_link = clean_url(response.url,detail_link,response.encoding)
                yield Request(url=detail_link, callback=self.parse_detail)

    def parse_detail(self, response):
        woaidu_item = WoaiduItem()

        response_selector = Selector(response)
        woaidu_item['book_name'] = list_first_item(response_selector.xpath('//div[@class="zizida"][1]/text()').extract())
        woaidu_item['author'] = [list_first_item(response_selector.xpath('//div[@class="xiaoxiao"][1]/text()').extract())[5:].strip(), ]
        woaidu_item['book_description'] = list_first_item(response_selector.xpath('//div[@class="lili"][1]/text()').extract()).strip()

        yield woaidu_item
