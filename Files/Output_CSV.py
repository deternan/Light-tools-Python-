# coding=utf8

'''
version: January 20, 2020 05:21 PM
Last revision: January 20, 2020 05:28 PM

Author : Chao-Hsuan Ke

'''

import csv

csvfile = 'output.csv'      # file full-location

f = open(csvfile, "w")
w = csv.writer(f)
w.writerow(['id', 'qid1', 'qid2', 'question1', 'question2', 'is_duplicate'])
w.writerow(['0', '1', '2', 'What is the step by step guide to invest in share market in india?', 'What is the step by step guide to invest in share market?', '0'])

f.close()


