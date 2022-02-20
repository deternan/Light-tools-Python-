# coding=utf8

'''
remove duplicated items in list
created: February 20, 2022 07:26 PM
Last revision: February 20, 2022 07:26 PM

Author : Chao-Hsuan Ke
'''

from collections import Counter

l = ["a", "b", "b"]
final_new_menu = list(set(l))
print(final_new_menu)
