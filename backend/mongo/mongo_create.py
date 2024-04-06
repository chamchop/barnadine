from pymongo import MongoClient

client = MongoClient('localhost', 27017)
table_name = 'local'
collection_name = 'barnardine'

def mongo_create(table_name, collection_name):
    db = client[table_name]
    collection = db[collection_name]
    print(f'created {collection}')

def mongo_insert(table_name, collection_name, title, content):
    db = client[table_name]
    collection = db[collection_name]
    insert = {
        'title': title,
        'content': content
    }
    collection.insert_one(insert)
    print(f'inserted {insert}')

def mongo_print(table_name, collection_name):
    db = client[table_name]
    collection = db[collection_name]
    data = collection.find({})
    for doc in data:
        print(doc)

if __name__ == '__main__':
    mongo_print(table_name, collection_name)