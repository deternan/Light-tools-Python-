# coding=utf8

'''
RegularExpression (Number)
version: October 14, 2019 04:35 PM
Last revision: October 14, 2019 05:10 PM
  
Author : Chao-Hsuan Ke
'''

import re

patternStr = r"[a-zA-z]+"
input_str = "各位我又回來啦，我們接下來要開始進入我們專案的起始這個階段，專案起始我們會跟各位介紹兩個非常重要的 concept 還有方法，第一個就是專案章程，我想各位有沒有聽過 project charter";


text = "1998 was the year when the film titanic was released"
#result = re.search(r"[a-zA-z]+", text)
#print(result)
result = re.finditer(patternStr, text)
for str in result:
    print(str)