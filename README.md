# End-to-End ETL & Data Warehouse System

## Overview

This project demonstrates the design and implementation of a modern data warehouse pipeline using Python, PostgreSQL, and AWS S3. The pipeline ingests raw e-commerce data, transforms it into a dimensional warehouse model, loads it into PostgreSQL, and generates business insights through SQL analytics.

## Architecture

Raw Olist Dataset
↓
Python ETL Pipeline
↓
Dimension & Fact Tables
↓
PostgreSQL Data Warehouse
↓
Analytics Layer
↓
AWS S3 Cloud Storage

## Tech Stack

* Python
* Pandas
* PostgreSQL
* SQLAlchemy
* AWS S3
* Boto3
* Git & GitHub

## Dataset

Brazilian E-Commerce Public Dataset by Olist

## Data Warehouse Schema

### Dimension Tables

* dim_customer
* dim_product
* dim_seller
* dim_date

### Fact Table

* fact_orders

## Key Features

* Built ETL workflows to clean and transform raw e-commerce data
* Designed a dimensional warehouse schema using fact and dimension tables
* Loaded warehouse tables into PostgreSQL for analytical workloads
* Developed SQL-based business analytics and reporting queries
* Integrated AWS S3 for cloud-based storage of processed warehouse outputs

## Sample Analytics

* Total Revenue Analysis
* Order Volume Analysis
* Top Seller Performance
* Product Category Insights

## Project Structure

warehouse/

├── analytics/

├── aws/

├── data/

├── etl/

├── notebooks/

├── sql/

├── docs/

└── README.md

## Future Enhancements

* Apache Airflow workflow orchestration
* Power BI dashboard integration
* Amazon Redshift data warehouse deployment
* Automated cloud-based ETL scheduling

## Project Status

Active Development
