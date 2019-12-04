# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

'''
import tensorflow as tf
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
#print(sess.run(hello))
print(tf.__version__)
'''

from keras import Input

import numpy as np

input = Input(shape=(32, ))



array = np.array([[1,2,3],
                 [4,5,6]])

print(array)

print('number of dim:',array.ndim)
print('shape',array.shape)
print('size:',array.size)


shapeinput = shape=(2, 5)
print(shapeinput)

# Random
x_random = np.random.random((10,3))
print(x_random)

print(x_random.shape);

#print(array)


#print(arrayTT.shape)

#for index in arrayTT:
#    print(index)


