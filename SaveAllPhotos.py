# -*- coding:utf-8 -*-
__author__ = 'SUN'
'''保存所有帖子上的图片'''
from GetAllTieZiUrls import get_all_tie_zi_urls
from SaveOneTieZiPhotos import save_one_tie_zi_photos
from time import sleep
import random


class save_all_photos:
    def __init__(self, url):
        self.url = url
        self.RANDOM_NUM = random.uniform(2, 3)

    # 获取所有的图片
    def save_all_photos(self):
        # 获取所有帖子的链接
        tie_zi_urls = get_all_tie_zi_urls(self.url).get_tie_zi_urls()
        print('共有', len(tie_zi_urls), '个帖子')
        for tie_zi_url in tie_zi_urls:
            tie_zi_url = tie_zi_url + '?pn=1'
            save_one_tie_zi_photos().save_all_pages_photos(tie_zi_url)
            sleep(self.RANDOM_NUM)