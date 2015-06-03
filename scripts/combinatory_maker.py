from pymongo import MongoClient
import json
import copy
import itertools


def connect():
        client = MongoClient('castleblack', 27017)
        db = client.virus_total
        return db
        
def get_collection(db):
        analysis = db.analysis
        pipeline = [
                {"$unwind" : "$tags"} ,
                {"$group": { "_id" : "$tags","count":{"$sum":1}}},
                {"$match": {"count":{"$gt": 1000}}},
                {"$sort":{"count":-1}}                
        ]
        collection = analysis.aggregate(pipeline)
        return collection

def combinate2(collection,db):
        result = {}
        
        for tag in collection:
                for tag2 in collection:
                        if tag2==tag:
                                continue
                        key =  [tag["_id"],tag2["_id"]]
                        key.sort()
                        result[key[0]+'-'+key[1]] = findGroupOfTags([tag2["_id"],tag["_id"]],db)
        return result

def findGroupOfTags(tags,db):
        return db.analysis.find({"tags": {"$all":tags}}).count()      

if __name__ == "__main__":
        db = connect()
        collection = get_collection(db)
        result=combinate2(collection,collection2,db)
        print json.dumps(result,indent=2)
        #print(findGroupOfTags(['win32'],db))
        



