## Define here the models for your scraped items
##
## See documentation in:
## https://docs.scrapy.org/en/latest/topics/items.html
#
#import scrapy
#
#
#class BilibiliItem(scrapy.Item):
#    # define the fields for your item here like:
#    # name = scrapy.Field()
#    pass


# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BilibiliItem(scrapy.Item):
    mid = scrapy.Field()
    name = scrapy.Field()
    sex = scrapy.Field()
    face = scrapy.Field()
    sign = scrapy.Field()
    follower = scrapy.Field()
    following = scrapy.Field()
    view = scrapy.Field()
    likes = scrapy.Field()

