# -*- coding:utf-8 -*-
__author__ = 'SUN'
'''获取所有帖子的链接和帖子的标题'''
from GetSoup import get_soup


class get_all_tie_zi_urls:
    def __init__(self, url):
        self.gs = get_soup()
        self.url = url
        self.URLS = []
        self.TITLES=[]

    # 获取到包含帖子链接的内容
    def get_contents(self):
        soup = self.gs.get_soup(self.url)
        contents = soup.find_all('a', attrs={"class", "j_th_tit"})
        return contents

    # 获取到帖子的链接
    def get_tie_zi_urls(self):
        contents = self.get_contents()
        for content in contents:
            tie_zi_url = content['href']
            self.URLS.append('http://tieba.baidu.com' + tie_zi_url)
        return self.URLS

    # 获取到帖子的标题
    def get_tie_zi_titles(self):
        contents = self.get_contents()
        for content in contents:
            title=content['title']
            self.TITLES.append(title)
        return self.TITLES

# url = 'http://tieba.baidu.com/f?ie=utf-8&kw=%E5%B7%B2%E5%A9%9A&fr=search'
# gatzu = get_all_tie_zi_urls(url)
# print(gatzu.get_contents())
# print(gatzu.get_tie_zi_urls())
# print(gatzu.get_tie_zi_title())