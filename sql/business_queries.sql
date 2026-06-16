SELECT
    ROUND(SUM(price), 2) AS total_revenue
FROM fact_orders;
SELECT
    seller_id,
    ROUND(SUM(price), 2) AS revenue
FROM fact_orders
GROUP BY seller_id
ORDER BY revenue DESC
LIMIT 10;
SELECT
    DATE_TRUNC('month', order_purchase_timestamp)
        AS month,
    ROUND(SUM(price), 2) AS revenue
FROM fact_orders
GROUP BY month
ORDER BY month;
