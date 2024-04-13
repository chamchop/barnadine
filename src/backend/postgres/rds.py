import psycopg2

db_config = {
    'dbname': 'ons_gdp',
    'user': 'barnardine_dev',
    'password': 'madmalvolio',
    'host': 'barnardine.cbc0qyow6ikm.eu-west-2.rds.amazonaws.com', 
    'port': 5432
}

try:
    conn = psycopg2.connect(
        dbname=db_config['dbname'],
        user=db_config['user'],
        password=db_config['password'],
        host=db_config['host'],
        port=db_config['port']
    )
    print("Connected to the database.")
    
    cursor = conn.cursor()

    cursor.execute("SELECT version();")

    db_version = cursor.fetchone()
    print("Database Version:", db_version)

except psycopg2.Error as e:
    print("Unable to connect to the database")
    print(e)
finally:
    if 'conn' in locals() and conn is not None:
        conn.close()
        print("Database connection closed.")
