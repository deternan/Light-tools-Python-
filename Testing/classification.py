# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 17:17:15 2019

@author: 
    
Reference    
https://www.itread01.com/content/1536178966.html    

"""

import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.wrappers.scikit_learn import KerasClassifier
from keras.utils import np_utils
from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.preprocessing import LabelEncoder

# load dataset
dataframe = pd.read_csv("C:\\Users\\barry.ke\\Desktop\\iris_training.csv", header=None)
dataset = dataframe.values
X = dataset[:, 0:4].astype(float)
Y = dataset[:, 4]

print(X[1][0:4])

print('OK')