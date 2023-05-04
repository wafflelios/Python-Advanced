SELECT "order".order_no, manager.fulL_name as manager_name, customer.full_name as customer_name
FROM "order"
JOIN customer ON "order".customer_id = customer.customer_id
JOIN manager ON "order".manager_id = manager.manager_id
WHERE customer.city != manager.city;
