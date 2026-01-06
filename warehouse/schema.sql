-- Dimension table: Customers
CREATE TABLE dim_customers (
    customer_id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    country TEXT,
    customer_region TEXT
);

-- Fact table: Orders
CREATE TABLE fact_orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    order_date DATE,
    total_amount DECIMAL(10, 2),
    FOREIGN KEY (customer_id) REFERENCES dim_customers(customer_id)
);
