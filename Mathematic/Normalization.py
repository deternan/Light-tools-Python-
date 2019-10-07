# coding=utf8

'''
version: October 03, 2019 04:27 PM
Last revision: October 07, 2019 05:12 PM
  
Author : Chao-Hsuan Ke

'''

from sklearn import preprocessing 
import numpy as np

arrayTest = np.array([[10, 2.7, 3.6],
              [-100, 5, -2],
              [120, 20, 40]], dtype=np.float64)



print(preprocessing.scale(arrayTest))

