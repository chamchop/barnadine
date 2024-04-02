import sys
import re
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

def highest_by_quarter(list):    
    pattern = r'2020|2021'
    filtered_list = [year for year in list if not re.search(pattern, year[0])]           
    sorted_numbers = sorted(filtered_list, key=lambda x: x[1], reverse=True)
    highest = sorted_numbers[:10]
    return highest

def lowest_by_quarter(list):    
    pattern = r'2020|2021'
    filtered_list = [year for year in list if not re.search(pattern, year[0])]           
    sorted_numbers = sorted(filtered_list, key=lambda x: x[1])
    lowest = sorted_numbers[:10]
    return lowest

if __name__ == '__main__':
    data = read_table(table_name)         
    highest = highest_by_quarter([row for row in data])
    lowest = lowest_by_quarter([row for row in data])
    print('highest:')
    for index, number in highest:
        print(f'index: {index}, number: {number}')
    print('lowest:')
    for index, number in lowest:
        print(f'index: {index}, number: {number}')        