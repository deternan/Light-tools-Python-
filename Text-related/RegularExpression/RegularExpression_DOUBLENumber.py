# coding=utf8

'''
RegularExpression (Number)
version: October 14, 2019 03:09 PM
Last revision: October 14, 2019 03:14 PM
  
Author : Chao-Hsuan Ke
'''

import re

pattern_num = '([0-9]+\\.?[0-9]+)'

input_str = "12.45aa69.7and60";

p = re.compile(pattern_num);
m = re.search(pattern_num, input_str)

print(m.group())
