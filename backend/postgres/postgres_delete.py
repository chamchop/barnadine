import psycopg2
from config import load_config
config = load_config()

def delete_record(table_name, id):
    sql = f'DELETE FROM {table_name} WHERE id = {id}'
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql)
            conn.commit()
            print(f'deleted record {id} from {table_name}')
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def delete_all_records(table_name):
    sql = f'DELETE FROM {table_name}'
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql)
            conn.commit()
            print(f'deleted records from {table_name}')
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)             

def delete_table(input):
    sql = f'DROP TABLE {input}'
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql)
                print(f'deleted table {input}')
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        conn.rollback()
        print(error)