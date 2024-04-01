import requests
from bs4 import BeautifulSoup
import psycopg2
import pandas as pd
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

table_name = 'gdp_data'
col_1 = 'period'
col_2 = 'value'

def top_five_numbers(numbers):
    top_five = sorted(numbers, reverse=True)[:5]
    return top_five

if __name__ == '__main__':
    data = read_table('ons_gdp')
    print(data[0][2])
    # if data:
    #     print("All data from the table:")
    #     for row in data:
    #         print(row[0], row[1])
        # top = top_five_numbers(data[1])
        # print(top)
    # else:
    #     print("Failed to read data from the table.")       