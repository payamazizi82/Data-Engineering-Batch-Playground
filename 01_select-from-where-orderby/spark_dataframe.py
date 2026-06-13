from pyspark.sql.functions import col, year

# Query 1
# Purpose:
# Retrieve all customer IDs and their corresponding order IDs.
orders_df.select( "customer_id", "order_id" ).show()
# Notes:
# Returns all customer-order relationships.
# No filtering is applied.


# Query 2
# Purpose:
# Retrieve the estimated delivery year for orders whose estimated delivery date is after January 1, 2017.
orders_df.filter(col("order_estimated_delivery_date") > "2017-01-01" ).select( year("order_estimated_delivery_date").alias("estimated_delivery_year") ).show()
# Notes:
# year() extracts the year from a date column.
# Results may contain duplicate years.
# Alternative version using distinct()
orders_df.filter(col("order_estimated_delivery_date") > "2017-01-01" ).select( year("order_estimated_delivery_date").alias("estimated_delivery_year") ).distinct().show()
# Notes:
# distinct() removes duplicate years.


# Query 3
# Purpose:
# Retrieve customers located in specific cities and sort the results by city name in descending order.
customers_df.filter( col("customer_city").isin("valinhos", "sao paulo", "mendonca") ).select( "customer_id", "customer_city" ).orderBy( col("customer_city").desc() ).show()
# Notes:
# isin() is equivalent to SQL IN().
# Results are sorted from Z to A.


# Query 4
# Purpose:
# Retrieve sellers whose ZIP code prefix is between 2000 and 3000, ordered by seller ID.
sellers_df.filter( col("seller_zip_code_prefix").between(2000, 3000) ).select( "seller_state", "seller_city" ).orderBy( col("seller_id").asc() ).show()
# Notes:
# between() includes both endpoints.
# seller_id is used for sorting but is not displayed.
# Alternative version displaying seller_id
sellers_df.filter( col("seller_zip_code_prefix").between(2000, 3000) ).select( "seller_id", "seller_state", "seller_city" ).orderBy( col("seller_id").asc() ).show()
# Notes:
# Makes the ordering column visible.


# Query 5
# Purpose:
# Retrieve products weighing more than 100 grams and sort them by weight in ascending order.
products_df.filter( col("product_weight_g") > 100 ).select( "product_id", "product_category_name" ).orderBy( col("product_weight_g").asc() ).show()
# Notes:
# Sorting is performed using product_weight_g.
# The weight itself is not displayed.
# Alternative version displaying weight
products_df.filter( col("product_weight_g") > 100 ).select( "product_id", "product_category_name", "product_weight_g" ).orderBy( col("product_weight_g").asc() ).show()
# Notes:
# Makes the sorting column visible.


# Query 6
# Purpose:
# Identify orders delivered later than their estimated delivery date.
orders_df.filter( col("order_delivered_customer_date") > col("order_estimated_delivery_date") ).select( "order_id", "order_delivered_customer_date", "order_estimated_delivery_date" ).orderBy( col("order_delivered_customer_date").desc() ).show()
# Notes:
# Useful for identifying delayed deliveries.
# Compares values from two columns.


# Query 7
# Purpose:
# Retrieve customers whose ZIP code prefix falls between 1000 and 5999.
customers_df.filter( col("customer_zip_code_prefix").between(1000, 5999) ).select( "customer_id", "customer_zip_code_prefix" ).orderBy( col("customer_zip_code_prefix").asc() ).show()
# Notes:
# between() includes both boundary values.
# Results are sorted by ZIP code.


# Query 8
# Purpose:
# Retrieve sellers located in the state of São Paulo (SP) and sort them alphabetically by city.
sellers_df.filter( col("seller_state") == "SP" ).select( "seller_id", "seller_city", "seller_state" ).orderBy( col("seller_city").asc() ).show()
# Notes:
# Filters sellers from São Paulo.
# Results are sorted alphabetically by city.