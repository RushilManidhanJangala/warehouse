-- ==========================================
-- DIMENSION TABLES
-- ==========================================

DROP TABLE IF EXISTS fact_orders;

DROP TABLE IF EXISTS dim_customer;
DROP TABLE IF EXISTS dim_product;
DROP TABLE IF EXISTS dim_seller;
DROP TABLE IF EXISTS dim_date;


-- ==========================================
-- CUSTOMER DIMENSION
-- ==========================================

CREATE TABLE dim_customer (

    customer_id VARCHAR(50) PRIMARY KEY,

    customer_unique_id VARCHAR(50),

    customer_city VARCHAR(100),

    customer_state VARCHAR(10)

);


-- ==========================================
-- PRODUCT DIMENSION
-- ==========================================

CREATE TABLE dim_product (

    product_id VARCHAR(50) PRIMARY KEY,

    product_category_name VARCHAR(100),

    product_name_lenght INTEGER,

    product_description_lenght INTEGER,

    product_photos_qty INTEGER,

    product_weight_g NUMERIC,

    product_length_cm NUMERIC,

    product_height_cm NUMERIC,

    product_width_cm NUMERIC

);


-- ==========================================
-- SELLER DIMENSION
-- ==========================================

CREATE TABLE dim_seller (

    seller_id VARCHAR(50) PRIMARY KEY,

    seller_zip_code_prefix INTEGER,

    seller_city VARCHAR(100),

    seller_state VARCHAR(10)

);


-- ==========================================
-- DATE DIMENSION
-- ==========================================

CREATE TABLE dim_date (

    date DATE PRIMARY KEY,

    day INTEGER,

    month INTEGER,

    month_name VARCHAR(20),

    quarter INTEGER,

    year INTEGER,

    weekday VARCHAR(20)

);


-- ==========================================
-- FACT TABLE
-- ==========================================

CREATE TABLE fact_orders (

    order_id VARCHAR(50),

    order_item_id INTEGER,

    product_id VARCHAR(50),

    seller_id VARCHAR(50),

    shipping_limit_date TIMESTAMP,

    price NUMERIC(12,2),

    freight_value NUMERIC(12,2),

    customer_id VARCHAR(50),

    order_status VARCHAR(30),

    order_purchase_timestamp TIMESTAMP,

    order_approved_at TIMESTAMP,

    order_delivered_carrier_date TIMESTAMP,

    order_delivered_customer_date TIMESTAMP,

    order_estimated_delivery_date TIMESTAMP

);