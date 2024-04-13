import psycopg2
from config import load_config
config = load_config()

def update_record(table_name, id, input):
    sql = f'UPDATE {table_name} SET {id} = {input}'    
    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                cur.execute(sql)
            print(f'update {table_name} with {input}')
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def update_row(table_name, col_1, col_2, input_1, input_2):
    sql = f'INSERT INTO {table_name} ({col_1}, {col_2}) VALUES (%s, %s)'
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (input_1, input_2))
            print(f'update {table_name} with {input_1} and {input_2}')
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)