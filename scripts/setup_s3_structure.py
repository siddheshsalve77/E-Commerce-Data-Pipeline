import boto3

def create_s3_structure():
    # Initialize S3 Client with EXPLICIT region
    s3_client = boto3.client(
        's3',
        region_name='ap-south-1'
    )
    bucket_name = 'ecommerce-data-pipeline-siddhesh'

    folders = [
        'raw/olist_data/',
        'staging/cleaned_data/',
        'processed/analytics_ready/',
        'scripts/spark_jobs/'
    ]

    print(f"Connecting to bucket: {bucket_name} in region ap-south-1...")

    for folder in folders:
        try:
            s3_client.put_object(Bucket=bucket_name, Key=folder)
            print(f"Created folder: {folder}")
        except Exception as e:
            print(f"Error creating {folder}: {e}")

    print("\nDone.")

if __name__ == "__main__":
    create_s3_structure()