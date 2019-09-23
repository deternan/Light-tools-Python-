# coding=utf8

'''
version: September 23, 2019 11:17 AM
Last revision: September 23, 2019 11:17 AM
  
Author : Chao-Hsuan Ke

''' 

import os

filename = '12345.json'

print(os.path.splitext(filename)[0])
print(os.path.splitext(filename)[1])