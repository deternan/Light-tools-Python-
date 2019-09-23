# coding=utf8

'''
version: September 19, 2019 03:08 PM
Last revision: September 19, 2019 03:08 PM
  
Author : Chao-Hsuan Ke

''' 

from os import listdir
from os.path import isfile, isdir, join

filePath = "";        # folder name    

files = listdir(filePath)

for fileName in files:
  fullpath = join(filePath, fileName)
  
  if isfile(fullpath):
    print("file：", fileName)
  elif isdir(fullpath):
    print("folder：", fileName)
   


