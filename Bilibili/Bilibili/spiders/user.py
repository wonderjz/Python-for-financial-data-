# -*- coding: utf-8 -*-

#import scrapy
#
#class DmozSpider(scrapy.Spider):
#    name = "geekdocs"
#    allowed_domains = ["geek-docs.com"]
#    start_urls = [
#        "https://geek-docs.com/vulkan/vulkan-tutorial/vulkan-understand-instance.html",
#    ]
#
#    def parse(self, response):
#        filename = response.url.split("/")[-2]
#        with open(filename, 'wb') as f:
#            f.write(response.body)


# -*- coding: utf-8 -*-
import scrapy
import json
from scrapy.http import Request
from Bilibili.items import BilibiliItem

Uid = 5970160
class UserSpider(scrapy.Spider):
    name = 'user' # 每个爬虫唯一的标识
    allowed_domains = ['bilibili.com']
    start_urls = ['https://api.bilibili.com/x/space/acc/info?mid=5970160']


    def parse(self, response):
        data = json.loads(response.body)['data']
        mid = data['mid']
#        name = data['name']
        name = data['name']
        sex = data['sex']
        face = data['face']
        sign = data['sign']
        # 粉丝数和关注数
        url1 = 'https://api.bilibili.com/x/relation/stat?vmid=' + str(mid)
#        yield Request(url=url1, callback=self.parse_page1,
#                      meta={'mid': mid, 'name': name, 'sex': sex, 'face': face, 'sign': sign})

#    def parse_page1(self, response):
#        data = json.loads(response.body)['data']
#        mid = data['mid']
#        following = data['following']
#        follower = data['follower']
#        # 获赞数和播放数
#        url2 = 'https://api.bilibili.com/x/space/upstat?mid=' + str(mid) #这个get不到
#        yield Request(url=url2, callback=self.parse_page2,
#                      meta={'mid': mid, 'name': response.meta['name'], 'sex': response.meta['sex'],
#                            'face': response.meta['face'], 'sign': response.meta['sign'], 'follower': follower,
#                            'following': following})
#
##    def parse_page2(self, response):
#        data = json.loads(response.body)['data']
#        mid = response.meta['mid']
#        name = response.meta['name']
#        sex = response.meta['sex']
#        face = response.meta['face']
#        sign = response.meta['sign']
#        follower = response.meta['follower']
#        following = response.meta['following']
#        view = data['archive']['view']
#        likes = data['likes']
#        item = BilibiliItem(
#            mid=mid,
#            name=name,
#            sex=sex,
#            face=face,
#            sign=sign,
#            follower=follower,
#            following=following,
#            view=view,
#            likes=likes
#        )
#        yield item
#        for i in range(1, 6):
#            following_url = 'https://api.bilibili.com/x/relation/followings?vmid=' + str(mid) + '&pn=' + str(i)
#            yield Request(url=following_url, callback=self.parse_following)
#        for i in range(1, 6):
#            follower_url = 'https://api.bilibili.com/x/relation/followers?vmid=' + str(mid) + '&pn=' + str(i)
#            yield Request(url=follower_url, callback=self.parse_follower)
#
#    def parse_following(self, response):
#        data = json.loads(response.body)['data']
#        user_list = data['list']
#        if user_list:
#            for item in user_list:
#                mid = item['mid']
#                url = 'https://api.bilibili.com/x/space/acc/info?mid=' + str(mid)
#                yield Request(url=url, callback=self.parse)
#
#    def parse_follower(self, response):
#        data = json.loads(response.body)['data']
#        user_list = data['list']
#        if user_list:
#            for item in user_list:
#                mid = item['mid']
#                url = 'https://api.bilibili.com/x/space/acc/info?mid=' + str(mid)
#                yield Request(url=url, callback=self.parse)


