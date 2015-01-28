# -*- coding: utf-8 -*-

# Scrapy settings for shortStory project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'shortStory'

SPIDER_MODULES = ['shortStory.spiders']
NEWSPIDER_MODULE = 'shortStory.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'shortStory (+http://www.yourdomain.com)'

# DOWNLOADER_MIDDLEWARES = {
#     'shortStory.util.middleware.CustomHttpProxyMiddleware': 400,
#     'shortStory.util.middleware.CustomUserAgentMiddleware': 401,
# }

ITEM_PIPELINES = {
    'shortStory.pipelines.JsonWithEncodingPipeline': 300,
    #'shortStory.pipelines.RedisPipeline': 301,
}

LOG_LEVEL = 'INFO'

DOWNLOAD_DELAY = 1