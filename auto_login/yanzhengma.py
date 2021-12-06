# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 17:15:22 2021

@author: ljz
"""



################################################################################
#login_bilibili
from selenium import webdriver
import time
from PIL import Image
from selenium.webdriver import ActionChains #导入动作链模块
from kuaishibie import base64_api

KUAI_USERNAME = 'wonderjz'
KUAI_PASSWORD = 'LJZksb'  # input your password 

USERNAME = '17302200589'
PASSWORD = 'password' # input your password bilibili

#创建浏览器对象
driver_path = r'E:\chrome_driver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)
#打开请求网页页面
driver.get('https://passport.bilibili.com/login')
driver.implicitly_wait(5) #隐式等待浏览器渲染完成，sleep是强制等待
#driver.execute_script("document.body.style.zoom='0.67'") #浏览器内容缩放67%
driver.maximize_window()#最大化浏览器

'''
用selenium自动化工具操作浏览器，操作的顺序和平常用浏览器操作的顺序是一样的
'''

'''
找到用户名和密码框输入密码
'''
user_input = driver.find_element_by_xpath('//*[@id="login-username"]') #使用xpath定位用户名标签元素
user_input.send_keys(USERNAME)
time.sleep(1)

user_input = driver.find_element_by_xpath('//*[@id="login-passwd"]') #用户密码标签
user_input.send_keys(PASSWORD)
time.sleep(1)

#点击登录
Login_input = driver.find_element_by_css_selector('#geetest-wrap > div > div.btn-box > a.btn.btn-login')
Login_input.click()
time.sleep(5)

#对图片验证码进行提取
#img_label = driver.find_element_by_css_selector('body > div.geetest_panel.geetest_wind > div.geetest_panel_box.geetest_no_logo.geetest_panelshowclick > div.geetest_panel_next > div > div > div.geetest_table_box > div.geetest_window > div > div.geetest_item_wrap > img' ) #提取图片标签
img_label = driver.find_element_by_css_selector('body > div.geetest_panel.geetest_wind > div.geetest_panel_box.geetest_no_logo.geetest_panelshowclick > div.geetest_panel_next > div > div > div.geetest_table_box' ) #提取图片标签

#保存图片
driver.save_screenshot('big.png') #截取当前整个页面
time.sleep(5)
#location可以获取这个元素左上角坐标
print(img_label.location)
#size可以获取这个元素的宽(width)和高(height)
print(img_label.size)

#计算验证码的左右上下横切面
left = img_label.location['x']+300
top = img_label.location['y']+150
right = img_label.location['x'] + img_label.size['width']+450
down = img_label.location['y'] + img_label.size['height']+250

#left = img_label.location['x']
#top = img_label.location['y']
#right = img_label.location['x'] + img_label.size['width']
#down = img_label.location['y'] + img_label.size['height']

im = Image.open('big.png')
im = im.crop((left,top,right,down))
width = 259
height = 262
im = im.resize((width, height))
im.save('LJZlogin.png')

#对接打码平台
#from interface import base64_api #显示报错也无妨，可以运行的不要被唬住



img_path = 'LJZlogin.png'
result = base64_api(uname= KUAI_USERNAME, pwd= KUAI_PASSWORD, img= img_path,typeid=27)
print(result)
print('验证码识别结果：', result)
result_list = result.split('|')
for result in result_list:
    x = result.split(',')[0]
    y = result.split(',')[1]
    ActionChains(driver).move_to_element_with_offset(img_label, int(x), int(y)).click().perform()  # perform()执行整个动作链

#点击确认按钮
driver.find_element_by_css_selector('body > div.geetest_panel.geetest_wind > div.geetest_panel_box.geetest_no_logo.geetest_panelshowclick > div.geetest_panel_next > div > div > div.geetest_panel > a > div').click()
input()  # 用户输入 阻塞浏览器关闭
# 关闭浏览器

driver.quit()





