# coding=utf8

'''
version: September 23, 2019 02:23 PM
Last revision: September 23, 2019 02:27 PM
  
Author : Chao-Hsuan Ke

''' 

import os
from os import listdir
from os.path import isfile, isdir, join

# file folder
filePath = "";        # folder name    

files = listdir(filePath)


for fileName in files:
  fullpath = join(filePath, fileName)  
  if isfile(fullpath):    
    os.remove(fullpath)
    print(fullpath)
