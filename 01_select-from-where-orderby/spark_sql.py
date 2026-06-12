# Query 1
# Purpose: 
# Retrieve all customer IDs and their corresponding order IDs. 
spark.sql(""" SELECT O.customer_id, O.order_id FROM orders AS O """).show() 
# Notes: 
# Returns all customer-order relationships. 
# No filtering is applied. 


# Query 2
# Purpose: 
# Retrieve the estimated delivery year for orders whose estimated delivery date is after January 1, 2017. 
spark.sql(""" SELECT YEAR(O.order_estimated_delivery_date) AS estimated_delivery_year FROM orders AS O WHERE O.order_estimated_delivery_date > '2017-01-01' """).show() 
# Notes: 
# YEAR() is supported in Spark SQL. 
# Results may contain duplicate years. 
# If unique years are required: adding DISTINCT
spark.sql(""" SELECT DISTINCT YEAR(O.order_estimated_delivery_date) AS estimated_delivery_year FROM orders AS O WHERE O.order_estimated_delivery_date > '2017-01-01' """).show() 
# Notes: 
# DISTINCT removes duplicate years. 


# Query 3
# Purpose: 
# Retrieve customers located in specific cities and sort the results by city name in descending order. 
spark.sql(""" SELECT C.customer_id, C.customer_city FROM customers AS C WHERE C.customer_city IN ('valinhos', 'sao paulo', 'mendonca') ORDER BY C.customer_city DESC """).show() 
# Notes: 
# IN() is cleaner than multiple OR conditions. 
# Results are sorted from Z to A. 


# Query 4
# Purpose: 
# Retrieve sellers whose ZIP code prefix is between 2000 and 3000, ordered by seller ID. 
spark.sql(""" SELECT S.seller_state, S.seller_city FROM sellers AS S WHERE S.seller_zip_code_prefix BETWEEN 2000 AND 3000 ORDER BY S.seller_id ASC """).show() 
# Notes: 
# BETWEEN includes both endpoints. 
# seller_id is used for sorting but not displayed. 
# Alternative version displaying seller_id: seller_id can be NOT presented here 
spark.sql(""" SELECT S.seller_id, S.seller_state, S.seller_city FROM sellers AS S WHERE S.seller_zip_code_prefix BETWEEN 2000 AND 3000 ORDER BY S.seller_id ASC """).show() 
# Notes: 
# Makes the ordering column visible. 


# Query 5
# Purpose: 
# Retrieve products weighing more than 100 grams and sort them by weight in ascending order. 
spark.sql(""" SELECT P.product_id, P.product_category_name FROM products AS P WHERE P.product_weight_g > 100 ORDER BY P.product_weight_g ASC """).show() 
# Notes: 
# Sorting is performed using product_weight_g. 
# The weight itself is not displayed. 
# Alternative version displaying weight 
spark.sql(""" SELECT P.product_id, P.product_category_name, P.product_weight_g FROM products AS P WHERE P.product_weight_g > 100 ORDER BY P.product_weight_g ASC """).show() 
# Notes: 
# Makes the sorting column visible. 


# Query 6
# Purpose: 
# Identify orders delivered later than their estimated delivery date. 
spark.sql(""" SELECT O.order_id, O.order_delivered_customer_date, O.order_estimated_delivery_date FROM orders AS O WHERE O.order_delivered_customer_date > O.order_estimated_delivery_date ORDER BY O.order_delivered_customer_date DESC """).show() 
# Notes: 
# Useful for identifying delayed deliveries. 


# Query 7
# Purpose: 
# Retrieve customers whose ZIP code prefix falls between 1000 and 5999. 
spark.sql(""" SELECT C.customer_id, C.customer_zip_code_prefix FROM customers AS C WHERE C.customer_zip_code_prefix BETWEEN 1000 AND 5999 ORDER BY C.customer_zip_code_prefix ASC """).show() 
# Notes: 
# BETWEEN includes both boundary values. 
# Results are sorted by ZIP code. 


# Query 8
# Purpose: 
# Retrieve sellers located in the state of São Paulo (SP) and sort them alphabetically by city.
spark.sql(""" SELECT S.seller_id, S.seller_city, S.seller_state FROM sellers AS S WHERE S.seller_state = 'SP' ORDER BY S.seller_city ASC """).show() 
# Notes: 
# Filters sellers from São Paulo. 
# Results are sorted alphabetically by city. 


# Spark SQL vs T-SQL Notes

# 1. YEAR() works in Spark SQL exactly as in T-SQL. 
# 2. AS for aliases is optional: FROM orders AS O = FROM orders O 
# 3. BETWEEN, IN, DISTINCT, WHERE and ORDER BY work exactly the same for these queries. 
# 4. Spark SQL queries are executed through: spark.sql(""" SQL QUERY """) instead of running directly inside SQL Server. 
# 5. ORDER BY is more expensive in Spark because Spark performs a distributed global sort. 
# 6. The query logic is identical. The major difference is the execution engine: - SQL Server -> database engine - Spark SQL -> distributed processing engine 
# 7. For these eight queries, almost no SQL syntax changes are required when moving from T-SQL to Spark SQL.