import psycopg2
import os

def create_tables():
    # Database Connection Parameters
    db_host = 'ecommerce-db.c3wo00cgqlaj.ap-southeast-1.rds.amazonaws.com'
    db_name = 'postgres' # Default DB name for RDS
    db_user = 'postgres'
    db_password = 'sidd1234' # The password you set earlier

    # Read SQL file
    sql_file_path = 'sql_queries/create_tables.sql'
    
    if not os.path.exists(sql_file_path):
        print(f"Error: {sql_file_path} not found.")
        return

    with open(sql_file_path, 'r') as file:
        sql_script = file.read()

    conn = None
    try:
        print("Connecting to RDS PostgreSQL...")
        conn = psycopg2.connect(
            host=db_host,
            database=db_name,
            user=db_user,
            password=db_password
        )
        
        cur = conn.cursor()
        print("Executing SQL script to create tables...")
        cur.execute(sql_script)
        
        conn.commit()
        cur.close()
        print("Tables created successfully!")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        if conn is not None:
            conn.close()

if __name__ == "__main__":
    create_tables()