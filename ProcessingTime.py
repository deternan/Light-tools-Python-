# coding=utf8

'''
executed time
created: October 28, 2019 01:19 PM
Last revision: October 28, 2019 01:57 PM
  
Author : Chao-Hsuan Ke
'''

#import timeit

 
import time
start_time = time.time()

outputStr = ''

for i in range(1, 10):
    for j in range(1, 10):
        outputStr = ''
        outputStr = str(i) + ' x ' + str(j) + ' = ' + str(i*j)
        print(outputStr)
        

print("--- %s seconds ---" % (time.time() - start_time))