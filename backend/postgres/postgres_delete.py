import psycopg2
from config import load_config

def delete(input):
    rows_deleted  = 0
    sql = 'DELETE FROM test WHERE test_id = %s'
    config = load_config()

    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                cur.execute(sql, (input,))
                rows_deleted = cur.rowcount

            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)    
    finally:
        return rows_deleted

def delete_all():
    sql = """DELETE FROM test WHERE test_id = 1;"""
    config = load_config()

    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                cur.execute(sql)

            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error) 


if __name__ == '__main__':
    # deleted_rows = delete(1)
    # print('The number of deleted rows: ', deleted_rows)
    delete_all()