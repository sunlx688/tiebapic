# -*- coding:utf-8 -*-
__author__ = 'SUN'
'''保存一个帖子上的图片'''
from GetOnePagePhotoUrls import get_one_page_photo_urls
from GetOneTiePages import get_one_tie_pages
import requests
import random
from time import sleep
import os


class save_one_tie_zi_photos:
    def __init__(self):
        # 生成随机数
        self.RANDOM_NUM = random.uniform(0.5, 2)

    # 保存一张图片
    def save_one_photo(self, photo_name, photo_url):
        data = requests.get(photo_url).content
        fp = open(photo_name, 'wb')
        fp.write(data)
        fp.close()

    # 保存一个页面的图片
    # def save_one_page_photos(self, url):
    #     X = 1
    #     photo_urls = get_one_page_photo_urls(url).get_photo_urls()
    #     print('本页共有图片', len(photo_urls), '张')
    #     for photo_url in photo_urls:
    #         if os.path.exists('%s.jpg' % X):
    #             pass
    #         else:
    #             print('开始保存第', X, '张')
    #             self.save_one_photo('%s.jpg' % X, photo_url)
    #             X += 1
    #             sleep(self.RANDOM_NUM)

    # 保存一个帖子所有页面的图片
    def save_all_pages_photos(self, url):
        PAGE_NUM = 1
        one_tie_pages = get_one_tie_pages(url).get_pages()
        while PAGE_NUM <= len(one_tie_pages):
            X = 1
            photo_urls = get_one_page_photo_urls(one_tie_pages[PAGE_NUM - 1]).get_photo_urls()
            print('本页共有图片', len(photo_urls), '张')
            print(one_tie_pages[PAGE_NUM - 1])
            print(len(one_tie_pages))
            print(PAGE_NUM)
            if os.path.exists(str(PAGE_NUM) + '页第%s张.jpg' % X):
                pass
            else:
                for photo_url in photo_urls:
                    print('开始保存第', X, '张')
                    self.save_one_photo(str(PAGE_NUM) + '页第%s张.jpg' % X, photo_url)
                    X += 1
                    sleep(self.RANDOM_NUM)
            PAGE_NUM += 1
            # print('本帖子的图片已保存完成！')


# url = 'http://tieba.baidu.com/p/3081354059?pn=1'
# url = 'http://tieba.baidu.com/p/4254370280?pn=1'
# photo_url = 'http://imgsrc.baidu.com/forum/w%3D580/sign=4443180e3d292df597c3ac1d8c305ce2/94fed9ef76094b367c02c6cca4cc7cd98c109dd7.jpg'
# sotzp = save_one_tie_zi_photos()
# sotzp.save_all_pages_photos(url)
