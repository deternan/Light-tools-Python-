# coding=utf8

'''
RegularExpression (Number+English)
version: February 13, 2022 11:14 PM
Last revision: February 13, 2022 11:14 PM

Author : Chao-Hsuan Ke
'''

import re

patternStr = r"[a-zA-z]+"
input_str = "Biden and b2 Ukrainian M3 President Zelensky will speak 1a today";
capital = re.findall('[A-Za-z0-9]{2,4}', str(input_str))
print(capital)
