import boto3
import os

# Replace with YOUR values
AWS_ACCESS_KEY_ID = "YOUR_ACCESS_KEY"
AWS_SECRET_ACCESS_KEY = "YOUR_SECRET_KEY"

BUCKET_NAME = "rushil-warehouse-project-2026"

s3 = boto3.client(
    "s3",
    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
    region_name="us-east-2"
)

files = [
    "data/processed/dim_customer.csv",
    "data/processed/dim_product.csv",
    "data/processed/dim_seller.csv",
    "data/processed/dim_date.csv",
    "data/processed/fact_orders.csv"
]

for file in files:

    object_name = file.split("/")[-1]

    s3.upload_file(
        file,
        BUCKET_NAME,
        object_name
    )

    print(f"Uploaded {object_name}")

print("Upload complete.")