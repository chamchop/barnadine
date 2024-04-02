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

def top_five_years_by_quarter(list):    
    pattern = r'2020|2021'
    filtered_list = [year for year in list if not re.search(pattern, year[0])]           
    sorted_numbers = sorted(filtered_list, key=lambda x: x[1], reverse=True)
    top_five = sorted_numbers[:5]
    return top_five

if __name__ == '__main__':
    data = read_table(table_name)         
    top = top_five_years_by_quarter([row for row in data])
    for index, number in top:
        print(f'index: {index}, number: {number}')