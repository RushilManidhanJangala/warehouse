# Data Warehouse Design

## Objective

Build a cloud-based data warehouse to support sales, customer, product, and seller analytics using the Olist E-Commerce dataset.

## Fact Table

### fact_orders

| Column                   |
| ------------------------ |
| order_id                 |
| customer_id              |
| product_id               |
| seller_id                |
| order_purchase_timestamp |
| price                    |
| freight_value            |

## Dimension Tables

### dim_customer

| Column             |
| ------------------ |
| customer_id        |
| customer_unique_id |
| customer_city      |
| customer_state     |

### dim_product

| Column                |
| --------------------- |
| product_id            |
| product_category_name |

### dim_seller

| Column       |
| ------------ |
| seller_id    |
| seller_city  |
| seller_state |

### dim_date

| Column  |
| ------- |
| date    |
| day     |
| month   |
| quarter |
| year    |
| weekday |
