from pymongo import MongoClient

client = MongoClient('localhost', 27017)

def mongo_delete_all_records(table_name, collection_name):
    db = client[table_name]
    collection = db[collection_name]
    collection.delete_many({})
    print (f'deleted rows from {collection}')

if __name__ == '__main__':
    mongo_delete_all_records('local', 'barnardine')