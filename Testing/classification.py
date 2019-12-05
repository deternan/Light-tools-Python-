# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 17:17:15 2019
revised : December 05, 2019 11:34 AM

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

#print(X[1][0:4])


# encode class values as integers
encoder = LabelEncoder()
encoder.fit(Y)
encoded_Y = encoder.transform(Y)
# convert integers to dummy variables (i.e. one hot encoded)
dummy_y = np_utils.to_categorical(encoded_Y)


# define baseline model
def baseline_model():
	# create model
	model = Sequential()
	model.add(Dense(8, input_dim=4, activation='relu'))
	model.add(Dense(3, activation='softmax'))
	# Compile model
	model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
	return model


# evaluation
estimator = KerasClassifier(build_fn=baseline_model, epochs=200, batch_size=5, verbose=0)

# splitting data into training set and test set. If random_state is set to an integer, the split datasets are fixed.
X_train, X_test, Y_train, Y_test = train_test_split(X, dummy_y, test_size=0.3, random_state=0)
estimator.fit(X_train, Y_train)

#print(X_test)

# make predictions
pred = estimator.predict(X_test)

# inverse numeric variables to initial categorical labels
init_lables = encoder.inverse_transform(pred)

# k-fold cross-validate
seed = 42
np.random.seed(seed)
kfold = KFold(n_splits=10, shuffle=True, random_state=seed)
results = cross_val_score(estimator, X, dummy_y, cv=kfold)

for i in results:
    print(i)

#print(results)


print('OK')