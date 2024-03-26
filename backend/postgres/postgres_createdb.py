import psycopg2
from crud.config import load_config

def create_tables():
    commands = ( 
        """CREATE TABLE test (test_id SERIAL PRIMARY KEY, test_name VARCHAR(255) NOT NULL)""",
        """CREATE TABLE test2 (test_id SERIAL PRIMARY KEY, test_name VARCHAR(255) NOT NULL)""")
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                for command in commands:
                    cur.execute(command)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == '__main__':
    create_tables()