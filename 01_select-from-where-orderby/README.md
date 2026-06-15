# 📊 01 - SELECT / FROM / WHERE / ORDER BY (Batch Processing Basics)

## 📌 Overview

This section focuses on 8 fundamental SQL operations using the **Brazilian E-Commerce Dataset (Olist)** and demonstrates how the same logic is implemented in:

- T-SQL (SQL Server style)
- Spark SQL
- Spark DataFrame API (PySpark)

The goal is to build a strong foundation in:

- Data selection
- Filtering
- Sorting
- Basic transformations

and understand how these concepts translate between SQL and Spark.


## 📂 Files in This Section

```text
tsql.sql              → T-SQL implementations + ANSI notes
spark_sql.py          → Spark SQL queries using spark.sql()
spark_dataframe.py    → PySpark DataFrame API implementation
```

## ⚙️ Required Setup

### Spark DataFrames used:

- orders_df
- customers_df
- sellers_df
- products_df

### Required imports:

```python
from pyspark.sql.functions import col, year
```
## 🧠 Concepts Covered

- SELECT statements  
- WHERE filtering  
- ORDER BY sorting  
- IN clause  
- BETWEEN condition  
- Date extraction (YEAR)  
- Basic comparison between SQL and DataFrame API 

## 📌 Important Differences (SQL vs DataFrame API)

| SQL Concept        | Spark SQL Syntax | DataFrame API (PySpark) |
|--------------------|------------------|---------------------------|
| SELECT             | SELECT           | `.select()`              |
| WHERE              | WHERE            | `.filter()`              |
| ORDER BY           | ORDER BY         | `.orderBy()`             |
| IN                 | IN (...)         | `.isin()`                |
| BETWEEN            | BETWEEN          | `.between()`             |
| YEAR extraction    | YEAR(col)        | `year(col)`              |


