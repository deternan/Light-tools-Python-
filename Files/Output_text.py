# coding=utf8

'''
version: September 23, 2019 10:40 AM
Last revision: December 09, 2019 03:14 PM
  
Author : Chao-Hsuan Ke

''' 

str = [1, 2, 3, 4, 5]
txtstr = ['abc\n', 'def\n']

outputFolder = ""                      # output folder name
outputFile = "output.txt"              # output file name

# open file
fp = open(outputFolder + outputFile, "a", encoding='UTF-8')       # 'a' --> overlapping
 
#write to output file
fp.writelines(txtstr)

# for i in str:
#     print(str[i-1])


fp.close()

