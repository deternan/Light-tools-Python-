# -*- coding: utf-8 -*-

'''
version: December 23 2019, 03:00 PM
Last revision: December 23 2019, 03:00 PM

Author : Chao-Hsuan Ke
'''

'''
Reference
https://www.w3resource.com/python-exercises/numpy/python-numpy-exercise-86.php
'''

import numpy as np
A = np.random.random((2,3)) # Create a constant array
#print(A)
B = np.array([[1],[3]])
D = np.concatenate((A,B),axis=1)

#--------------------------------------------

category = np.array([[1,0,0,0,0,0,0],
 [0,0,1,0,0,0,0],
 [0,0,0,0,0,0,1]])

print(category)

categoryType = np.zeros(shape=(len(category), 1))
#print(categoryType)

kk = 0
for i in category:
    index = np.argwhere(i == np.max(i, axis=0))
    #print(i, index)
    categoryType[kk] = index
    kk +=1

print(categoryType)
print((np.append(category, categoryType, axis=1)))

# sample
# x = np.array([[10,20,30], [40,50,60]])
# y = np.array([[100], [200]])
# print(np.append(x, y, axis=1))