import pandas as pd
from sqlalchemy import create_engine

# Replace with your password
PASSWORD = "postgres"

engine = create_engine(
    f"postgresql+psycopg2://postgres:{PASSWORD}@localhost:5432/warehouse_db"
)

print("\n===== TOTAL REVENUE =====")

query1 = """
SELECT
    ROUND(SUM(price)::numeric, 2) AS total_revenue
FROM fact_orders;
"""

print(pd.read_sql(query1, engine))

print("\n===== TOTAL ORDERS =====")

query2 = """
SELECT
    COUNT(DISTINCT order_id) AS total_orders
FROM fact_orders;
"""

print(pd.read_sql(query2, engine))

print("\n===== TOP 10 SELLERS =====")

query3 = """
SELECT
    seller_id,
    ROUND(SUM(price)::numeric, 2) AS revenue
FROM fact_orders
GROUP BY seller_id
ORDER BY revenue DESC
LIMIT 10;
"""

print(pd.read_sql(query3, engine))