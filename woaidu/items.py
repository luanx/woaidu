# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class WoaiduItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    book_name = Field()
    alias_name = Field()
    author = Field()
    book_description = Field()
    pass
