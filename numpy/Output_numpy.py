# -*- coding: utf-8 -*-

'''
version: December 23 2019, 02:10 PM
Last revision: December 23 2019, 02:43 PM

Author : Chao-Hsuan Ke
'''

import numpy as np

base_dir = ''
outputfile = 'txtfile.txt'

myArr = np.arange(15).reshape(3, 5)
print(myArr)

aa = np.array( [ [1,2], [3,4] ], dtype=int)
np.around(aa, decimals=5)
print(aa)

array_x2 = np.random.randint(10, size=(3,4))
print(array_x2)

# save
np.savetxt(base_dir + outputfile, array_x2, fmt='%2.5f')
