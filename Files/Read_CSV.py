# coding=utf8

'''
version: September 23, 2019 11:39 AM
Last revision: September 23, 2019 11:48 AM
  
Author : Chao-Hsuan Ke

''' 

import csv

csvfile = 'test.csv'

# include read head (first row)
with open(csvfile) as f:
    myCsv = csv.reader(f)
    headers = next(myCsv)
    for row in myCsv:
        print(row)


# no head (no (first row))
with open(csvfile) as f:
    myCsv = csv.reader(f)    
    for row in myCsv:
        print(row)