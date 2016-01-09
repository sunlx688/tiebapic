# -*- coding:utf-8 -*-
__author__ = 'SUN'
'''获取到一个页面上所有图片的链接'''
from GetSoup import get_soup


class get_one_page_photo_urls:
    def __init__(self, url):
        self.url = url
        self.URLS = []
        self.gs = get_soup()

    # 获取包含图片链接的内容
    def get_contents(self):
        soup = self.gs.get_soup(self.url)
        contents = soup.find_all('img', attrs={"class": "BDE_Image"})
        return contents

    # 获取一个页面上的所有的图片链接
    def get_photo_urls(self):
        contents = self.get_contents()
        for content in contents:
            url = content['src']
            self.URLS.append(url)
        return self.URLS


# tiezi_url = 'http://tieba.baidu.com/p/4226024634?pn=1'
# goppu = get_one_page_photo_urls(tiezi_url)
# print(goppu.get_photo_urls())