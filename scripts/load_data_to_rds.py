import pandas as pd
from sqlalchemy import create_engine
import os

def load_data():
    # Database Connection
    db_user = 'postgres'
    db_password = 'sidd1234'
    db_host = 'ecommerce-db.c3wo00cgqlaj.ap-southeast-1.rds.amazonaws.com'
    db_name = 'postgres'
    
    # Create connection string
    conn_str = f'postgresql+psycopg2://{db_user}:{db_password}@{db_host}/{db_name}'
    db_engine = create_engine(conn_str)

    print("Connected to Database.")

    # Files to load (mapping CSV to Table Names)
        # Files to load (mapping CSV to Table Names)
    files_to_load = [
        {'file': 'olist_customers_dataset.csv', 'table': 'stg_customers'},
        {'file': 'olist_products_dataset.csv', 'table': 'stg_products'},
        {'file': 'olist_orders_dataset.csv', 'table': 'stg_orders'},            # NEW
        {'file': 'olist_order_items_dataset.csv', 'table': 'stg_order_items'}    # NEW
    ]

    raw_data_path = 'raw_data/'

    for item in files_to_load:
        file_path = os.path.join(raw_data_path, item['file'])
        
        if os.path.exists(file_path):
            print(f"Loading {item['file']} into {item['table']}...")
            
            # Read CSV
            df = pd.read_csv(file_path)
            
            # Load to SQL (replace if exists)
            df.to_sql(item['table'], db_engine, if_exists='replace', index=False)
            print(f"Loaded {len(df)} rows into {item['table']}.")
        else:
            print(f"File not found: {file_path}")

    print("\nData loading complete!")

if __name__ == "__main__":
    load_data()