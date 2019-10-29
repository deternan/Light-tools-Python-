# coding=utf8

'''
Random (SEED)
created: October 29, 2019 09:32 AM
Last revision: October 29, 2019 09:34 AM
  
Author : Chao-Hsuan Ke
'''

import random

random.seed(618)        # setting Random SEED number

for x in range(10):
    print (random.randint(1,100))