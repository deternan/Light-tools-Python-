# coding=utf8

'''
 matrix calculation based on Numpy
version: October 01, 2019 05:28 PM
Last revision: October 01, 2019 05:3 PM
  
Author : Chao-Hsuan Ke

'''

import numpy 

x = numpy.array([[1, 2], [5, 6]]) 
y = numpy.array([[3, 4], [7, 8]]) 


#add
print ("The element wise addition of matrix is : ") 
print (numpy.add(x,y)) 

# using divide() to divide matrices 
print ("The element wise division of matrix is : ") 
print (numpy.divide(x,y)) 

# Subtraction
print (numpy.subtract(x,y)) 

