-- Query 1 
-- Purpose: 
-- Retrieve the first 5 orders with the earliest estimated delivery dates.
SELECT TOP (5) 
    O.order_id, 
    O.order_estimated_delivery_date 
FROM Orders AS O 
ORDER BY O.order_estimated_delivery_date ASC; GO
-- Notes: 
-- TOP (5) returns exactly five rows. 
-- ORDER BY ASC ensures the earliest delivery dates are returned first. 
-- Without ORDER BY, TOP may return arbitrary rows.

-- Query 2 
-- Purpose: 
-- Retrieve the latest 5 percent of approved orders.
SELECT TOP (5) 
    PERCENT O.order_id, 
    O.order_approved_at 
FROM Orders AS O 
ORDER BY O.order_approved_at DESC; GO
-- Notes: 
-- TOP PERCENT returns a percentage of rows rather than a fixed count. 
-- The number of rows returned depends on the total row count. 
-- ORDER BY DESC returns the most recently approved orders.

-- Query 3 
-- Purpose: 
-- Retrieve the 10 most recently delivered orders, including any ties on the last delivery date.
SELECT 
    TOP (10) WITH TIES  
    O.order_id,     
    O.order_delivered_customer_date,    
    O.order_status 
FROM Orders AS O 
ORDER BY O.order_delivered_customer_date DESC; GO
-- Notes: 
-- WITH TIES may return more than 10 rows. 
-- Additional rows are included when they share the same ORDER BY value as the final row within the TOP limit. 
-- Useful when ranking data fairly.

-- Query 4 
-- Purpose: 
-- Skip the first 10 delivered orders and retrieve the next 5 orders.
SELECT 
    O.customer_id, 
    O.order_id, 
    O.order_status 
FROM Orders AS O 
ORDER BY O.order_delivered_customer_date 
OFFSET 10 ROWS FETCH NEXT 5 ROWS ONLY; GO
-- Notes: 
-- OFFSET skips a specified number of rows. 
-- FETCH NEXT limits the number of returned rows. 
-- Commonly used for pagination.

-- Query 5 
-- Purpose: 
-- Skip the first 10 delivered orders and return all remaining rows.
SELECT 
    O.customer_id, 
    O.order_id, 
    O.order_status 
FROM Orders AS O 
ORDER BY O.order_delivered_customer_date OFFSET 10 ROWS; GO
-- Notes: 
-- OFFSET can be used without FETCH. 
-- Returns all rows after the skipped rows. 
-- ORDER BY is mandatory when using OFFSET.

-- Query 6 
-- Purpose: 
-- Retrieve the 15 most recently approved orders.
SELECT TOP (15) 
    O.order_id, 
    O.order_approved_at, 
    O.order_status 
FROM Orders AS O 
ORDER BY O.order_approved_at DESC; GO
-- Notes: 
-- Similar to Query 1 but focused on recent approvals. 
-- Frequently used in operational reporting.

-- Query 7 
-- Purpose: 
-- Retrieve the earliest 3 percent of delivered orders.
SELECT 
    TOP (3) PERCENT 
    O.order_id, 
    O.order_delivered_customer_date 
FROM Orders AS O 
ORDER BY O.order_delivered_customer_date ASC; GO
-- Notes: 
-- ASC is required because the goal is to retrieve the earliest deliveries. 
-- DESC would return the most recent deliveries instead. 
-- The number of rows depends on the total table size.

-- Query 8 
-- Purpose: 
-- Retrieve the 20 highest freight-value order items, including ties.
SELECT 
    TOP (20) WITH TIES 
    OI.order_id, 
    OI.freight_value 
FROM Order_Items AS OI 
ORDER BY OI.freight_value DESC; GO
-- Notes: 
-- WITH TIES includes additional rows that have the same freight value as the last row within the TOP limit. 
-- Useful when ranking monetary values.

-- Query 9 
-- Purpose: 
-- Skip the first 20 customers ordered by ZIP code and retrieve the next 10 customers.
SELECT 
    C.customer_id, 
    C.customer_zip_code_prefix 
FROM Customers AS C 
ORDER BY C.customer_zip_code_prefix 
OFFSET 20 ROWS FETCH NEXT 10 ROWS ONLY; GO
-- Notes: 
-- Another pagination example. 
-- Often used in web applications and reporting systems. 
-- Results are deterministic because ORDER BY is specified.

-- Query 10 
-- Purpose: 
-- Skip the first 50 products ordered by weight and return all remaining products.
SELECT 
    P.product_id, P.product_weight_g 
    FROM Products AS P 
ORDER BY P.product_weight_g 
OFFSET 50 ROWS; GO
-- Notes: 
-- Demonstrates OFFSET without FETCH. 
-- Returns all products after the first 50 sorted by weight. 
-- Useful for paging through large datasets.