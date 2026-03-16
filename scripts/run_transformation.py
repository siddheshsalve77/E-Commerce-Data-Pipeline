import psycopg2
import os

def run_transformation():
    # Database Connection
    db_host = 'ecommerce-db.c3wo00cgqlaj.ap-southeast-1.rds.amazonaws.com'
    db_name = 'postgres'
    db_user = 'postgres'
    db_password = 'sidd1234'

    sql_file_path = 'sql_queries/transform_orders.sql'

    with open(sql_file_path, 'r') as file:
        sql_script = file.read()

    conn = None
    try:
        print("Connecting to Database for Transformation...")
        conn = psycopg2.connect(
            host=db_host,
            database=db_name,
            user=db_user,
            password=db_password
        )
        
        cur = conn.cursor()
        print("Executing Transformation SQL...")
        cur.execute(sql_script)
        
        conn.commit()
        cur.close()
        print("Transformation complete! Dimensions updated.")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        if conn is not None:
            conn.close()

if __name__ == "__main__":
    run_transformation()