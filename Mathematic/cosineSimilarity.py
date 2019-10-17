# coding=utf8

'''
cosineSimilarity
version: October 17, 2019 06:15 PM
Last revision: October 17, 2019 06:17 PM
  
Author : Chao-Hsuan Ke
'''

from numpy import dot
from numpy.linalg import norm

aMatrix = [1, 50, 6, 18]
bMatrix = [2, 54, 13, 15]

cos_sim = dot(aMatrix, bMatrix)/(norm(aMatrix)*norm(bMatrix))

print(cos_sim)

