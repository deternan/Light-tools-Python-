# -*- coding: utf-8 -*-

'''
version: May 02 2022, 05:06 PM
Last revision: May 02 2022, 08:40 PM

Author : Chao-Hsuan Ke
'''

'''
Reference
https://iter01.com/566479.html

'''

from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search

es = Elasticsearch(["http://127.0.0.1:9200"])

index_name = 'qmc_members'

# method 1
#result = dict()
#result = es.get(index = index_name, id = 1)
#print(result)

querybody = {
    "size": 5,
    "query": {
        "match": {
            "name": "張淑貞"
        }
    }
}

# querybody = {
#     "size": 5,
#     "query": {
#         "bool": {
#             "must": {
#                 "term": {
#                     "name": "張淑貞"
#                 }
#             }
#         }
#     }
# }

# method 2
res = es.search(index=index_name, body=querybody)
print(res)
#print(res.values())

# method 3
s=Search(using=es,index=index_name).filter("match",name='張淑貞')
response=s.execute()
print(response[0])
print(len(response))
