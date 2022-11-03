# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 10:26:33 2022

@author: prasanth
"""
from pymongo import MongoClient
import numpy as np
import pandas as pd
import json

def mongoimport (csv_path):
    
    hr_df = pd.read_csv(csv_path)
    
    payload = json.loads(hr_df.to_json(orient='records'))
    
    collection.delete_many({})
    collection.insert_many(payload)
    

if __name__ == "__main__":
    print("welcom to pymongo")
    client = MongoClient("mongodb://localhost:27017")
    print(client)
    db = client['HRdatabase']
    collection = db['EmpCollection']
    mongoimport('C:/PyMongo/HR-Employee-Attrition.csv')
    countdepartment = collection.aggregate([{'$group':{'_id':'$Department',
                                        'Departmentcount':{'$count':{} } }  },
                                          {'$sort': { 'Departmentcount': -1 } }])
    for item in countdepartment:
        print(item)
    countdepartment1 = collection.aggregate([{'$group':{'_id':'$Department',
                                        'Departmentcount':{'$count':{} } }  },
                                          {'$sort': { 'Departmentcount': -1 } },{'$limit':1}])
    for item in countdepartment1:
        print(item)
    topeducation = collection.aggregate([{'$group':{'_id':'$EducationField',
                                        'EducationFieldcount':{'$count':{} } }  },
                                          {'$sort': { 'EducationFieldcount': -1 } },{'$limit':1}])
    for item in topeducation:
        print(item)
    
    min_maxsalary = collection.aggregate([
        {'$group' : {'_id' : 'null', 'max salary':{ '$max' : '$Income'}, 
                    'min salary' : {'$min':'$Income'}}}, {'$project' : {'_id' : 0}}])
    for item in min_maxsalary:
        print(item)
    
    print('\nFind the AVG Monthly Income of overall employee : ')
    avgincome = collection.aggregate([
        {'$group' : {'_id' : 'null', 'avg salary':{ '$avg' : '$MonthlyIncome'}}}, 
                    {'$project' : {'_id' : 0}}])
    
    for item in avgincome:
        item['avg salary'] = np.round(item['avg salary'], 2) 
        print(item)

    print('\nFind the AVG PercentSalaryHike of employee : ')
    avgincome = collection.aggregate([
        {'$group' : {'_id' : 'null', 'avgsalary_hike':{ '$avg' : '$PercentSalaryHike'}}}, 
                    {'$project' : {'_id' : 0}}])
    
    for item in avgincome:
        item['avgsalary_hike'] = np.round(item['avgsalary_hike'], 2) 
        print(item)

    allDocuments = collection.aggregate([{'$match':{'Attrition':'Yes'}},{'$group':{'_id':'null','avgsalary_hike':{'$avg':'$PercentSalaryHike'}}},{'$project' : {'_id' : 0}}])
    for item in allDocuments:
        item['avgsalary_hike'] = np.round(item['avgsalary_hike'], 2) 
        print(item)
    allDocuments = collection.aggregate([{'$match':{'Attrition':'Yes'}},{'$group':{'_id':'$Department',
                                        'Attritioncount':{'$count':{} } }  },
                                          {'$sort': { 'Attritioncount': -1 } },{'$limit':1}])
    for items in allDocuments:
        print(items)
    print('\nFind the AVG Monthly Income of overall employee : ')
    # avgincome = collection.aggregate([
    #         {'$group' : {'_id' : '$EducationField', 'avgsalary':{ '$avg' : '$MonthlyIncome'},
    #                      'avgsalary1':{'$avg' : '$MonthlyIncome'},{'avgsalary':{'$lte':'avgsalary1'}}}}])
        
    # for item in avgincome:
    #     item['avg salary'] = np.round(item['avg salary'], 2) 
    #     print(item)
