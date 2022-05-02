# -*- coding: utf-8 -*-

'''
version: May 02 2022, 03:21 PM
Last revision: May 02 2022, 03:40 PM

Author : Chao-Hsuan Ke
'''

from elasticsearch import Elasticsearch
import json

def create_index(es):
    body = dict()
    body['settings'] = get_setting()
    body['mappings'] = get_mappings()
    print(json.dumps(body))
    es.indices.create(index='qmc_members', body=body)


def get_setting():
    settings = {
        "index": {
            "number_of_shards": 3,
            "number_of_replicas": 2
        }
    }

    return settings


def get_mappings():
    mappings = {
        "properties": {
            "sid": {
                "type": "integer"
            },
            "name": {
                "type": "text"
            },
            "id": {
                "type": "text"
            },
            "extension": {
                "type": "text"
            },
            "phone": {
                "type": "text"
            }
        }
    }

    return mappings


if __name__ == "__main__":
    #es = Elasticsearch(hosts='127.0.0.1', port=9200)
    es = Elasticsearch(["http://127.0.0.1:9200"])
    create_index(es)