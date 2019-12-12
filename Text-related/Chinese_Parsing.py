# coding=utf8

'''
 version: December 12, 2019 02:29 PM
 Last revision: December 12, 2019 02:35 PM

@author: Chao-Hsuan Ke
'''

import re

#x = 'a12121assa'
x = '根據上面這張圖，我們能將 RNN 的輸入與輸出關係更細分幾種情形'
r1 = '[a-zA-Z0-9’!"#$%&\'()*+,-./:;<=>?@，。?★、…【】《》？“”‘’！[\\]^_`{|}~]+'

#print(re.sub(r1, '', x))

newStr = re.sub(r1, '', x)
resultStr = newStr.replace(' ', '')
print(resultStr.strip())

