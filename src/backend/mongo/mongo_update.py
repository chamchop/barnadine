from pymongo import MongoClient

client = MongoClient('localhost', 27017)
table_name = 'local'
collection_name = 'barnardine'

def mongo_insert_record(table_name, collection_name, title, content):
    db = client[table_name]
    collection = db[collection_name]
    insert = {
        'title': title,
        'content': content
    }
    collection.insert_one(insert)
    print(f'inserted {insert}')

if __name__ == '__main__':
    title = 'Lorem ipsum'
    content = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
    mongo_insert_record(table_name, collection_name, title, content)    