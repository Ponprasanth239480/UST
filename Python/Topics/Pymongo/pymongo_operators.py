# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 15:48:56 2022

@author: prasanth
"""

from pymongo import MongoClient

if __name__ == "__main__":
    print("welcom to pymongo")
    client = MongoClient("mongodb://localhost:27017")
    print(client)
    db = client['pymongoDB']
    collection = db['transactions']
    
    
# =============================================================================
#     allDocuments = collection.aggregate([{'$group':{'_id':'$category','averageAmount':{'$avg':'$amount'}}}])
#     
#     for items in allDocuments:
#         #print(items)
#     countcategory = collection.aggregate([{'$group':{'_id':'$category',
#                                         'categorycount':{'$count':{}}}  },
#                                           {'$sort': { 'categorycount': -1 } }])
#         
#     for item in countcategory:
#         #print(item)
# =============================================================================
    countproduct = collection.aggregate([{'$group':{'_id':'$productname',
                                        'productcount':{'$count':{} } }  },
                                          {'$sort': { 'productcount': -1 } },{'$limit':5}])
        
    for item in countproduct:
        print(item)
    countproduct = collection.aggregate([{'$group':{'_id':'$productname',
                                        'productcount':{'$count':{}}}  },
                                          {'$sort': { 'productcount': 1 } },{'$limit':5}])
        
    for item in countproduct:
        print(item)