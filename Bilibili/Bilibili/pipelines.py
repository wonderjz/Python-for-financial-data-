## Define your item pipelines here
##
## Don't forget to add your pipeline to the ITEM_PIPELINES setting
## See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#
#
## useful for handling different item types with a single interface
#from itemadapter import ItemAdapter
#
#
#class BilibiliPipeline:
#    def process_item(self, item, spider):
#        return item


# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from twisted.enterprise import adbapi
from pymysql import cursors

#db = pymysql.connect(host='localhost',user='root', password='LJZ991103mysql', port=3306)
#cursor = db.cursor()  
#cursor.execute('SELECT VERSION()')  
#data = cursor.fetchone()  
#print('Database version:', data)  
#cursor.execute("CREATE DATABASE bzhan DEFAULT CHARACTER SET utf8") #创建一个数据库叫bzhan 
#db.close()
class BilibiliPipeline(object):
    def __init__(self):
        dbparams = {
#            'host': '61.238.222.45',
#            'port': 3306,
            'host': 'localhost',
            'port': 3306,          
            'user': 'root',
            'password': 'LJZ991103mysql', #root
            'database': 'bzhan',
            'charset': 'utf8mb4'
        }
        self.conn = pymysql.connect(**dbparams)
        self.cursor = self.conn.cursor()
        self._sql = None

    def process_item(self, item, spider):
        sql = self.sql()
        data = dict(item)
        self.cursor.execute(
            sql,
            (data['mid'],
             data['name'],
             data['sex'],
             data['face'],
             data['sign'],
             data['follower'],
             data['following'],
             data['view'],
             data['likes']))
        self.conn.commit()
        print(data)
        return item

    def sql(self):
        if not self._sql:
            self._sql = "insert into user(id,mid,name,sex,face,sign,follower,following,view,likes) values(null,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            return self._sql
        return self._sql

