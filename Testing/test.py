# coding=utf8

'''
 version: December 10, 2019 02:29 PM
 Last revision: December 13, 2019 10:36 AM

@author: Chao-Hsuan Ke
'''

# shape
# input = Input(shape=(32, ))
# array = (10,)
# print(array)

# set (建立一個無序不重複元素集)
# list1=[1,2,3,4,5,4,3]
# s=set(list1)
# print(s)

# dict
dictUser = {'Name': 'Zara', 'Age': 20}
print(dictUser['Name'])
print(dictUser['Age'])

dictUser['Note'] = 'Child'
print(dictUser);

for key in dictUser:
    print(key, dictUser[key])

# enumerate
#lst = [1,2,3,4,5,6]
#lst = ['今','天','天','氣','好']
lst = ['E','L','S','A']
for index,value in enumerate(lst):
  print((index,value))
