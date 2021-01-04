# -*- coding: utf-8 -*-

'''
version: January 01 2021, 04:50 PM
Last revision: January 01 2021, 06:20 PM
'''

class Person:

    def __init__(self, input):
        self.inputStr = input

    def getName(self):
        strCheck = isinstance(self.inputStr, str)
        #print('strCheck', strCheck)
        return strCheck


    def getAge(self):
        intCheck = isinstance(self.inputStr, int)
        #print('intCheck', intCheck)
        return intCheck