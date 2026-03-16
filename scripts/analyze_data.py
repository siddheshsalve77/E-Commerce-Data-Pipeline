import psycopg2
import pandas as pd

def analyze_data():
    db_host = 'ecommerce-db.c3wo00cgqlaj.ap-southeast-1.rds.amazonaws.com'
    db_name = 'postgres'
    db_user = 'postgres'
    db_password = 'sidd1234'

    conn = None
    try:
        print("Connecting to Database for Analysis...")
        conn = psycopg2.connect(
            host=db_host,
            database=db_name,
            user=db_user,
            password=db_password
        )
        
        # 1. Verify Counts
        print("\n--- Verification Counts ---")
        query_counts = """
        SELECT 
            (SELECT COUNT(*) FROM dim_customer) as total_customers,
            (SELECT COUNT(*) FROM dim_product) as total_products;
        """
        df_counts = pd.read_sql(query_counts, conn)
        print(df_counts)

        # 2. Top 5 States by Customers
        print("\n--- Top 5 States by Customer Count ---")
        query_states = """
        SELECT customer_state, COUNT(*) as customer_count
        FROM dim_customer
        GROUP BY customer_state
        ORDER BY customer_count DESC
        LIMIT 5;
        """
        df_states = pd.read_sql(query_states, conn)
        print(df_states)

        print("\nAnalysis Complete.")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        if conn is not None:
            conn.close()

if __name__ == "__main__":
    analyze_data()