import unittest
import sys
from unittest.mock import patch
import mongomock
sys.path.insert(2, 'C://Programming//barnardine//backend//mongo')
from mongo_create import *

class TestMongoDBOperations(unittest.TestCase):
    @patch('mongo_create.MongoClient') 
    def setUp(self, mock_mongo_client):
        self.mock_client = mongomock.MongoClient()
        mock_mongo_client.return_value = self.mock_client

        self.table_name = 'testdb'
        self.collection_name = 'testcollection'

    def test_mongo_create(self):
        mongo_create(self.table_name, self.collection_name)

    def test_mongo_insert(self):
        title = "Test Title"
        content = "Test content"
        mongo_insert(self.table_name, self.collection_name, title, content)
        inserted_data = self.mock_client[self.table_name][self.collection_name].find_one({"title": title})
        # self.assertIsNotNone(inserted_data)
        # self.assertEqual(inserted_data["content"], content)

    def test_mongo_print(self):
        self.mock_client[self.table_name][self.collection_name].insert_one({"title": "Existing Title", "content": "Existing content"})
        with patch('builtins.print') as mocked_print:
            mongo_print(self.table_name, self.collection_name)

if __name__ == '__main__':
    unittest.main()
