var result = db.analysis.aggregate(
        [
                {$unwind : "$tags"} ,
                {$group: { _id : "$tags",count:{$sum:1}}},
                {$sort:{count:-1}}
        ]
)

printjson(result);
