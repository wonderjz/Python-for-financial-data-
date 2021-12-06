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
from bs4 import BeautifulSoup
#https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html
import csv
import datetime

#url = 'https://www.bilibili.com/ranking'
url = 'https://www.bilibili.com/v/popular/rank/all?spm_id_from=333.851.b_7072696d61727950616765546162.3'
#发起网络请求
response = requests.get(url)
html_text = response.text
# 解析这个str
soup = BeautifulSoup(html_text, 'html.parser')# 标准缩进的soup 

#用来保存视频信息的对象
class Video:
	def __init__(self, rank, title, score, visit, up, up_id, url):
		self.rank = rank
		self.title = title
		self.score = score
		self.visit = visit
		self.up = up
		self.up_id = up_id
		self.url = url
	def to_csv(self):
		return [self.rank, self.title, self.score, self.visit, self.up, self.up_id, self.url]

	@staticmethod
	def csv_title():
		return ['排名','标题','分数','播放量','Up主','Up Id', 'URL']

#提取列表
items = soup.findAll('li',{'class':'rank-item'})
vidoes = [] #保存提取出来的Video列表

for itm in items:
    title = itm.find('a',{'class':'title'}).text #视频标题
    score = itm.find('div',{'class':'pts'}).find('div').text #综合得分
    rank = itm.find('div',{'class':'num'}).text #排名
    visit = itm.find('span',{'class':'data-box'}).text #播放量
    up = itm.find_all('a')[2].text #播放量
    space = itm.find_all('a')[2].get('href')
    up_id = space[len('//space.bilibili.com/'):] #播放量
    url = itm.find('a', {'class':'title'}).get('href')
    v = Video(rank, title, score, visit, up, up_id, url)
    vidoes.append(v)

now_str = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
file_name = f'top100_{now_str}.csv'
with open(file_name, 'w', newline='',encoding='gb18030') as f:
	pen = csv.writer(f)
	pen.writerow(Video.csv_title())
	for v in vidoes:
		pen.writerow(v.to_csv())


url2 = 'https://www.bilibili.com/video/av85054372'
with open('temp.html', 'w', newline='',encoding='gb18030') as f:
	f.write(requests.get(url2).text)
#f = open("out.html","w",encoding='utf-8') 


