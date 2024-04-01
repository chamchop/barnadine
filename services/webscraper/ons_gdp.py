import pandas as pd
import requests

def get_ons_gdp():
    url = "https://www.ons.gov.uk/economy/grossdomesticproductgdp/timeseries/ihyq/qna"
    response = requests.get(url=url, headers={'User-Agent': 'Mozilla/5.0'})
    df = pd.read_html(response.content)
    table = df[1]
    data = table.loc[:, ['Period', 'Value']]
    print(data)
    return data

# import requests
# from bs4 import BeautifulSoup
# import psycopg2
# import pandas as pd
# import unittest
# import psycopg2
# import sys
# sys.path.insert(1, 'C://Programming//barnardine//backend//postgres')
# from postgres_create import *
# from postgres_read import *
# from postgres_update import *
# from postgres_delete import *
# from config import load_config
# config = load_config()

# table_name = 'test'
# col_1 = 'period'
# col_2 = 'value'

# def scrape_and_store():
#     url = "https://www.ons.gov.uk/economy/grossdomesticproductgdp/timeseries/ihyq/qna"
#     response = requests.get(url=url, headers={'User-Agent': 'Mozilla/5.0'})
#     tables = pd.read_html(response.content)
#     try:
#         if tables:
#             table = tables[1] 
#             create_table(table_name, col_1, col_2)
#             for row in table.iterrows():
#                 period = row[0]
#                 value = row[1]
#                 update_row(table_name, col_1, col_2, period, value)
#             print("Data scraped and stored successfully.")
#         else:
#             print("No tables found on the webpage.")
#     except Exception as e:
#         print("Error occurred while scraping:", e)

# # if __name__ == '__main__':
# #     scrape_and_store()
# #     data = read_table(table_name)
# #     if data:
# #         print("All data from the table:")
# #         for row in data:
# #             print(row)
# #     else:
# #         print("Failed to read data from the table.")

# if __name__ == '__main__':
#     delete_table(table_name)        

# # def create_table():
# #     conn = psycopg2.connect(
# #         dbname="postgres",
# #         user="postgres",
# #         password="Gl@sgow098!",
# #         host="localhost",
# #     )

# #     cursor = conn.cursor()
# #     create_table_query = """
# #         CREATE TABLE IF NOT EXISTS gdp_data (
# #             period VARCHAR(50),
# #             value NUMERIC
# #         );
# #     """
# #     cursor.execute(create_table_query)
# #     conn.commit()
# #     conn.close()        
        
# # def read_all_data():
# #     try:
# #         conn = psycopg2.connect(
# #             dbname="postgres",
# #             user="postgres",
# #             password="Gl@sgow098!",
# #             host="localhost",
# #         )
# #         cursor = conn.cursor()
# #         select_query = "SELECT * FROM gdp_data;"
# #         cursor.execute(select_query)
# #         rows = cursor.fetchall()
# #         conn.close()
# #         return rows
# #     except Exception as e:
# #         print("Error occurred while reading data:", e)
# #         return None        
        
# # def insert_data(period, value):
# #     conn = psycopg2.connect(
# #         dbname="postgres",
# #         user="postgres",
# #         password="Gl@sgow098!",
# #         host="localhost",
# #     )
# #     cursor = conn.cursor()
# #     insert_query = "INSERT INTO gdp_data (period, value) VALUES (%s, %s);"
# #     cursor.execute(insert_query, (period, value))
# #     conn.commit()
# #     conn.close()        