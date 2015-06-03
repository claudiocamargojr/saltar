var result = db.analysis.aggregate(
        [
                {$unwind : "$tags"} ,
                {$group: { _id : null, ts: {$addToSet: "$tags"}, count:{$sum:1}}} ,
                {$project: {_id : 0, tags: "$ts"}}
        ]
)

printjson(result);
