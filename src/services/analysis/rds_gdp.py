import re
import psycopg2

table_name = 'gdp_data'
col_1 = 'period'
col_2 = 'value'

def read_all_data():
    try:
        conn = psycopg2.connect(
            dbname="ons_gdp",
            user="barnardine_dev",
            password="madmalvolio",
            host="barnardine.cbc0qyow6ikm.eu-west-2.rds.amazonaws.com",
            port=5432
        )
        cursor = conn.cursor()
        select_query = "SELECT period, value FROM gdp_data;"
        cursor.execute(select_query)
        rows = cursor.fetchall()
        conn.close()
        return rows
    except Exception as e:
        print("Error occurred while reading data:", e)
        return None

def highest_by_quarter():
    data = read_all_data()
    list = [row for row in data]
    pattern = r'2020|2021'
    filtered_list = [year for year in list if not re.search(pattern, year[0])]           
    sorted_numbers = sorted(filtered_list, key=lambda x: x[1], reverse=True)
    highest = sorted_numbers[:10]
    return highest

def lowest_by_quarter():
    data = read_all_data()
    list = [row for row in data]
    pattern = r'2020|2021'
    filtered_list = [year for year in list if not re.search(pattern, year[0])]           
    sorted_numbers = sorted(filtered_list, key=lambda x: x[1])
    lowest = sorted_numbers[:10]
    return lowest

if __name__ == '__main__':
    data = read_all_data()
    for rows in data:
        print(rows)