from db_setup import create_table
from extractor import fetch_bitcoin_data
from transformer import transform_bitcoin_data
from loader import load_bitcoin_data

def main():
    # Database Setup: Create the bitcoin_price table if it doesn't exist
    print("Setting up the database...")
    create_table()
    
    # Extraction: Fetch raw data from CoinGecko API
    print("Extracting data...")
    raw_data = fetch_bitcoin_data()
    
    # Transformation: Convert raw JSON to a structured format
    print("Transforming data...")
    transformed_data = transform_bitcoin_data(raw_data)
    
    # Loading: Insert the transformed data into the database.
    # Environment variables are loaded inside load_bitcoin_data().
    print("Loading data...")
    load_bitcoin_data(transformed_data)

if __name__ == '__main__':
    main()
