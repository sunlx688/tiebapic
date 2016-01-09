# -*- coding:utf-8 -*-
__author__ = 'SUN'
'''获得一个帖子中所有的页面'''
from GetSoup import get_soup


class get_one_tie_pages:
    def __init__(self, url):
        self.gs = get_soup()
        self.url = url
        self.base_url = self.url.split('=')[0] + '='

    # 获取最大的页码
    def get_max_page_num(self):
        soup = self.gs.get_soup(self.url)
        page_num_str = soup.find_all('span', attrs={"class": "red"})[1]
        max_page_num = int(page_num_str.text)
        return max_page_num

    # 获取所有页面的链接
    def get_pages(self):
        PAGES=[]
        for page_num in range(self.get_max_page_num()):
            page = self.base_url + str(page_num+1)
            PAGES.append(page)
            page_num += 1
        return PAGES