import os
import psycopg2
from dotenv import load_dotenv

def load_bitcoin_data(data):
    # Load environment variables from the .env file
    load_dotenv()
    
    # Retrieve database configuration from environment variables
    db_host = os.environ.get("DB_HOST", "localhost")
    db_port = os.environ.get("DB_PORT", "5432")
    db_name = os.environ.get("DB_NAME", "crypto_db")
    db_user = os.environ.get("DB_USER", "postgres")
    db_password = os.environ.get("DB_PASSWORD", "password")
    
    conn = None
    try:
        conn = psycopg2.connect(
            host=db_host,
            port=db_port,
            dbname=db_name,
            user=db_user,
            password=db_password
        )
        cursor = conn.cursor()
        insert_query = """
            INSERT INTO bitcoin_price (time_updated, usd_rate, code)
            VALUES (%s, %s, %s)
        """
        cursor.execute(insert_query, (
            data["time_updated"],
            data["usd_rate"],
            data["code"]
        ))
        conn.commit()
        cursor.close()
        print("Data loaded successfully.")
    except Exception as e:
        print("Error loading data:", e)
    finally:
        if conn:
            conn.close()
