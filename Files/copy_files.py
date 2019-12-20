# coding=utf8
'''
 version: December 20, 2019 10:52 AM
 Last revision: December 20, 2019 11:00 AM

 Author : Chao-Hsuan Ke

'''

import os
from os import listdir
import shutil

path = ''      # original path
obj_path = ''  # target path


def copyFiles(path, obj_path):
    files = listdir(path)
    count = 0
    for fileName in files:
        orifullpath = path + fileName
        tarfullpath = obj_path + fileName
        print(files[count])
        count+=1
        shutil.copyfile(orifullpath, tarfullpath)
    print('finished')


copyFiles(path, obj_path)