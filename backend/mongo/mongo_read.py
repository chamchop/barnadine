from pymongo import MongoClient

client = MongoClient('localhost', 27017)
table_name = 'local'
collection_name = 'barnardine'

def mongo_read_all():
    db = client[table_name]
    collection = db[collection_name]
    data = list(collection.find({}))
    items = [{"title": doc["title"], "content": doc["content"]} for doc in data]
    return items