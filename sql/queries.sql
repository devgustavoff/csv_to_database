-- TOP 10 PRODUTOS MAIS VENDIDOS
SELECT 
    order_items.product_id, 
    SUM(order_items.price) AS total_sales
FROM order_items
GROUP BY order_items.product_id
ORDER BY total_sales DESC
LIMIT 10;

-- RECEITA POR MÊS
SELECT
    EXTRACT(YEAR FROM orders.order_purchase_timestamp) AS year,
    EXTRACT(MONTH FROM orders.order_purchase_timestamp) AS month, 
    SUM(order_items.price) AS total_month_revenue
FROM orders
JOIN order_items ON orders.order_id = order_items.order_id
GROUP BY year, month
ORDER BY year, month;

-- ESTADOS COM MAIS PEDIDOS
SELECT
    customers.customer_state,
    COUNT(orders.order_id) AS orders_total
FROM customers
JOIN orders ON customers.customer_id = orders.customer_id
GROUP BY customers.customer_state
ORDER BY orders_total DESC;

-- TICKET MEDIO POR CATEGORIA
SELECT
    products.product_category_name,
    AVG(order_items.price) AS avg_ticket
FROM products
JOIN order_items ON products.product_id = order_items.product_id
GROUP BY products.product_category_name
ORDER BY avg_ticket DESC;

-- TAXA DE PEDIDOS ATRASADOS
SELECT 
    (COUNT(*) FILTER(WHERE orders.order_delivered_customer_date > orders.order_estimated_delivery_date)::DECIMAL 
    / COUNT(*)) * 100 AS late_order_rate
FROM orders;