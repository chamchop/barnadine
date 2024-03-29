import sys
sys.path.insert(1, 'C://Programming//barnardine//backend//postgres')
from postgres_create import *
from postgres_read import *
from postgres_update import *
from postgres_delete import *

name = 'ons_gdp'
col_1 = 'period'
col_2 = 'value'

if __name__ == '__main__':
    # create_table(name, col_1, col_2)
    # update_row(name, col_1, col_2, 'today', '1')
    read_table(name)
    delete_record(name, 1)
    read_table(name)
    update_row(name, col_1, col_2, 'today', '1')
    read_table(name)
