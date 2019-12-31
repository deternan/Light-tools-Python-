# -*- coding: utf-8 -*-

'''
version: December 25 2019, 11:40 AM
Last revision: December 31 2019, 10:34 AM

Author : Chao-Hsuan Ke
'''

import lucene

lucene.initVM(vmargs=['-Djava.awt.headless=true'])
print('lucene', lucene.VERSION)
