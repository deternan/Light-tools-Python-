# -*- coding: utf-8 -*-

'''
version: March 24, 09:20 AM
Last revision: March 24, 02:30 PM

Author : Chao-Hsuan Ke
'''

'''
Reference

https://api.mongodb.com/python/current/tutorial.html
https://www.w3schools.com/python/python_mongodb_find.asp

'''

from pymongo import MongoClient, errors
from bson.objectid import ObjectId

ip = ''     ## db IP
port = 8083             ## db PORT

dbName = 'ncov2019'
collectionName = 'news_cdc'


try:
    # try to instantiate a client instance
    client = MongoClient('mongodb://' + ip + ':' + str(port), serverSelectionTimeoutMS = 3000)
    # client = MongoClient(
    #     host = [ ip + str(port) ],
    #     serverSelectionTimeoutMS = 3000
    # )
except errors.ServerSelectionTimeoutError as err:
    client = None
    print ("pymongo ERROR:", err)

'''
db list
'''
if client != None:
    # the list_database_names() method returns a list of strings
    database_names = client.list_database_names()
    #print ("database_names() TYPE:", type(database_names))
    #print ("The client's list_database_names() method returned", len(database_names), "database names.")
    # for i in database_names:
    #     print(i)

'''
collection list
'''
db = client[dbName]
if db != None:
    collections = db.list_collection_names()
    # for i in collections:
    #     print(i)


'''
get collection data
'''
collection = db[collectionName]
# if collections != None:
#     for x in collection.find():
#         print(x)


'''
query by ObjectId
'''
def get(post_id):
    print(ObjectId(post_id))
    # Convert from string to ObjectId:
    document = collection.find_one({'_id': ObjectId(post_id)})
    print(document)


idStr = '5e787132e2e8d50291462a8a'
get(idStr)

'''
insert document
'''
