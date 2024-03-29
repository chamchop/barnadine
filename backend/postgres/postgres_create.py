import psycopg2
from config import load_config

def create_table(table_name, col_1, col_2):
    sql = f'CREATE TABLE {table_name} (id SERIAL PRIMARY KEY, {col_1} VARCHAR(255), {col_2} VARCHAR(255))'
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql)
            conn.commit()
            print(f"created table {table_name}")
    except (psycopg2.DatabaseError, Exception) as error:
        conn.rollback()
        print(error)