# coding=utf8

'''
version: September 23, 2019 11:39 AM
Last revision: January 20, 2020 05:10 PM
  
Author : Chao-Hsuan Ke

''' 

import csv

csvfile = 'test.csv'      # file full-location

# include read head (first row)
with open(csvfile, "r", encoding="utf-8") as f:
    myCsv = csv.reader(f)
    headers = next(myCsv)
    for row in myCsv:
        print(row)


# no head (no (first row))
with open(csvfile, "r", encoding="utf-8") as f:
    myCsv = csv.reader(f)
    for row in myCsv:
        print(row)