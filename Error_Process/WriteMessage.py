# coding=utf8

'''
 output Error Message
version: October 02, 2019 04:17 PM
Last revision: October 02, 2019 04:17 PM
  
Author : Chao-Hsuan Ke

'''

from datetime import datetime, timedelta
import time

outputFolder = ""                      # output folder name
outputFile = ""                         # output file name

# open file
fp = open(outputFolder + outputFile, "a")       # 'a' --> overlapping

# Error message
# current time
#print(datetime.now())
em = 'Error    '+ str(datetime.now()) 

# write error message 
fp.writelines(em+'\n')
 
print("finished")
 
fp.close()

