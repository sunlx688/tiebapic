# -*- coding:utf-8 -*-
__author__ = 'SUN'
'''管理程序运行'''

from Dir import dir
from SaveAllPhotos import save_all_photos
from GetOnePagePhotoUrls import get_one_page_photo_urls
from GetAllTieZiUrls import get_all_tie_zi_urls


class run:
    def __init__(self, url, path):
        self.url = url
        self.path = path

    # 程序运行函数
    def start(self):
        tie_zi_num = 0
        tie_zi_urls = get_all_tie_zi_urls(self.url).get_tie_zi_urls()
        tie_zi_titles = get_all_tie_zi_urls(self.url).get_tie_zi_titles()
        while tie_zi_num < len(tie_zi_urls):
            photos_num = len(get_one_page_photo_urls(tie_zi_urls[tie_zi_num]).get_photo_urls())
            dir_name = tie_zi_titles[tie_zi_num]
            if photos_num == 0:
                tie_zi_num += 1
                continue
            else:
                dir().ch_dir(path)
                dir().make_dir(dir_name)
                new_path = self.path + dir_name
                dir().ch_dir(new_path)
                save_all_photos(self.url).save_all_photos()
                print('本帖子的名字为', dir_name, photos_num, new_path)
                tie_zi_num += 1


url = 'http://tieba.baidu.com/f?ie=utf-8&kw=%E5%B7%B2%E5%A9%9A&fr=search'
path = 'G:\Code\img\\tieba\已婚\\'

sun = run(url, path)
sun.start()
