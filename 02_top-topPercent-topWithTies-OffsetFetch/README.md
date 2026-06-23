# 📊 02 - LIMIT / TOP / WINDOW-LIKE OPERATIONS (Batch Processing Advanced Basics)

## 📌 Overview

This section builds on basic SQL concepts and focuses on **row-limiting and ranking-style operations** using the **Brazilian E-Commerce Dataset (Olist)**.

It demonstrates how different systems handle:

- TOP N rows
- TOP N PERCENT
- TOP WITH TIES
- OFFSET / FETCH pagination
- Ranking-based filtering

Implemented in:

- T-SQL (SQL Server style)
- Spark SQL
- Spark DataFrame API (PySpark)

The goal is to understand how SQL Server features map to Spark equivalents, especially where Spark requires **window functions instead of built-in syntax**.

---

## 📂 Files in This Section

```text
tsql.sql              → T-SQL TOP / OFFSET / ANSI notes
spark_sql.py          → Spark SQL equivalents using spark.sql()
spark_dataframe.py    → PySpark DataFrame implementations
```
## ⚙️ Required Setup

### Spark DataFrames used:

- orders_df
- customers_df
- products_df
- order_items_df

### Required imports (DataFrame API):
```python
from pyspark.sql import functions as F
from pyspark.sql.window import Window
```

## 🧠 Concepts Covered

- TOP N equivalent (LIMIT)
- TOP N PERCENT equivalent
- TOP WITH TIES equivalent
- OFFSET / FETCH pagination
- Window functions (ROW_NUMBER, RANK, COUNT)
- Ordering and ranking logic
- Dataset slicing strategies in Spark

## 📌 Important Differences (T-SQL vs Spark vs DataFrame)

| Concept | T-SQL Syntax | Spark SQL / DataFrame Equivalent |
|----------|-------------|----------------------------------|
| TOP (N) | `TOP (N)` | `LIMIT N` |
| TOP (N) PERCENT | `TOP (N) PERCENT` | `ROW_NUMBER() + COUNT(*) OVER()` |
| TOP WITH TIES | `WITH TIES` | `RANK()` / `DENSE_RANK()` |
| OFFSET / FETCH | `OFFSET ... FETCH` | `LIMIT + OFFSET` |
| Window Ranking | Built-in TOP-related features | Window functions required |

## 📊 Key Notes (for this section)
- Spark SQL replaces `TOP` with `LIMIT`.
- Spark does NOT support:
    - `TOP PERCENT`
    - `TOP WITH TIES`
    - → these require **window functions**
- DataFrame API relies heavily on:
    - `Window`
    - `row_number()`
    - `rank()`
    - `count(*) over()`
- Pagination in Spark is simulated using:
    - `limit()`
    - `offset (SQL only)`
    - `subtract() (DataFrame workaround)`
- T-SQL is included as a reference system for comparison, not execution.
- Window functions become essential in Spark, while in SQL Server many of these features are built-in.

## 🚀 Learning Goal

### By completing this section, you should be able to:

- Understand how TOP / LIMIT differs across systems
- Implement ranking logic using Spark Window functions
- Translate SQL Server pagination into Spark logic
- Recognize when Spark requires more explicit transformations
- Compare relational vs distributed execution behavior
