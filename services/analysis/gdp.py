import sys
import re
sys.path.insert(1, 'C://Programming//barnardine//backend//postgres')
from postgres_read import *
from config import load_config
config = load_config()

table_name = 'gdp_data'

def highest_by_quarter():
    data = read_table(table_name)
    list = [row for row in data]
    pattern = r'2020|2021'
    filtered_list = [year for year in list if not re.search(pattern, year[0])]           
    sorted_numbers = sorted(filtered_list, key=lambda x: x[1], reverse=True)
    highest = sorted_numbers[:10]
    return highest

def lowest_by_quarter():
    data = read_table(table_name)
    list = [row for row in data]
    pattern = r'2020|2021'
    filtered_list = [year for year in list if not re.search(pattern, year[0])]           
    sorted_numbers = sorted(filtered_list, key=lambda x: x[1])
    lowest = sorted_numbers[:10]
    return lowest