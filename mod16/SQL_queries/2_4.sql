SELECT customer.full_name as customer_name, "order".order_no
FROM "order"
JOIN customer ON "order".customer_id = customer.customer_id AND "order".manager_id is NULL;
