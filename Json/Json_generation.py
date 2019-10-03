# coding=utf8

'''
version: October 03, 2019 04:06 PM
Last revision: October 03, 2019 04:09 PM
  
Author : Chao-Hsuan Ke

'''

import json

# type 1
data = {}
data['key'] = 'value'
json_data = json.dumps(data)
print ('JSON: ', json_data)

# type 2
my_json_string = json.dumps({'key1': '123', 'key2': '456'})
print(my_json_string)
