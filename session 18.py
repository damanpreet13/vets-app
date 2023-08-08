"""
create account
network access 0.0.0.0/
"""
import pymongo
uri ="mongodb+srv://damanpreet01:abc@cluster0.crerpeh.mongodb.net/?retryWrites=true&w=majiority"
client = pymongo.MongoClient(uri)
db = client['myproject']
collections=db.list_collection_names()
#print(collections)
for collection in collections:
    print(collection)
documents = db['customer'].find()
for document in documents:
    print(document)
documents = db['pet'].find()
for document in documents:
    print(document)
documents = db['consultation'].find()
for document in documents:
    
    print(document)

