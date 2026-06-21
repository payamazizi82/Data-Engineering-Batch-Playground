# Query 1
# Purpose:
# Retrieve the first 5 orders with the earliest estimated delivery dates.
spark.sql("""
SELECT
    O.order_id,
    O.order_estimated_delivery_date
FROM Orders O
ORDER BY O.order_estimated_delivery_date ASC
LIMIT 5
""").show()
# Notes:
# LIMIT is the Spark SQL equivalent of TOP (5).
# ORDER BY determines which rows are selected.


# Query 2 (TOP 5 PERCENT Equivalent)
# Purpose:
# Retrieve the latest 5 percent of approved orders.
spark.sql("""
WITH ordered_orders AS (
    SELECT
        O.order_id,
        O.order_approved_at,
        ROW_NUMBER() OVER (
            ORDER BY O.order_approved_at DESC
        ) AS rn,
        COUNT(*) OVER () AS total_rows
    FROM Orders O
)
SELECT
    order_id,
    order_approved_at
FROM ordered_orders
WHERE rn <= CEIL(total_rows * 0.05)
""").show()
# Notes:
# Spark SQL does not support TOP (N) PERCENT.
# ROW_NUMBER() creates a sequential number after sorting.
# COUNT(*) OVER () calculates the total number of rows.
# CEIL(total_rows * 0.05) determines how many rows represent 5 percent.
# The query returns the most recently approved 5 percent of orders.
# NOTE THAT WE WILL ADDRESS CTE AND WINDOW FUNCTIONS LATER IN DETAIL IN ANOTHER SEPERATE SECTION


# Query 3 (TOP 10 WITH TIES Equivalent)
# Purpose:
# Retrieve the 10 most recently delivered orders, including any ties on the last delivery date.
spark.sql("""
WITH ranked_orders AS (
    SELECT
        O.order_id,
        O.order_delivered_customer_date,
        O.order_status,
        RANK() OVER (
            ORDER BY O.order_delivered_customer_date DESC
        ) AS delivery_rank
    FROM Orders O
)
SELECT
    order_id,
    order_delivered_customer_date,
    order_status
FROM ranked_orders
WHERE delivery_rank <= 10
""").show()
# Notes:
# Spark SQL does not support WITH TIES.
# RANK() assigns the same rank to identical delivery dates.
# If multiple rows share the 10th-ranked delivery date, all of them are returned.
# This closely reproduces SQL Server's TOP WITH TIES behavior.
# NOTE THAT WE WILL ADDRESS CTE AND WINDOW FUNCTIONS LATER IN DETAIL IN ANOTHER SEPERATE SECTION


# Query 4
# Purpose:
# Skip the first 10 delivered orders and retrieve the next 5 orders.
spark.sql("""
SELECT
    O.customer_id,
    O.order_id,
    O.order_status
FROM Orders O
ORDER BY O.order_delivered_customer_date
LIMIT 5 OFFSET 10
""").show()
# Notes:
# Equivalent to OFFSET 10 FETCH NEXT 5 ROWS ONLY.
# Requires Spark 3.4+.
