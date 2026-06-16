import pandas as pd


def extract_data():

    customers = pd.read_csv(
        "data/raw/olist_customers_dataset.csv"
    )

    orders = pd.read_csv(
        "data/raw/olist_orders_dataset.csv"
    )

    order_items = pd.read_csv(
        "data/raw/olist_order_items_dataset.csv"
    )

    products = pd.read_csv(
        "data/raw/olist_products_dataset.csv"
    )

    sellers = pd.read_csv(
        "data/raw/olist_sellers_dataset.csv"
    )

    payments = pd.read_csv(
        "data/raw/olist_order_payments_dataset.csv"
    )

    reviews = pd.read_csv(
        "data/raw/olist_order_reviews_dataset.csv"
    )

    return {
        "customers": customers,
        "orders": orders,
        "order_items": order_items,
        "products": products,
        "sellers": sellers,
        "payments": payments,
        "reviews": reviews
    }


if __name__ == "__main__":

    data = extract_data()

    for name, df in data.items():
        print(f"{name}: {df.shape}")