# coding=utf8

'''
version: September 23, 2019 02:28 PM
Last revision: September 23, 2019 02:28 PM
  
Author : Chao-Hsuan Ke

''' 

listArray = [1,3,6,18,27,11,2,21]

# ascendent order
listArray.sort(key=None, reverse=False)

for i in listArray:
    print (i)

print ('--------------------------------')

# descending order
listArray.sort(key=None, reverse=True)
for i in listArray:
    print (i)