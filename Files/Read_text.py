# coding=utf8

'''
version: September 19, 2019 02:28 PM
Last revision: November 26, 2019 09:22 AM
  
Author : Chao-Hsuan Ke

''' 

filePath = "C:\\Users\\barry.ke\\Desktop\\";        # file path
fileName = "Song Recommendation.txt";        # file name

f = open(filePath + fileName, 'r', encoding="utf-8")
#print(f.read())                 # print all at once time
#print(len(f.readlines()))      # all line number

# read each lines
# for line in f:
#     print(line)

# read function
data = f.read()
print(len(data))

f.close()