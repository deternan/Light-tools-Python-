# -*- coding: utf-8 -*-

'''
version: December 30 2019, 04:26 PM
Last revision: December 30 2019, 04:26 PM

Author : Chao-Hsuan Ke
'''

import sys

# print('Plase input your name: ')
# name = sys.stdin.readline()
# print('Hello ', name)

text = 'Synthetic opioids like fentanyl ravaged the US during the last decade. They may do even more damage to Asia in the next'
for n, l in enumerate(text):
    print(n, l)

#print(len(temp))
temp = text.split(' ')
for i in temp:
    print(i)

