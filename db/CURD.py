# -*- coding: utf-8 -*-

'''
version: March 24, 09:20 AM
Last revision: March 24, 10:13 AM

Author : Chao-Hsuan Ke
'''

'''
Reference

https://api.mongodb.com/python/current/tutorial.html
https://www.w3schools.com/python/python_mongodb_find.asp

'''

from pymongo import MongoClient, errors

ip = ''
port = 8083

dbName = 'ncov2019'
collectionName = 'news_cdc'

# client = MongoClient('mongodb://'+ ip + ':' + str(port))
# db = client.test_database
# print(db)
# client.close()

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
    print ("The client's list_database_names() method returned", len(database_names), "database names.")
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
mycollection = db[collectionName]
if mycollection != None:
    for x in mycollection.find():
        print(x)


