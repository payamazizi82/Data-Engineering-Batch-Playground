# Query 1
# Purpose:
# Retrieve the first 5 orders with the earliest estimated delivery dates.
orders_df.orderBy("order_estimated_delivery_date").limit(5).show()
# Notes:
# limit() is the DataFrame equivalent of LIMIT in Spark SQL.
# orderBy() determines which rows are selected.


# Query 2 (TOP 5 PERCENT Equivalent)
# Purpose:
# Retrieve the latest 5 percent of approved orders.
from pyspark.sql import functions as F
from pyspark.sql.window import Window

window_spec = Window.orderBy(F.col("order_approved_at").desc())

orders_df \
    .withColumn(
        "rn",
        F.row_number().over(window_spec)
    ) \
    .withColumn(
        "total_rows",
        F.count("*").over(Window.partitionBy())
    ) \
    .filter(
        F.col("rn") <= F.ceil(F.col("total_rows") * 0.05)
    ) \
    .select(
        "order_id",
        "order_approved_at"
    ) \
    .show()

# Notes:
# Spark DataFrames do not have a TOP PERCENT method.
# row_number() and count() window functions are used instead.
# We will cover Window Functions later in a dedicated section.


# Query 3 (TOP 10 WITH TIES Equivalent)
# Purpose:
# Retrieve the 10 most recently delivered orders, including any ties on the last delivery date.
window_spec = Window.orderBy(
    F.col("order_delivered_customer_date").desc()
)

orders_df \
    .withColumn(
        "delivery_rank",
        F.rank().over(window_spec)
    ) \
    .filter(
        F.col("delivery_rank") <= 10
    ) \
    .select(
        "order_id",
        "order_delivered_customer_date",
        "order_status"
    ) \
    .show()

# Notes:
# Spark DataFrames do not support WITH TIES directly.
# rank() reproduces similar behavior.
# We will cover Window Functions later in a dedicated section.


# Query 4
# Purpose:
# Skip the first 10 delivered orders and retrieve the next 5 orders.
orders_df \
    .orderBy("order_delivered_customer_date") \
    .limit(15) \
    .subtract(
        orders_df
        .orderBy("order_delivered_customer_date")
        .limit(10)
    ) \
    .show()
# Notes:
# DataFrames do not have a direct FETCH NEXT syntax.
# This approximates OFFSET/FETCH behavior.


# Query 5
# Purpose:
# Skip the first 10 delivered orders and return all remaining rows.
orders_df \
    .orderBy("order_delivered_customer_date") \
    .subtract(
        orders_df
        .orderBy("order_delivered_customer_date")
        .limit(10)
    ) \
    .show()
# Notes:
# DataFrames do not provide a direct OFFSET method.
# Alternative approaches often use row_number().


# Query 6
# Purpose:
# Retrieve the 15 most recently approved orders.
orders_df \
    .orderBy(
        F.col("order_approved_at").desc()
    ) \
    .limit(15) \
    .select(
        "order_id",
        "order_approved_at",
        "order_status"
    ) \
    .show()
# Notes:
# Direct equivalent of LIMIT 15.


# Query 7 (TOP 3 PERCENT Equivalent)
# Purpose:
# Retrieve the earliest 3 percent of delivered orders.
window_spec = Window.orderBy(
    F.col("order_delivered_customer_date").asc()
)

orders_df \
    .withColumn(
        "rn",
        F.row_number().over(window_spec)
    ) \
    .withColumn(
        "total_rows",
        F.count("*").over(Window.partitionBy())
    ) \
    .filter(
        F.col("rn") <= F.ceil(F.col("total_rows") * 0.03)
    ) \
    .select(
        "order_id",
        "order_delivered_customer_date"
    ) \
    .show()

# Notes:
# DataFrames do not have a TOP PERCENT method.
# Window functions are used instead.
# We will cover Window Functions later in a dedicated section.


# Query 8 (TOP 20 WITH TIES Equivalent)
# Purpose:
# Retrieve the 20 highest freight-value order items, including ties.
window_spec = Window.orderBy(
    F.col("freight_value").desc()
)

order_items_df \
    .withColumn(
        "freight_rank",
        F.rank().over(window_spec)
    ) \
    .filter(
        F.col("freight_rank") <= 20
    ) \
    .select(
        "order_id",
        "freight_value"
    ) \
    .show()

# Notes:
# rank() is used to emulate WITH TIES behavior.
# We will cover Window Functions later in a dedicated section.


# Query 9
# Purpose:
# Skip the first 20 customers ordered by ZIP code and retrieve the next 10 customers.
customers_df \
    .orderBy("customer_zip_code_prefix") \
    .limit(30) \
    .subtract(
        customers_df
        .orderBy("customer_zip_code_prefix")
        .limit(20)
    ) \
    .show()
# Notes:
# Approximation of LIMIT 10 OFFSET 20.


# Query 10
# Purpose:
# Skip the first 50 products ordered by weight and return all remaining products.
products_df \
    .orderBy("product_weight_g") \
    .subtract(
        products_df
        .orderBy("product_weight_g")
        .limit(50)
    ) \
    .show()
# Notes:
# Approximation of OFFSET 50.
