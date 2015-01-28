#-*- coding: UTF-8 -*-
__author__ = 'eric'

import re
import json


from scrapy.selector import Selector
try:
    from scrapy.spider import Spider
except:
    from scrapy.spider import BaseSpider as Spider
from scrapy.utils.response import get_base_url
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor as sle

from shortStory.items import *
from shortStory.util.log import *

class DoubanBookSpider(CrawlSpider):
    name = "ypgs"
    allowed_domains = ["07938.com"]
    start_urls = [
        "http://www.07938.com/zheligushi/"
    ]
    rules = [
        Rule(sle(allow=("/\d+.html$")), callback='parse_2'),
        # Rule(sle(allow=("/tag/[^/]+/?$", )), follow=True),
        # Rule(sle(allow=("/tag/$", )), follow=True),
    ]

    def parse_2(self, response):
        item = StoryItem()
        sel = Selector(response)
        item['title'] = sel.css("h1::text")
        content = sel.css(".content")
        # TODO 内容格式处理
        item['content'] = self.process_content(content)
        # info('parsed ' + str(response))
        return item

    def parse_1(self, response):
        # url cannot encode to Chinese easily.. XXX
        info('parsed ' + str(response))

    def _process_request(self, request):
        info('process ' + str(request))
        return request

    def process_content(self, content):
        # TODO process content

        return content