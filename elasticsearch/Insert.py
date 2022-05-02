# -*- coding: utf-8 -*-

'''
version: May 02 2022, 04:06 PM
Last revision: May 02 2022, 03:45 PM

Author : Chao-Hsuan Ke
'''

from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
es = Elasticsearch(["http://127.0.0.1:9200"])

data = {'name':'柯國成','id':'10010094', 'extension':'43115', 'phone':'550-16724'}
result = es.create(index='qmc_members', id=2, body=data)
print(result)
