# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 17:34:33 2021

@author: ljz
"""

#快识别网址 http://www.kuaishibie.cn/
#interface
import base64
import json
import requests

#def base64_api(uname,pwd,img):
#    '''
#    验证码识别接口
#    :param uname: 快识别用户名
#    :param pwd: 快识别密码
#    :param img: 图片路径
#    :return: 返回识别结果
#    '''
#    
#    with open(img, 'rb') as f:
#        base64_data = base64.b64encode(f.read())
#        b64 = base64_data.decode()
#    data = {"username": uname, "password": pwd, "image": b64,"typeid":21}
#    data = {"username": 'wonderjz', "password": 'LJZshb', "image": b64,"typeid":21}
#    #result = json.loads(requests.post("http://api.ttshitu.com/base64", json=data).text)
#    result = json.loads(requests.post("http://api.ttshitu.com/imageXYPlus", json=data).text)
#    if result['success']:
#        return result["data"]["result"]
#    else:
#        return result["message"]

def base64_api(uname, pwd, img, typeid):
    with open(img, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        b64 = base64_data.decode()
    data = {"username": 'wonderjz', "password": 'LJZksb', "typeid":27, "image": b64} # typeid 27: 1-4 words click
    result = json.loads(requests.post("http://api.ttshitu.com/predict", json=data).text)
    if result['success']:
        return result["data"]["result"]
    else:
        return result["message"]
    return ""
