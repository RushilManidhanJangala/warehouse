import os
import boto3

# Read credentials from environment variables
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.getenv("AWS_REGION")
BUCKET_NAME = os.getenv("S3_BUCKET_NAME")

# Create S3 client
s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION
)


def upload_files():

    files = [
        "/opt/airflow/project/data/processed/dim_customer.csv",
        "/opt/airflow/project/data/processed/dim_product.csv",
        "/opt/airflow/project/data/processed/dim_seller.csv",
        "/opt/airflow/project/data/processed/dim_date.csv",
        "/opt/airflow/project/data/processed/fact_orders.csv"
    ]

    for file in files:

        object_name = os.path.basename(file)

        s3.upload_file(
            file,
            BUCKET_NAME,
            object_name
        )

        print(f"Uploaded {object_name}")

    print("Upload complete.")


if __name__ == "__main__":
    upload_files()