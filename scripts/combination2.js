var result = db.analysis.aggregate(
        [
                {$unwind : "$tags"} ,
                {$group: { _id : "$tags",count:{$sum:1}}},
                {$match: {count:{$gt: 100}}},
                {$sort:{count:-1}}
                
        ]
)

printjson(result);


//db.analysis.find({tags: {$all:['trojan','win32']}}).count()

