# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 10:35:01 2022

@author: prasanth
"""

from pymongo import MongoClient
import json

if __name__ == "__main__":
   
    client = MongoClient("mongodb://localhost:27017")
    
    db = client['restaurant']
    
    collection = db['rescollection']
    
    with open ('C:/PyMongo/restaurants-dataset.json',"r",encoding="utf-8") as file:
        record=file.read()
        record=record.replace('\n','')
        record=record.replace('}{','},{')
        record="[" + record + "]"
        file_data = json.loads(record)
        
    if isinstance(file_data, list):
        collection.insert_many(file_data)
    else:
        collection.insert_one(file_data)