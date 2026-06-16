import pandas as pd


def build_dim_customer(customers):
    return customers.copy()


def build_dim_product(products):
    return products.copy()


def build_dim_seller(sellers):
    return sellers.copy()


def build_fact_orders(
    orders,
    order_items
):
    fact_orders = order_items.merge(
        orders,
        on="order_id",
        how="left"
    )

    return fact_orders
from extract import extract_data


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