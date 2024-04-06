from pymongo import MongoClient

client = MongoClient('localhost', 27017)

def mongo_create(table_name, collection_name):
    db = client[table_name]
    collection = db[collection_name]
    print(f'created {collection}')
