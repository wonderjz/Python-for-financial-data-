# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 10:13:59 2021

@author: ljz
"""
from selenium import webdriver
import time
from random import uniform

driver_path = r'E:\chrome_driver\chromedriver.exe'
browser = webdriver.Chrome(executable_path=driver_path)
save_path = r'E:\codes for 7033\Pa'
upername = "学神王牢实"


#bzhan = 'https://passport.bilibili.com/login'
#browser.get(bzhan)
# use .py inside file "auto_login" and your phone verification code to login in
# or let bilibili remember you when you use your own pc
# the total program is not fully automatic

search = 'https://search.bilibili.com/'
browser.get(search)


button  = browser.find_element_by_xpath('//*[@id="internationalHeader"]/div[1]/div/div[3]/div[1]/a/i')
browser.execute_script("arguments[0].click();", button)
#输入uper 名字
upername = "学神王牢实"
button1 = browser.find_element_by_xpath('//*[@id="search-keyword"]').send_keys(upername)
browser.maximize_window()
#搜索
button_search = browser.find_element_by_xpath('//*[@id="server-search-app"]/div/div/div[2]/a')
browser.execute_script("arguments[0].click();", button_search)
time.sleep(1)

#点进个人空间
title = browser.find_element_by_xpath('//*[@id="all-list"]/div[1]/div[2]/ul[1]/div/div[1]/div/div[1]/a[1]')
browser.execute_script("arguments[0].click();", title)
time.sleep(1)

#跳入新窗口
print(browser.current_window_handle)
handles = browser.window_handles
print(browser.window_handles)
browser.switch_to.window(handles[-2]) 

#for handle in handles:
#    if handle!= browser.current_window_handle:
#        browser.close()
#        browser.swith_to.window(handle)

#get into his posts
tougao = browser.find_element_by_xpath('//*[@id="navigator"]/div/div[1]/div[1]/a[3]')
browser.execute_script("arguments[0].click();", tougao)
time.sleep(uniform(1,1.5))

#browser.switch_to.window(handles[-1])
#browser.close()

# first
video1 = browser.find_element_by_xpath('//*[@id="submit-video-list"]/ul[2]/li[1]/a[1]/img')
browser.execute_script("arguments[0].click();", video1)

# scroll the window
#eles = browser.find_elements_by_css_selector('#arc_toolbar_report > div.ops > span.like > i')
#ele = eles[0]
#browser.execute_script("arguments[0].scrollIntoView();",ele)
handles = browser.window_handles
browser.switch_to.window(handles[-2])
browser.execute_script('window.scrollBy(0,400)')
# dianzan
dianzan = browser.find_element_by_xpath('//*[@id="arc_toolbar_report"]/div[1]/span[1]/i')
browser.execute_script("arguments[0].click();", dianzan)

handles = browser.window_handles

browser.switch_to.window(handles[-1]) 
browser.close()

handles = browser.window_handles
browser.switch_to.window(handles[-2]) 

from selenium.webdriver.common.action_chains import ActionChains


# give a thumbs up for the first 10 videos

#i = 2
for i in range(2,10):
    handles = browser.window_handles
    browser.switch_to.window(handles[-2]) 
    thevideo = browser.find_element_by_xpath('//*[@id="submit-video-list"]/ul[2]/li['+ str(i)+ ']/a[1]/img')

    browser.execute_script("arguments[0].scrollIntoView();", thevideo)
    
    browser.execute_script("arguments[0].click();", thevideo)
    time.sleep(1)
    handles = browser.window_handles
    browser.switch_to.window(handles[-1])
    browser.execute_script('window.scrollBy(0,400)')
    dianzan = browser.find_element_by_xpath('//*[@id="arc_toolbar_report"]/div[1]/span[1]/i')
    time.sleep(uniform(3,3.4))
    browser.execute_script("arguments[0].click();", dianzan)
    handles = browser.window_handles
    browser.switch_to.window(handles[-1]) 
    time.sleep(uniform(1,1.4))
    browser.close()
    
    

