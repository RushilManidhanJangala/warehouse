import pandas as pd
from sqlalchemy import create_engine

PASSWORD = "postgres"

engine = create_engine(
    f"postgresql+psycopg2://postgres:{PASSWORD}@localhost:5432/warehouse_db"
)

query = """
SELECT
    ROUND(SUM(price)::numeric, 2) AS total_revenue
FROM fact_orders;
"""

result = pd.read_sql(query, engine)

print(result)