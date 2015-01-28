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


from nownews.items import *
from nownews.util.log import *

class DoubanBookSpider(CrawlSpider):
    name = "36kr"
    allowed_domains = ["36kr.com"]
    start_urls = [
        "http://www.36kr.com/"
    ]
    rules = [
        # Rule(sle(allow=("/p/\d+.html$")), callback='parse_2'),
        # Rule(sle(allow=("/tag/[^/]+/?$", )), follow=True),
        # Rule(sle(allow=("/tag/$", )), follow=True),
    ]

    def parse_2(self, response):
        items = []
        sel = Selector(response)
        sites = sel.css('.content-wrapper')
        for site in sites:
            item = NewsItem()
            item['title'] = site.css('.single-post__title::text').extract()
            item['link'] = response.url
            item['imgUrl'] = site.css('.single-post-header__headline img::attr(src)').extract()
            item['time'] = site.css('.timeago::attr(title)').extract()

            items.append(item)
            # print repr(item).decode("unicode-escape") + '\n'
            print item
        # info('parsed ' + str(response))
        return items

    def parse_1(self, response):
        # url cannot encode to Chinese easily.. XXX
        info('parsed ' + str(response))

    def _process_request(self, request):
        info('process ' + str(request))
        return request