# -*- coding: utf-8 -*-
from scrapy.spiders import BaseSpider
from woaidu.items import WoaiduItem


class WoaiduSpider(BaseSpider):
    name = "woaidu"
    start_urls = [
        'http://www.woaidu.org/sitemap_1.html'
    ]

    def parse(self, response):

        woaidu_item = WoaiduItem()

        yield woaidu_item