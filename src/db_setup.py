import os
import psycopg2
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

def create_database():
    db_config = {
        "host": os.environ.get("DB_HOST", "localhost"),
        "port": os.environ.get("DB_PORT", "5432"),
        "dbname": os.environ.get("DB_NAME", "crypto_db"),
        "user": os.environ.get("DB_USER", "postgres"),
        "password": os.environ.get("DB_PASSWORD", "password")
    }
    
    conn = None
    try:
        # Connect to the default "postgres" database
        conn = psycopg2.connect(
            host=db_config["host"],
            port=db_config["port"],
            dbname="postgres",
            user=db_config["user"],
            password=db_config["password"]
        )
        conn.autocommit = True
        cursor = conn.cursor()
        
        # Check if the target database exists
        cursor.execute("SELECT 1 FROM pg_database WHERE datname = %s", (db_config["dbname"],))
        exists = cursor.fetchone()
        if not exists:
            cursor.execute(f"CREATE DATABASE {db_config['dbname']}")
            print(f"Database '{db_config['dbname']}' created successfully!")
        else:
            print(f"Database '{db_config['dbname']}' already exists.")
        
        cursor.close()
    except Exception as e:
        print("Error creating database:", e)
    finally:
        if conn:
            conn.close()

def create_table():
    # First, ensure the database exists
    create_database()
    
    db_config = {
        "host": os.environ.get("DB_HOST", "localhost"),
        "port": os.environ.get("DB_PORT", "5432"),
        "dbname": os.environ.get("DB_NAME", "crypto_db"),
        "user": os.environ.get("DB_USER", "postgres"),
        "password": os.environ.get("DB_PASSWORD", "password")
    }
    
    create_table_query = """
    CREATE TABLE IF NOT EXISTS bitcoin_price (
        id SERIAL PRIMARY KEY,
        time_updated TIMESTAMP,
        usd_rate REAL,
        code VARCHAR(10)
    );
    """
    
    conn = None
    try:
        conn = psycopg2.connect(
            host=db_config["host"],
            port=db_config["port"],
            dbname=db_config["dbname"],
            user=db_config["user"],
            password=db_config["password"]
        )
        cursor = conn.cursor()
        cursor.execute(create_table_query)
        conn.commit()
        print("Table 'bitcoin_price' created successfully!")
        cursor.close()
    except Exception as e:
        print("Error creating table:", e)
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    create_table()
