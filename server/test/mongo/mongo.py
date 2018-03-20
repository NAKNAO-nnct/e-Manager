from pymongo import *
import json

def post_Data():
    file = open('data.json', 'r')
    post = json.load(file)
    collection.insert_many(post)


client = MongoClient('localhost', 27017)

db = client['test-database']
collection = db.test_collection

post_Data()

print(collection.find_one())

# print(collection.find_one({"user": "admin"}))
re = collection.find_one()
print(re['user']['admin'])

# BDデータ削除
# collection.remove({'passwd':'qaz'})
collection.remove()

