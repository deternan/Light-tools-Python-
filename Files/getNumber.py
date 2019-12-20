# coding=utf8
'''
 version: December 20, 2019 01:30 PM
 Last revision: December 20, 2019 02:14 PM

 Author : Chao-Hsuan Ke
'''

from os import listdir

# files folder
sourcepath = '';  # folder name

files = listdir(sourcepath)

print(max(files))
print(min(files))

# max number in Files
maxNameTmp = max(files)
maxName = maxNameTmp.split('.')
print(maxName[0])

# min number in Files
minNameTmp = min(files)
minName = minNameTmp.split('.')
print(minName[0])