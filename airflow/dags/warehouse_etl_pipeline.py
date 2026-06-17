from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="warehouse_etl_pipeline",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False,
) as dag:

    build_warehouse = BashOperator(
        task_id="build_warehouse",
        bash_command="echo Building warehouse"
    )

    load_postgres = BashOperator(
        task_id="load_postgres",
        bash_command="echo Loading PostgreSQL"
    )

    upload_s3 = BashOperator(
        task_id="upload_s3",
        bash_command="echo Uploading to S3"
    )

    build_warehouse >> load_postgres >> upload_s3