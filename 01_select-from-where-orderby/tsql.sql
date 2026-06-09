-- Query 1
-- Purpose:
-- Retrieve all customer IDs and their corresponding order IDs.
SELECT
    O.customer_id,
    O.order_id
FROM orders AS O;


-- Query 2
-- Purpose:
-- Retrieve the estimated delivery year for orders
-- whose estimated delivery date is after January 1, 2017.
SELECT
    YEAR(O.order_estimated_delivery_date) AS estimated_delivery_year
FROM orders AS O
	WHERE O.order_estimated_delivery_date > '2017-01-01';
-- The result may contain duplicate years 
-- if the goal is to see unique years
SELECT DISTINCT
    YEAR(O.order_estimated_delivery_date) AS estimated_delivery_year
FROM orders AS O
	WHERE O.order_estimated_delivery_date > '2017-01-01';


-- Query 3
-- Purpose:
-- Retrieve customers located in specific cities
-- and sort the results by city name in descending order.
SELECT
    C.customer_id,
    C.customer_city
FROM customers AS C
	WHERE C.customer_city IN ('valinhos', 'sao paulo', 'mendonca')
ORDER BY C.customer_city DESC;
-- IN() is cleaner than mulitple OR conditions.


-- query 4 
-- Purpose:
-- Retrieve sellers whose ZIP code prefix is between
-- 2000 and 3000, ordered by seller ID.
SELECT
    S.seller_state,
    S.seller_city
FROM sellers AS S
	WHERE S.seller_zip_code_prefix BETWEEN 2000 AND 3000
ORDER BY S.seller_id ASC;
-- Since sorting is preformed by selller_id, it can be displayed or not
SELECT
    S.seller_id,
    S.seller_state,
    S.seller_city
FROM sellers AS S
	WHERE S.seller_zip_code_prefix BETWEEN 2000 AND 3000
ORDER BY S.seller_id ASC;


-- Query 5 
-- Purpose:
-- Retrieve products weighing more than 100 grams
-- and sort them by weight in ascending order.
SELECT
    P.product_id,
    P.product_category_name
FROM products AS P
	WHERE P.product_weight_g > 100
ORDER BY P.product_weight_g ASC;
-- displaying the weight can improve the clarity but as we told, it isn't mandatory.
SELECT
    P.product_id,
    P.product_category_name,
    P.product_weight_g
FROM products AS P
	WHERE P.product_weight_g > 100
ORDER BY P.product_weight_g ASC;


-- Query 6
-- Purpose:
-- Identify orders delivered later than their estimated delivery date.
SELECT
    O.order_id,
    O.order_delivered_customer_date,
    O.order_estimated_delivery_date
FROM orders AS O
	WHERE O.order_delivered_customer_date > O.order_estimated_delivery_date
ORDER BY O.order_delivered_customer_date DESC;


-- Query 7
-- Purpose:
-- Retrieve customers whose ZIP code prefix falls between 1000 and 5999.
SELECT
    C.customer_id,
    C.customer_zip_code_prefix
FROM customers AS C
WHERE C.customer_zip_code_prefix BETWEEN 1000 AND 5999
ORDER BY C.customer_zip_code_prefix ASC;


-- Query 8 
-- Purpose:
-- Retrieve sellers located in the state of São Paulo (SP) and sort them alphabetically by city.
SELECT
    S.seller_id,
    S.seller_city,
    S.seller_state
FROM sellers AS S
WHERE S.seller_state = 'SP'
ORDER BY S.seller_city ASC;


/*
ANSI SQL Note:
The only SQL Server-specific syntax used in this file is YEAR().
In ANSI SQL, YEAR(date_column) is typically written as:

EXTRACT(YEAR FROM date_column)

All other queries use ANSI-standard SQL syntax and can be executed
with little or no modification in most relational database systems.
*/