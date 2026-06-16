from extract import extract_data
from transform import (
    build_dim_customer,
    build_dim_product,
    build_dim_seller,
    build_fact_orders,
    save_tables
)

from date_dimension import create_date_dimension


def build_warehouse():

    data = extract_data()

    dim_customer = build_dim_customer(
        data["customers"]
    )

    dim_product = build_dim_product(
        data["products"]
    )

    dim_seller = build_dim_seller(
        data["sellers"]
    )

    fact_orders = build_fact_orders(
        data["orders"],
        data["order_items"]
    )

    dim_date = create_date_dimension(
        "2016-01-01",
        "2018-12-31"
    )

    save_tables(
        dim_customer,
        dim_product,
        dim_seller,
        fact_orders
    )

    dim_date.to_csv(
        "data/processed/dim_date.csv",
        index=False
    )

    print("Warehouse build complete")


if __name__ == "__main__":
    build_warehouse()