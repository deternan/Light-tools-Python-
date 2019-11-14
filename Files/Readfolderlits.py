# coding=utf8

'''
version: September 19, 2019 03:08 PM
Last revision: November 14, 2019 02:22 PM
  
Author : Chao-Hsuan Ke

''' 

import os
from os import listdir
from os.path import isfile, isdir, join

filePath = "";        # folder name    

files = listdir(filePath)

print(os.path.exists(filePath))

if (os.path.exists(filePath)):
    for fileName in files:
        fullpath = join(filePath, fileName)
  
        if isfile(fullpath):
            print("file：", fileName)
        elif isdir(fullpath):
            print("folder：", fileName)

