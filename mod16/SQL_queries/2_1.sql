SELECT customer.full_name AS customer_name, manager.full_name AS manager_name, "order".purchase_amount as sum, "order".date
FROM "order"
JOIN customer ON "order".customer_id = customer.customer_id
LEFT JOIN manager ON "order".manager_id = manager.manager_id OR manager.manager_id IS NULL;
