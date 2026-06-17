import pandas as pd
from extract import extract_data


def build_dim_customer(customers):
    return customers.copy()


def build_dim_product(products):
    return products.copy()


def build_dim_seller(sellers):
    return sellers.copy()


def build_fact_orders(orders, order_items):
    fact_orders = order_items.merge(
        orders,
        on="order_id",
        how="left"
    )

    return fact_orders


def save_tables(
    dim_customer,
    dim_product,
    dim_seller,
    fact_orders
):

    dim_customer.to_csv(
        "/opt/airflow/project/data/processed/dim_customer.csv",
        index=False
    )

    dim_product.to_csv(
        "/opt/airflow/project/data/processed/dim_product.csv",
        index=False
    )

    dim_seller.to_csv(
        "/opt/airflow/project/data/processed/dim_seller.csv",
        index=False
    )

    fact_orders.to_csv(
        "/opt/airflow/project/data/processed/fact_orders.csv",
        index=False
    )


if __name__ == "__main__":

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

    print(
        "Customer Dimension:",
        dim_customer.shape
    )

    print(
        "Product Dimension:",
        dim_product.shape
    )

    print(
        "Seller Dimension:",
        dim_seller.shape
    )

    print(
        "Fact Orders:",
        fact_orders.shape
    )

    save_tables(
        dim_customer,
        dim_product,
        dim_seller,
        fact_orders
    )

    print("Processed tables saved.")