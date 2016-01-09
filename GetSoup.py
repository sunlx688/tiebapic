# -*- coding:utf-8 -*-
__author__ = 'SUN'
'''获取一个页面的内容'''
import requests
from bs4 import BeautifulSoup


class get_soup:
    # 获得页面中的所有内容
    def get_soup(self, url):
        response = requests.get(url)
        response.encoding = 'utf-8'
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser', from_encoding=response.encoding)
            return soup
        else:
            print('您访问页面不存在！')