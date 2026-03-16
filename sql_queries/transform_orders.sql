-- Transform Orders and Items into Fact_Sales
INSERT INTO fact_sales (
    order_id, 
    customer_id, 
    product_id, 
    order_purchase_timestamp, 
    order_status, 
    quantity, 
    price, 
    freight_value, 
    total_revenue
)
SELECT 
    o.order_id,
    o.customer_id,
    oi.product_id,
    -- Cast text to timestamp
    o.order_purchase_timestamp::TIMESTAMP, 
    o.order_status,
    oi.order_item_id as quantity,
    oi.price,
    oi.freight_value,
    (oi.price + oi.freight_value) as total_revenue
FROM stg_orders o
JOIN stg_order_items oi ON o.order_id = oi.order_id;