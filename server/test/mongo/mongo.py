from pymongo import *
import json, re

def post_Data(file):
    file = open(file, 'r')
    post = json.load(file)
    result = collection.insert(post)
    return result


client = MongoClient('localhost', 27017)

db = client['JokenSystem']
collection = db['member']
# collection = db.member
# collection.update({ "ID": "orehajyaian", "personal":{"SNS" : { "Twiiter":"@OreJaian"} }})
# result = post_Data('data.json')
# print(result)
# post_Data('data1.json')
# print(re)
# all = list(collection.find())
all = list(collection.find({}))
# aa = list(collection.find({ "ID": "orehajyaian" }))
# c = dict(aa[0])
# del c['_id']
# b = json.dumps(c)
print(all)
# print(aa)
# print(aa[0])
# SNS_info = c['personal']['SNS']
# SNS_info['LINE'] = 'OreJyaianSama'
# print(SNS_info)
# print(c)
# o_id = c['_id']
# a = collection.update({"_id":o_id}, c)
# print(a['updatedExisting'])
# collection.insert(c)
# print(c)
# print(list(aa[1]))
# user = "admin"
# # for i in range(len(aa)):
# #     print(aa[i]['user'])
# print(aa[0]['user']['admin'])
# print('###########################')
# print(str(b))
# a = aa['user']
# print()

# BDデータ削除
# collection.remove( {"ID": "orehajyaian"} )
# collection.remove()
