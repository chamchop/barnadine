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
                for row in rows:
                    print(row)

    except (Exception, psycopg2.DatabaseError) as error:
        conn.rollback()
        print(error)        