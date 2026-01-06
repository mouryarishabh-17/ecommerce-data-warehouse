-- ===============================
-- PROJECT 1: E-Commerce Analytics
-- ===============================

-- KPI 1: Total Revenue

SELECT SUM(total_amount) AS total_revenue
FROM fact_orders;

-- KPI 2: Top 10 Customers by Revenue

SELECT
    c.customer_id,
    SUM(o.total_amount) AS customer_revenue
FROM fact_orders o
JOIN dim_customers c
    ON o.customer_id = c.customer_id
GROUP BY c.customer_id
ORDER BY customer_revenue DESC
LIMIT 10;

-- KPI 3: Revenue by Country

SELECT
    c.country,
    SUM(o.total_amount) AS revenue
FROM fact_orders o
JOIN dim_customers c
    ON o.customer_id = c.customer_id
GROUP BY c.country
ORDER BY revenue DESC;

-- KPI 4: Average Order Value (AOV)

SELECT
    AVG(total_amount) AS average_order_value
FROM fact_orders;

-- KPI 5: Orders Trend Over Time (Daily)

SELECT
    order_date,
    COUNT(*) AS total_orders
FROM fact_orders
GROUP BY order_date
ORDER BY order_date;
