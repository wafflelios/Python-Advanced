SELECT customer.full_name, customer.customer_id
FROM customer
LEFT JOIN "order" ON "order".customer_id = customer.customer_id
WHERE "order".order_no IS NULL;
