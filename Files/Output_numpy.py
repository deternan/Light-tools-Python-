# -*- coding: utf-8 -*-

'''
version: December 23 2019, 02:10 PM
Last revision: December 23 2019, 02:16 PM

Author : Chao-Hsuan Ke
'''

import numpy as np

base_dir = ''
outputfile = 'txtfile.txt'

myArr = np.arange(15).reshape(3, 5)
print(myArr)

aa = c = np.array( [ [1,2], [3,4] ], dtype= int)
print(aa)

# save
np.savetxt(base_dir + outputfile, aa)