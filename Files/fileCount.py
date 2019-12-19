# coding=utf8

'''
version: December 19, 2019 06:30 PM
Last revision: December 19, 2019 06:40 PM

Author : Chao-Hsuan Ke

'''

import os
import sys

rootdir = ''

#print(len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))]))

fileList = []
fileSize = 0
folderCount = 0

for root, subFolders, files in os.walk(rootdir):
    folderCount += len(subFolders)
    for file in files:
        f = os.path.join(root,file)
        #fileSize = fileSize + os.path.getsize(f)
        fileList.append(f)

#print("Total Size is {0} bytes".format(fileSize))
print('Total Files ', len(fileList))
print('Total Folders ', folderCount)
