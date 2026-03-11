CREATE TABLE customers (
    customer_id VARCHAR PRIMARY KEY,
    customer_unique_id VARCHAR,
    customer_zip_code_prefix INT,
    customer_city VARCHAR,
    customer_state VARCHAR
);

CREATE TABLE order_items (
    order_id VARCHAR,
    order_item_id INT,
    product_id VARCHAR,
    seller_id VARCHAR,
    shipping_limit_date TIMESTAMP,
    price REAL,
    freight_value REAL,
    PRIMARY KEY (order_id, order_item_id)
);

CREATE TABLE orders (
    order_id VARCHAR PRIMARY KEY,
    customer_id VARCHAR,
    order_status VARCHAR,
    order_purchase_timestamp TIMESTAMP,
    order_approved_at TIMESTAMP,
    order_delivered_carrier_date TIMESTAMP,
    order_delivered_customer_date TIMESTAMP,
    order_estimated_delivery_date TIMESTAMP
);

CREATE TABLE products (
    product_id VARCHAR PRIMARY KEY,
    product_category_name VARCHAR,
    product_name_lenght REAL,
    product_description_lenght REAL,
    product_photos_qty REAL,
    product_weight_g REAL,
    product_lenght_cm REAL,
    product_height_cm REAL,
    product_width_cm REAL
);