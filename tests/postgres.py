import unittest
import psycopg2
import sys
sys.path.insert(1, 'C://Programming//barnardine//backend//postgres')
from postgres_create import *
from postgres_read import *
from postgres_update import *
from postgres_delete import *
from config import load_config
config = load_config()

class TestPostgresMethods(unittest.TestCase):

    def setUp(self):
        self.table_name = 'gdp_data'
        self.col_1 = 'Period'
        self.col_2 = 'Value'

    # def test_create_table(self):
    #     create_table(self.table_name, self.col_1, self.col_2)

    # def test_update_table(self):
    #     update_row(self.table_name, self.col_1, self.col_2, 'today', '1')

    def test_read_table(self):
        table = read_table(self.table_name)
        self.assertIsNotNone(table)

    # def test_read_record(self):
    #     record = read_record(self.table_name, 9)
    #     print(record)
    #     self.assertIsNotNone(record)

    # def test_delete_all_records(self):
    #     delete_all_records(self.table_name)
    #     record = read_record(self.table_name, 1)
    #     self.assertIsNone(record)

    # def test_delete_record(self):
    #     delete_record(self.table_name, 1)
    #     record = read_record(self.table_name, 1)
    #     self.assertIsNone(record)

    # def test_delete_table(self):
    #     delete_table(self.table_name)
    #     table = read_table(self.table_name)
    #     print(table)
    #     self.assertIsNone(table)

if __name__ == '__main__':
    unittest.main()