import unittest
import sys
sys.path.insert(1, 'C://Programming//barnardine//services//analysis')
from gdp import *


class TestPostgresMethods(unittest.TestCase):

    def setUp(self):
        self.table_name = 'gdp_data'

    def test_gdp_analysis(self):    
        highest = highest_by_quarter(self.table_name)
        lowest = lowest_by_quarter(self.table_name)
        print('highest:')
        for index, number in highest:
            print(f'index: {index}, number: {number}')
        print('lowest:')
        for index, number in lowest:
            print(f'index: {index}, number: {number}')        

if __name__ == '__main__':
    unittest.main()