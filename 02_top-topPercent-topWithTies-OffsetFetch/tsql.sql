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