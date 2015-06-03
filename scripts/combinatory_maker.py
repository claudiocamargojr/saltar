from pymongo import MongoClient
import json
import copy
import itertools
import operator

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
        result = [tag for tag in collection]
        
        print 'Found', len(result), 'tags'
        return result

def combinate2(collection,db):
        result = {}
        
        total = len(collection)
        for i in range(total):
                tag = collection[i]
                print 'Processing',i+1, "/", total
                
                for j in range(i, total):
                        tag2 = collection[j]
                        if tag2==tag:
                                continue
                        key =  [tag["_id"],tag2["_id"]]
                        key.sort()
                        result[key[0]+'-'+key[1]] = findGroupOfTags(key,db)

	sorted_result = ( (x[0], x[1]) for x in (sorted(result.items(), key=operator.itemgetter(1), reverse=True)) )

        return sorted_result

def combinate3(collection,db):
        result = {}
        
        total = len(collection)
        for i in range(total):
                tag = collection[i]
                print 'Processing',i+1, "/", total
                
                for j in range(i, total):
                        tag2 = collection[j]
                        if tag == tag2:
                                continue                        
                        for k in range(j, total):
                                tag3 = collection[k]
                                if tag2 == tag3:
                                        continue                        

                                key =  [tag["_id"],tag2["_id"], tag3["_id"]]
                                key.sort()
                                result[key[0]+'-'+key[1] + '-' + key[2]] = findGroupOfTags(key,db)

	sorted_result = ( (x[0], x[1]) for x in (sorted(result.items(), key=operator.itemgetter(1), reverse=True)) )

        return sorted_result
        
def findGroupOfTags(tags,db):
        return db.analysis.find({"tags": {"$all":tags}}).count()      

if __name__ == "__main__":
        db = connect()
        collection = get_collection(db)
        result=combinate3(collection, db)
        for item in result:
                print item[0], ":",item[1]
        #print(findGroupOfTags(['win32'],db))
        



