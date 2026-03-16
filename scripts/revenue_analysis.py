import psycopg2
import pandas as pd

def analyze_revenue():
    db_host = 'ecommerce-db.c3wo00cgqlaj.ap-southeast-1.rds.amazonaws.com'
    db_name = 'postgres'
    db_user = 'postgres'
    db_password = 'sidd1234'

    conn = None
    try:
        print("Connecting to Database for Revenue Analysis...")
        conn = psycopg2.connect(
            host=db_host,
            database=db_name,
            user=db_user,
            password=db_password
        )
        
        # 1. Total Revenue
        print("\n--- Total Revenue ---")
        query_revenue = """
        SELECT 
            COUNT(*) as total_transactions,
            SUM(total_revenue) as total_revenue,
            AVG(total_revenue) as avg_order_value
        FROM fact_sales;
        """
        df_rev = pd.read_sql(query_revenue, conn)
        print(df_rev)

        # 2. Monthly Revenue Trend
        print("\n--- Monthly Revenue Trend (First 5 Months) ---")
        query_trend = """
        SELECT 
            TO_CHAR(order_purchase_timestamp, 'YYYY-MM') as month,
            SUM(total_revenue) as monthly_revenue
        FROM fact_sales
        GROUP BY 1
        ORDER BY 1 ASC
        LIMIT 5;
        """
        df_trend = pd.read_sql(query_trend, conn)
        print(df_trend)

        # 3. Top 5 Products by Revenue
        print("\n--- Top 5 Products by Revenue ---")
        query_top_products = """
        SELECT 
            p.product_category_name,
            SUM(f.total_revenue) as category_revenue
        FROM fact_sales f
        JOIN dim_product p ON f.product_id = p.product_id
        GROUP BY p.product_category_name
        ORDER BY category_revenue DESC
        LIMIT 5;
        """
        df_top = pd.read_sql(query_top_products, conn)
        print(df_top)

        print("\nAnalysis Complete.")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        if conn is not None:
            conn.close()

if __name__ == "__main__":
    analyze_revenue()