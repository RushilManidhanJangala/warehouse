import pandas as pd
from sqlalchemy import create_engine

PASSWORD = "airflow"

engine = create_engine(
    f"postgresql+psycopg2://airflow:{PASSWORD}@postgres/airflow"
)


def load_tables():

    dim_customer = pd.read_csv(
        "/opt/airflow/project/data/processed/dim_customer.csv"
    )

    dim_product = pd.read_csv(
        "/opt/airflow/project/data/processed/dim_product.csv"
    )

    dim_seller = pd.read_csv(
        "/opt/airflow/project/data/processed/dim_seller.csv"
    )

    dim_date = pd.read_csv(
        "/opt/airflow/project/data/processed/dim_date.csv"
    )

    fact_orders = pd.read_csv(
        "/opt/airflow/project/data/processed/fact_orders.csv"
    )

    dim_customer.to_sql(
        "dim_customer",
        engine,
        if_exists="replace",
        index=False
    )

    dim_product.to_sql(
        "dim_product",
        engine,
        if_exists="replace",
        index=False
    )

    dim_seller.to_sql(
        "dim_seller",
        engine,
        if_exists="replace",
        index=False
    )

    dim_date.to_sql(
        "dim_date",
        engine,
        if_exists="replace",
        index=False
    )

    fact_orders.to_sql(
        "fact_orders",
        engine,
        if_exists="replace",
        index=False
    )

    print("Warehouse tables loaded successfully.")


if __name__ == "__main__":
    load_tables()