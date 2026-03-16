import psycopg2

def fix_constraints():
    db_host = 'ecommerce-db.c3wo00cgqlaj.ap-southeast-1.rds.amazonaws.com'
    db_name = 'postgres'
    db_user = 'postgres'
    db_password = 'sidd1234'

    conn = None
    try:
        print("Connecting to fix constraints...")
        conn = psycopg2.connect(
            host=db_host,
            database=db_name,
            user=db_user,
            password=db_password
        )
        cur = conn.cursor()
        
        # Add unique constraint to customer_id
        print("Adding unique constraint to dim_customer...")
        cur.execute("ALTER TABLE dim_customer ADD CONSTRAINT cust_id_unique UNIQUE (customer_id);")
        
        conn.commit()
        cur.close()
        print("Constraint added successfully!")

    except Exception as e:
        print(f"Error (or constraint might already exist): {e}")
    finally:
        if conn is not None:
            conn.close()

if __name__ == "__main__":
    fix_constraints()