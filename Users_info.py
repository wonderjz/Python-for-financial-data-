# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 11:21:52 2021

@author: ljz
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 20:24:45 2021

@author: ljz
"""
#https://python3webspider.cuiqingcai.com/5.2-guan-xi-xing-shu-ju-ku-cun-chu
#https://www.bilibili.com/robots.txt
#火烧云
#小小数据

import requests
#from bs4 import BeautifulSoup
#https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html
import csv
#import datetime
import json
import os
import time
from random import uniform
#Users_id = [261504973,517327498]
path = r'E:\codes for 7033\Pa'
path1 = os.path.join(path,'Users_id.txt')


file = open(path1,'r')
txt = file.readlines()
Users_id = []
for w in txt:
    w = w.replace('\n', '')
    Users_id.append(w)

#for i in Users_id:
#    if i is None:
#        Users_id.pop(i)
print(Users_id)

class BilibiliUser:
    def __init__(self, name, mid, gender, level, sign, birthday, following, follower):
        self.name = name
        self.mid = mid
        self.gender = gender
        self.level = level
        self.sign = sign
        self.birthday = birthday
        self.following = following
        self.birthday = birthday
        self.follower = follower
        
    def to_csv(self):
        return [self.name, self.mid, self.gender, self.level, self.sign, self.birthday, self.following, self.follower]
    #	@staticmethod
    def csv_title():
        return ['name','id','gender','level','sign', 'birthday','following','follower']
        
		 
#提取列表
#items = soup.findAll('li',{'class':'rank-item'})

Users_data = [] #保存提取出来的Video列表
i = 0
for Uid in Users_id:
    try:
        user_url = 'https://api.bilibili.com/x/space/acc/info?mid=' + str(Uid)
        requests.get(user_url) #用户信息请求的URL
        response = requests.get(user_url)
        html_text = response.text
        html_json = json.loads(html_text)
        time.sleep(uniform(1,1.3))
        
        fans_url = 'https://api.bilibili.com/x/relation/stat?vmid=' + str(Uid) #粉丝数和关注数请求的URL
        requests.get(fans_url)
        #fans_url = 'https://api.bilibili.com/x/space/upstat?mid=' + str(Uid) #获赞数和播放数请求的URL
        fans_response = requests.get(fans_url)
        fans_html_text = fans_response.text
        fans_html_json = json.loads(fans_html_text)
        time.sleep(uniform(1,1.3))
        
        name = html_json['data']['name']
        mid = html_json['data']['mid']
        gender = html_json['data']['sex']
        level = html_json['data']['level']
        sign = html_json['data']['sign']
        birthday = html_json['data']['birthday']    
        following = fans_html_json['data']['following']
        follower = fans_html_json['data']['follower']  
        
        v = BilibiliUser(name,mid,gender,level,sign, birthday,following,follower)
        Users_data.append(v)
        print("have finished " + str(i+1))
    except:
        print("error in " + str(i+1))
    i = i+1

#now_str = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
file_name = f'BilibiliUsers.csv'
with open(file_name, 'w', newline='',encoding='gb18030') as f:
	pen = csv.writer(f)
	pen.writerow(BilibiliUser.csv_title())
	for v in Users_data:
		pen.writerow(v.to_csv())




