import psycopg2
from config import load_config

def insert_single(test_name):
    sql = """INSERT INTO test(test_name) VALUES(%s) RETURNING test_id;"""    
    test_id = None
    config = load_config()
    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                cur.execute(sql, (test_name,))
                rows = cur.fetchone()
                if rows:
                    test_id = rows[0]
                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)    
    finally:
        return test_id

def insert_many(test_name):
    sql = """INSERT INTO test(test_name) VALUES(%s) RETURNING *;"""
    config = load_config()
    rows = []
    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                cur.executemany(sql, test_name)
                rows = cur.fetchall()
                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)    
    finally:
        return rows
    
if __name__ == '__main__':
    insert_single(1)
    
    insert_many([
        (2,),
        (3,),
    ])