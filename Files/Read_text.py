# coding=utf8

'''
version: September 19, 2019 02:28 PM
Last revision: November 14, 2019 02:22 PM
  
Author : Chao-Hsuan Ke

''' 

filePath = "";        # file path
fileName = "";        # file name

f = open(filePath + fileName, 'r')
#print(f.read())                 # print all at once time
#print(len(f.readlines()))      # all line number

    
for line in f:    
    print(line)
    
