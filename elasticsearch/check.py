# -*- coding: utf-8 -*-

'''
version: May 02 2022, 03:41 PM
Last revision: May 02 2022, 03:45 PM

Author : Chao-Hsuan Ke
'''

from elasticsearch import Elasticsearch

es = Elasticsearch(["http://127.0.0.1:9200"])
index_name = 'qmc_members'

result = es.indices.exists(index=index_name)
print(result)