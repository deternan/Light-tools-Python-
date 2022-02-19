# coding=utf8

'''
RegularExpression (Number+English)
version: February 18, 2022 08:35 PM
Last revision: February 18, 2022 08:35 PM

Author : Chao-Hsuan Ke
'''

def merge_two_dicts(x, y):
    """Given two dicts, merge them into a new dict as a shallow copy."""
    z = x.copy()
    z.update(y)
    return z

#x = {'a': 1, 'b': 2}
#y = {'b': 3, 'c': 4}
x = {'16': ['fig', 'descriptions fig'], '25': ['mar', 'filed mar']}
y = {'119': ['35 usc', 'benefit 35 usc']}


z = merge_two_dicts(x, y)
print(z)

x = {}
y = {}
z = merge_two_dicts(x, y)
print(z)

x = []
y = []
z = merge_two_dicts(x, y)
print(z)