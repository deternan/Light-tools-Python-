# coding=utf8

'''
version: October 03, 2019 04:46 PM
Last revision: October 03, 2019 04:58 PM
  
Author : Chao-Hsuan Ke

'''

import json

input_file = open ('D:\\Phelps\\GitHub\\Light-tools (Python)\\Json\\myJSONArray.json')      # file path
json_array = json.load(input_file)


for item in json_array:
    print(item)
#     print("id:" + item['id'])
#     print("name:" + item['name'])
