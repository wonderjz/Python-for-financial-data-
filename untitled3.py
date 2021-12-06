# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 22:23:03 2021

@author: ljz
"""

import requests  # 第三方模块, 需要 pip install requests
import re  # 内置模块

# 快速排版 代码 ctrl + ALT + L 首先你要QQ/网页云 这些快捷键改一下


# 如果只是想单独爬取一个视频 定义变量 要见名知意
bv_id = input('请输入你想要爬取的视频ID: ')    
url = f'https://www.ibilibili.com/video/{bv_id}'

# 请求头  让python伪装成浏览器 对其发送请求

headers = {
    'cookie': '__gads=ID=c43fc236264ad824-22fd6bb9ccc600a9:T=1616496169:RT=1616496169:S=ALNI_Mb67euYSi6VKwgSHX8yC_3mDmKgsQ; fsv__Session=lc8qa9ks0713d62lk7ljq0o305',
    'pragma': 'no-cache',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',

}



response = requests.get(url=url, headers=headers, verify=False)
# repsonse.text 获取网页文本数据 response.json() 获取json数据  response.content 获取二进制数据
# print(response.text)
# 解析数据 获取data参数  解析方法: re  css xpath
aid = re.findall('"aid":"(\d+)"', response.text)[0]
# 找到所有(包含"aid":"(多位数字)" 从 response.text 找 )
#  从 response.text 找到所有 包含"aid":"(多位数字)" 数据
b_cid = re.findall('"bcid":"(\d+)"', response.text)[0]
sign = re.findall('"absign":"(.*?)"', response.text)[0]
title = re.findall('<h4>(.*?)</h4>', response.text)[0]

index_url = 'https://bilibili.applinzi.com/index.php'
data = {
    'aid': aid,
    'bcid': b_cid,
    'absign': sign,
}
headers_1 = {
    'Host': 'bilibili.applinzi.com',
    'Origin': 'https://www.ibilibili.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
}
# print(aid, b_cid, sign)
response_1 = requests.post(url=index_url, data=data, headers=headers_1)

# 字典取值: 根据关键字取值   通俗的讲 就是根据冒号左边的内容 提取 冒号右边内容
video_url = response_1.json()['url']
print(video_url)
headers_2 = {
    'referer': video_url,
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
}
video_content = requests.get(url=video_url, headers=headers_2).content

with open(title + '.mp4', mode='wb') as f:
    f.write(video_content)