# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pymongo

if __name__ == "__main__":
    print("welcom to pymongo")
    client = pymongo.MongoClient("mongodb://localhost:27017")
    print(client)
    db = client['pymongoDB']
    collection = db['myFirstCollection']
    document1 = {'_id': 1, 'name':'Macbook', 'price':178000, 
                  'color': ["Gray","Silver"], 'storage': [512,128,256]}
    #collection.insert_one(document1)
    document2 = [{'_id': 2, 'name':'Lenovo Thinkpad', 'price':118000, 
                  'color': ["Gray","Gold","Black"], 'ram':[4096,8196],'storage':[1024, 2048, 4096]},
                {'_id': 3, 'name':'Dell Inspiron', 'price':98000, 
                  'color': ["Black","Silver"], 'ram':[4096,8196], 'storage': [1024, 2048, 4096]}]
    #collection.insert_many(document2)
    first = collection.find_one() 
    print(first)
    second = collection.find_one({'_id': 3}) 
    print(second)
    alldocuments = collection.find()
# =============================================================================
#     for item in alldocuments:
#         print(item)
# =============================================================================
    alldocuments = collection.find({},{'name':1,'_id':0,'price':1})
    for item in alldocuments:
        print(item)

