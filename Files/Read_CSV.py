# coding=utf8

'''
version: September 23, 2019 11:39 AM
Last revision: May 01, 2022 11:30 PM
  
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


# 讀取 CSV 檔內容，將每一列轉成一個 dictionary
with open(csvfile, newline='') as f:
  rows = csv.DictReader(f)
  # 以迴圈輸出指定欄位
  for row in rows:
    print(row['name'], row['id'], row['extension'], row['phone'])