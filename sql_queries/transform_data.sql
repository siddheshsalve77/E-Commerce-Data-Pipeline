-- 1. Populate Customer Dimension
INSERT INTO dim_customer (
    customer_id, 
    customer_unique_id, 
    customer_city, 
    customer_state, 
    customer_zip_code_prefix, 
    effective_date, 
    is_current
)
SELECT 
    customer_id,
    customer_unique_id,
    customer_city,
    customer_state,
    customer_zip_code_prefix,
    CURRENT_TIMESTAMP as effective_date,
    TRUE as is_current
FROM stg_customers
ON CONFLICT (customer_id) 
DO UPDATE SET 
    customer_city = EXCLUDED.customer_city,
    is_current = TRUE;

-- 2. Populate Product Dimension
INSERT INTO dim_product (
    product_id,
    product_category_name,
    product_weight_g,
    product_length_cm,
    product_height_cm,
    product_width_cm
)
SELECT 
    product_id,
    product_category_name,
    product_weight_g,
    product_length_cm,
    product_height_cm,
    product_width_cm
FROM stg_products
WHERE product_id IS NOT NULL;