import psycopg2
from config import load_config

def update_vendor(test_id, test_name):
    updated_row_count = 0
    sql = """ UPDATE test SET test_name = %s WHERE test_id = %s"""    
    config = load_config()
    
    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                cur.execute(sql, (test_id, test_name))
                updated_row_count = cur.rowcount
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)    
    finally:
        return updated_row_count

if __name__ == '__main__':
    update_vendor("statistics", 1)