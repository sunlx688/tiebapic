# -*- coding:utf-8 -*-
__author__ = 'SUN'
'''创建和修改目录'''

import os


class dir:
    # 创建目录
    def make_dir(self, dir_name):
        IS_EXISTS = os.path.exists(dir_name)
        if not IS_EXISTS:
            print('创建名为', dir_name, '的目录')
            os.mkdir(dir_name)
        else:
            print('名为', dir_name, '的目录已存在！')

    # 修改目录路径
    def ch_dir(self, path):
        print('切换目录到', path)
        os.chdir(path)
