# coding=utf8

'''
version: September 23, 2019 01:27 PM
Last revision: September 23, 2019 01:51 PM
  
Author : Chao-Hsuan Ke

''' 

import os
from os import listdir
from os.path import isfile, isdir, join

# file folder
filePath = "";        # folder name    

files = listdir(filePath)

count = 0;

for fileName in files:
  fullpath = join(filePath, fileName)  
  if isfile(fullpath):
    print("old name：", fileName)
    os.rename(join(filePath, fileName), join(filePath, str(count))+".json")
    count +=1

   

