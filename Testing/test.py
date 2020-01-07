# coding=utf8

'''
 version: December 10, 2019 02:29 PM
 Last revision: January 06, 2020 01:42 PM

@author: Chao-Hsuan Ke
'''

import numpy as np

# 1) shape
# input = Input(shape=(32, ))
# array = (10,)
# print(array)

rng = np.random.RandomState(1)
# 顯示小數點下兩位，保持畫面簡潔
np.set_printoptions(precision=2)

X = rng.normal(scale=5, size=(2, 20))
print('X.shape:', X.shape, '\n')
print(X)
#print(X[:, 0])
print(X[0, :])
print(X[1, :])

# 2) set (建立一個無序不重複元素集)
# list1=[1,2,3,4,5,4,3]
# s=set(list1)
# print(s)

# 3) dict
# dictUser = {'Name': 'Zara', 'Age': 20}
# print(dictUser['Name'])
# print(dictUser['Age'])
#
# dictUser['Note'] = 'Child'
# print(dictUser);
#
# for key in dictUser:
#     print(key, dictUser[key])

# 4) enumerate (多用於在for循環中得到計數，利用它可以同時獲得索引和值，即需要index和value值的時候可以使用)
#lst = [1,2,3,4,5,6]
#lst = ['今','天','天','氣','好']
# lst = ['E','L','S','A']
# for index,value in enumerate(lst):
#   print((index,value))

# 5) Max
#a = [-10, -9, -8, 1, 3, -4, 6]
# type 1
# tmp = max(a, key=lambda x: x)
# print(tmp)
# type 2
# tmp = max(a, key=lambda x: abs(x))
# print(tmp)

# 6) zip (二維矩陣變換（矩陣的行列互換） ; 先比對 key 值, 再比對 value)

# prices = {
#     'A':123,
#     'B':450.1,
#     'C':12,
#     'E':444,
# }
#
# max_prices = max(zip(prices.values(), prices.keys()))
# print(max_prices) # (450.1, 'B')
#
# for abc in prices:
#     print(abc, prices.get(abc))
#
# testZip = zip(prices.keys(), prices.values())
# for aa in testZip:
#     print(aa)
#
# testZip = zip(prices.values(), prices.keys())
# for aa in testZip:
#     print(aa)