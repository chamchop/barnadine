import requests
from bs4 import BeautifulSoup
import psycopg2
import pandas as pd
import psycopg2

table_name = 'gdp_data'
col_1 = 'period'
col_2 = 'value'

def create_table(table_name, col_1, col_2):
    sql = f'CREATE TABLE IF NOT EXISTS {table_name} (id SERIAL PRIMARY KEY, {col_1} VARCHAR(255), {col_2} VARCHAR(255))'
    try:
        with psycopg2.connect(
            dbname="ons_gdp",
            user="barnardine_dev",
            password="madmalvolio",
            host="barnardine.cbc0qyow6ikm.eu-west-2.rds.amazonaws.com",
            port=5432) as conn:
            with conn.cursor() as cur:
                cur.execute(sql)
            conn.commit()
            print(f"created table {table_name}")
    except (psycopg2.DatabaseError, Exception) as error:
        conn.rollback()
        print(error)

def update_row(table_name, col_1, col_2, input_1, input_2):
    sql = f'INSERT INTO {table_name} ({col_1}, {col_2}) VALUES (%s, %s)'
    try:
        with psycopg2.connect(
            dbname="ons_gdp",
            user="barnardine_dev",
            password="madmalvolio",
            host="barnardine.cbc0qyow6ikm.eu-west-2.rds.amazonaws.com",
            port=5432) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (input_1, input_2))
            print(f'update {table_name} with {input_1} and {input_2}')
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def scrape_and_store():
    url = "https://www.ons.gov.uk/economy/grossdomesticproductgdp/timeseries/ihyq/qna"
    response = requests.get(url=url, headers={'User-Agent': 'Mozilla/5.0'})
    tables = pd.read_html(response.content)
    try:
        if tables:
            table = tables[1]
            create_table(table_name, col_1, col_2)
            for index, row in table.iterrows():
                period = row[0]
                value = row[1]
                update_row(table_name, col_1, col_2, period, value)
            print("Data scraped and stored successfully.")
        else:
            print("No tables found on the webpage.")
    except Exception as e:
        print("Error occurred while scraping:", e)

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
        select_query = "SELECT * FROM gdp_data;"
        cursor.execute(select_query)
        rows = cursor.fetchall()
        conn.close()
        return rows
    except Exception as e:
        print("Error occurred while reading data:", e)
        return None

# if __name__ == '__main__':    
#     scrape_and_store()
#     data = read_all_data()
#     if data:
#         print("All data from the table:")
#         for row in data:
#             print(row)
#     else:
#         print("Failed to read data from the table.")