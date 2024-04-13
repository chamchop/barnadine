import unittest
import sys
from unittest.mock import patch
import mongomock
sys.path.insert(1, 'C:/Programming/barnardine/src/backend/mongo')
from mongo_create import *
from mongo_read import *
from mongo_update import *

class TestMongoDBOperations(unittest.TestCase):
    @patch('mongo_create.MongoClient') 
    def setUp(self, mock_mongo_client):
        self.mock_client = mongomock.MongoClient()
        mock_mongo_client.return_value = self.mock_client

        self.table_name = 'testdb'
        self.collection_name = 'testcollection'

    # def test_mongo_create(self):
    #     mongo_create(self.table_name, self.collection_name)

    # def test_mongo_insert(self):
    #     title = "Test Title"
    #     content = "Test content"
    #     mongo_insert(self.table_name, self.collection_name, title, content)
    #     inserted_data = self.mock_client[self.table_name][self.collection_name].find_one({"title": title})

    def test_mongo_read_all(self):
        self.mock_client[self.table_name][self.collection_name].insert_one({"title": "Existing Title", "content": "Existing content"})
        data = mongo_read_all()
        for record in data:
            print(record)                      

if __name__ == '__main__':
    unittest.main()
