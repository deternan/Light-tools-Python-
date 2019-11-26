# coding=utf8

'''
version: September 19, 2019 02:28 PM
Last revision: November 26, 2019 09:30 AM
  
Author : Chao-Hsuan Ke

''' 

filePath = "";        # file path
fileName = "";        # file name

f = open(filePath + fileName, 'r', encoding="utf-8")
#print(f.read())                 # print all at once time
#print(len(f.readlines()))      # all line number

# read each lines
# for line in f:
#     print(line)

# read function
data = f.read()
#print(len(data))
lines = data.split('\n')
print(len(lines))

f.close()