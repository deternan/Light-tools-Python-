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
# dictUser = {'Name': 'Zara', 'Age': 20}
# print(dictUser['Name'])
# print(dictUser['Age'])
#
# dictUser['Note'] = 'Child'
# print(dictUser);
#
# for key in dictUser:
#     print(key, dictUser[key])

# enumerate (多用於在for循環中得到計數，利用它可以同時獲得索引和值，即需要index和value值的時候可以使用)
#lst = [1,2,3,4,5,6]
#lst = ['今','天','天','氣','好']
# lst = ['E','L','S','A']
# for index,value in enumerate(lst):
#   print((index,value))

# Max
a = [-10, -9, -8, 1, 3, -4, 6]
# type 1
tmp = max(a, key=lambda x: x)
print(tmp)
# type 2
tmp = max(a, key=lambda x: abs(x))
print(tmp)
