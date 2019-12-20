# coding=utf8
'''
 version: October 15, 2019 05:59 PM
 Last revision: December 20, 2019 09:32 AM
  
 Author : Chao-Hsuan Ke
 
 Reference
 https://docs.python.org/3/library/random.html
 https://github.com/python/cpython/blob/3.6/Lib/random.py
 
'''

import random
from random import randint

min = 0;
max = 30;

# for i in range(1, 11):
#     print(randint(min,max))

# non duplication

total = 100
li = [i for i in range(total)]
res = []
num = 30
for i in range(num):
    t = random.randint(i,total-1)
    res.append(li[t])
    li[t], li[i] = li[i], li[t]

print(res)