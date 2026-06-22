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


# Query 5
# Purpose:
# Skip the first 10 delivered orders and return all remaining rows.
spark.sql("""
SELECT
    O.customer_id,
    O.order_id,
    O.order_status
FROM Orders O
ORDER BY O.order_delivered_customer_date
OFFSET 10
""").show()
# Notes:
# Equivalent to OFFSET 10 ROWS.
# Supported in modern Spark versions.


# Query 6
# Purpose:
# Retrieve the 15 most recently approved orders.
spark.sql("""
SELECT
    O.order_id,
    O.order_approved_at,
    O.order_status
FROM Orders O
ORDER BY O.order_approved_at DESC
LIMIT 15
""").show()
# Notes:
# Direct replacement for TOP (15).


# Query 7 (TOP 3 PERCENT Equivalent)
# Purpose:
# Retrieve the earliest 3 percent of delivered orders.
spark.sql("""
WITH ordered_orders AS (
    SELECT
        O.order_id,
        O.order_delivered_customer_date,
        ROW_NUMBER() OVER (
            ORDER BY O.order_delivered_customer_date ASC
        ) AS rn,
        COUNT(*) OVER () AS total_rows
    FROM Orders O
)
SELECT
    order_id,
    order_delivered_customer_date
FROM ordered_orders
WHERE rn <= CEIL(total_rows * 0.03)
""").show()
# Notes:
# Spark SQL does not support TOP (N) PERCENT.
# ROW_NUMBER() creates a sequence after sorting.
# COUNT(*) OVER () obtains the total row count.
# CEIL(total_rows * 0.03) calculates 3 percent of the dataset.
# The query returns the earliest 3 percent of deliveries.
# NOTE THAT WE WILL ADDRESS CTE AND WINDOW FUNCTIONS LATER IN DETAIL IN ANOTHER SEPERATE SECTION


# Query 8
# Purpose:
# Retrieve the 20 highest freight-value order items, including ties.
spark.sql("""
WITH ranked_items AS (
    SELECT
        OI.order_id,
        OI.freight_value,
        RANK() OVER (
            ORDER BY OI.freight_value DESC
        ) AS freight_rank
    FROM Order_Items OI
)
SELECT
    order_id,
    freight_value
FROM ranked_items
WHERE freight_rank <= 20
""").show()
# Notes:
# RANK() is used to mimic WITH TIES behavior.
# NOTE THAT WE WILL ADDRESS CTE AND WINDOW FUNCTIONS LATER IN DETAIL IN ANOTHER SEPERATE SECTION


# Query 9
# Purpose:
# Skip the first 20 customers ordered by ZIP code and retrieve the next 10 customers.
spark.sql("""
SELECT
    C.customer_id,
    C.customer_zip_code_prefix
FROM Customers C
ORDER BY C.customer_zip_code_prefix
LIMIT 10 OFFSET 20
""").show()
# Notes:
# Equivalent to OFFSET 20 FETCH NEXT 10 ROWS ONLY.


# Query 10
# Purpose:
# Skip the first 50 products ordered by weight and return all remaining products.
spark.sql("""
SELECT
    P.product_id,
    P.product_weight_g
FROM Products P
ORDER BY P.product_weight_g
OFFSET 50
""").show()
# Notes:
# Equivalent to OFFSET 50 ROWS in SQL Server.


# PySpark SQL Notes and Differences from T-SQL
# -----------------------------------------------------------
# 1. TOP (N)

# T-SQL:
# TOP (10)

# PySpark SQL:
# LIMIT 10
# -----------------------------------------------------------
# 2. TOP (N) PERCENT

# T-SQL:
# TOP (5) PERCENT

# PySpark SQL:
# No direct equivalent exists.
# Common approach:
# ROW_NUMBER()
# COUNT(*) OVER ()

# Why?
# * Spark SQL cannot use TOP PERCENT.
# * Spark SQL cannot dynamically place a subquery inside LIMIT.
# * Window functions provide a portable solution.
# -----------------------------------------------------------
# 3. TOP (N) WITH TIES

# T-SQL:
# TOP (10) WITH TIES

# PySpark SQL:
# No direct equivalent exists.
# Common approaches:
# RANK()
# DENSE_RANK()

# Why?
# * Rows sharing the same ranking value are returned together.
# * This closely mimics WITH TIES behavior.
# -----------------------------------------------------------
# 4. OFFSET/FETCH

# T-SQL:
# OFFSET 10 ROWS
# FETCH NEXT 5 ROWS ONLY

# PySpark SQL:
# LIMIT 5 OFFSET 10
# -----------------------------------------------------------
# 5. Window Functions Become More Important

# In T-SQL:
# TOP
# TOP PERCENT
# TOP WITH TIES
# solve many row-limiting problems directly.

# In Spark SQL:
# Window functions often replace these features:
# ROW_NUMBER()
# RANK()
# DENSE_RANK()
# COUNT(*) OVER ()
# Therefore, window functions are much more important in Spark SQL than in SQL Server for these types of queries.
# -----------------------------------------------------------
# Summary

# | T-SQL             | PySpark SQL                     |
# | ----------------- | ------------------------------- |
# | TOP (N)           | LIMIT                           |
# | TOP (N) PERCENT   | ROW_NUMBER() + COUNT(*) OVER () |
# | TOP (N) WITH TIES | RANK() or DENSE_RANK()          |
# | OFFSET/FETCH      | LIMIT + OFFSET                  |
# | GO                | Separate spark.sql() calls      |

# For these queries, the biggest differences are:

# TOP becomes LIMIT.
# TOP PERCENT requires window functions.
# TOP WITH TIES requires ranking functions.
# GO does not exist.
# Window functions are used much more frequently in Spark SQL.
