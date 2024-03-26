import psycopg2
from config import load_config

def get_names():
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT test_id, test_name FROM test ORDER BY test_name")
                rows = cur.fetchall()

                for row in rows:
                    print(row)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

if __name__ == '__main__':
    get_names()