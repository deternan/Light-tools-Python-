# coding=utf8

'''
version: September 19, 2019 03:08 PM
Last revision: September 19, 2019 03:08 PM
  
Author : Chao-Hsuan Ke

''' 

from os import listdir
from os.path import isfile, isdir, join

# file filder
filePath = "D:\\Phelps\\GitHub\\Light-tools (Python)\\";     

files = listdir(filePath)

for fileName in files:
# 產生檔案的絕對路徑
  fullpath = join(filePath, fileName)
  # 判斷 fullpath 是檔案還是目錄
  if isfile(fullpath):
    print("file：", fileName)
  elif isdir(fullpath):
    print("folder：", fileName)
   
#print(fileName)

