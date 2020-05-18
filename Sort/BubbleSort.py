# coding=utf8
'''
Created on January 08, 2018    11:32 PM
Last revised : May 18, 2020 03:13 PM
author: Chao-Hsuan Ke
'''

import random;
import unittest

# Random 
unsortData = random.sample(range(100), 10)
#print("Original Data:", unsortData)

def bubble_sort(sourceBubbleSortList):
    listLength = len(sourceBubbleSortList)
    i = 0
    while i < listLength - 1:
        j = listLength - 1
        while j > i:
            if sourceBubbleSortList[j] < sourceBubbleSortList[j - 1]:
                tempNum = sourceBubbleSortList[j]
                sourceBubbleSortList[j] = sourceBubbleSortList[j - 1]
                sourceBubbleSortList[j - 1] = tempNum
            j = j -1
        i = i +1

    return sourceBubbleSortList


class TestSortFunc(unittest.TestCase):
    def test_bubble_sort_1(self):
        arr = []
        self.assertEquals([], bubble_sort(arr))

    def test_bubble_sort_2(self):
        arr = [618]
        self.assertEquals([618], bubble_sort(arr))

    def test_bubble_sort_3(self):
        self.assertEquals(sorted(unsortData), bubble_sort(unsortData))



if __name__ == '__main__':
    # Unit Test
    # suite
    suite = unittest.TestSuite()
    tests = [TestSortFunc("test_bubble_sort_1"), TestSortFunc("test_bubble_sort_2"), TestSortFunc("test_bubble_sort_3")]
    suite.addTests(tests)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

    # Display
    sortData = bubble_sort(unsortData)
    print("Sort", sortData)