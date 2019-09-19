# coding=utf8

'''
version: September 19, 2019 03:08 PM
Last revision: September 19, 2019 04:31 PM
  
Author : Chao-Hsuan Ke

''' 

import os.path

filepath = "D:\\Phelps\\GitHub\\Light-tools (Python)\\Files\\"

print(os.path.splitext(filepath)[0])    # filename
print(os.path.splitext(filepath)[1])    # file extension name

 
def fileName(file_dir):  
    for root, dirs, files in os.walk(file_dir): 
        print(root)          #當前目錄路徑 
        print(dirs)         #當前路徑下所有子目錄 
        print(files)        #當前路徑下所有非目錄子檔案
        for i in files:
            print(os.path.splitext(i)[0],   os.path.splitext(i)[1])
        
fileName(filepath)    