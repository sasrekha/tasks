import pymongo

url = "mongodb://localhost:27017"

mongoClient = pymongo.MongoClient(url)

mydb = mongoClient["mydb"]

mycollection = mydb["users"]

# find(query, projections)
# documents = mycollection.find({"City":{"$eq","El Paso"}})

# print(list(documents))

# for document in documents:
#     print(document["Vendor"])

mycollection.insert_one({
    "name":"kamala",
    "email":"kamala@demo.com",
    "password":"2123127"
})

users = [{}, {}, {}]

mycollection.insert_many(users)

documents = mycollection.find(
        {
            "name":{"$eq":"prasad"}
        },
        {"_id":0,"name":1,"email":1}
        )


print(list(documents))

mycollection.update_one(
    {
        "name":{"$eq":"prasad"}
    },
    {"$set":
        {"password":"12345678"}
    })

