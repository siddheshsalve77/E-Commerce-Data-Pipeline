import boto3
import os
import glob

def upload_files():
    # Initialize S3
    s3_client = boto3.client('s3', region_name='ap-south-1')
    bucket_name = 'ecommerce-data-pipeline-siddhesh'
    
    # Local path
    local_raw_path = 'raw_data/'
    s3_target_path = 'raw/olist_data/'

    # Get all CSV files
    files = glob.glob(os.path.join(local_raw_path, '*.csv'))

    if not files:
        print("No CSV files found in raw_data folder!")
        return

    print(f"Found {len(files)} files to upload...")

    for file_path in files:
        file_name = os.path.basename(file_path)
        s3_key = s3_target_path + file_name
        
        try:
            print(f"Uploading {file_name} to S3...")
            s3_client.upload_file(file_path, bucket_name, s3_key)
        except Exception as e:
            print(f"Error uploading {file_name}: {e}")

    print("\nAll files uploaded successfully!")

if __name__ == "__main__":
    upload_files()