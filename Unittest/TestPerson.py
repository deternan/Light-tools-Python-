# -*- coding: utf-8 -*-

'''
version: January 04 2021, 04:53 PM
Last revision: January 05 2021, 06:10 PM
'''

import unittest
from person import *

class TestPerson(unittest.TestCase):

    # def setUp(self):
    #     getTest = Person('John')
    #     print(getTest.getName())


    def test_checkName(self):
        #print(self.assertEqual('John', 'Tom'))
        #print(self.assertEqual('John', 'John'))
        #print('Tom')
        getTest = Person('John')
        print(getTest.getName())

    def test_checkAge(self):
        getTest = Person(123)
        print(getTest.getAge())

if __name__ == "__main__":
    unittest.main()