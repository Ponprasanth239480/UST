# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 12:33:00 2022

@author: prasanth
"""

import pymongo

if __name__ == "__main__":
    print("welcom to pymongo")
    client = pymongo.MongoClient("mongodb://localhost:27017")
    print(client)
    allDBS = client.list_database_names()
    print(allDBS)
    collection = client['pymongoDB']
    print(collection.list_collection_names())
    collection_1 = client['bookstoredb']
    print(collection_1.list_collection_names())
    myCollection = collection['myFirstCollection']
    document = [{'_id': 4, 'name':'Lenovo Ideapad', 'price':128000, 
                  'color': ["Gray","Gold","Black"], 'ram':[4096,8196],'storage':[1024, 2048, 4096]},
                {'_id': 5, 'name':'Macbook', 'price':8000, 
                  'color': ["Black","Silver"], 'ram':[4096], 'storage': [1024, 2048]}]
    #myCollection.insert_many(document)
    print(myCollection.distinct('name'))
    print(myCollection.distinct('price'))
    
    #myCollection.update_one({'_id':5}, {'$set':{'price':88000}})
    #myCollection.update_many({},{'$rename':{'name':'Laptop Name'}})
    
    allDocuments = myCollection.find()
    for item in allDocuments:
        print(item)
        
    
    


    