import psycopg2
from config import load_config
config = load_config()

def read_table(table_name):
    sql = f'SELECT * FROM {table_name}'
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql)
                rows = cur.fetchall()
                return rows

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def read_record(table_name, id):
    sql = f'SELECT * FROM {table_name} WHERE id = {id}'
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:                
                cur.execute(sql, (id,))
                record = cur.fetchone()
                return record
    except Exception as e:
        print("Error occurred while reading data:", e)
        return None 