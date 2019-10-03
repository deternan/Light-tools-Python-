# coding=utf8

'''
version: October 03, 2019 04:27 PM
Last revision: October 03, 2019 04:31 PM
  
Author : Chao-Hsuan Ke

'''

import json

j = json.loads('{"one" : "1", "two" : "2", "three" : "3","twoDimension" : {"lv2id":"777", "lv2name":"superman"}}')

print(j['two'])
print(j['twoDimension']["lv2id"])

# array list number (index)
for x in range(len(j)):
    print(x)


# array list 
for x in j:
    print(x)

