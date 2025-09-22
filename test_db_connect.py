# Databricks notebook source
display(dbutils.fs.ls("dbfs:/user"))



# COMMAND ----------

# Choose a new folder (or delete old one)
new_path = "dbfs:/user/ankit/retail_db"
dbutils.fs.rm(new_path, True)  # Remove if exists

# Folder is now guaranteed empty
dbutils.fs.mkdirs(new_path)     # Optional: can let Delta create it automatically


# COMMAND ----------

# MAGIC %sql
# MAGIC -- 1️⃣ Drop the database if it exists (CASCADE removes all tables inside)
# MAGIC DROP DATABASE IF EXISTS itversity_retail_db CASCADE;
# MAGIC
# MAGIC -- 2️⃣ Create the database in a separate folder
# MAGIC CREATE DATABASE itversity_retail_db
# MAGIC LOCATION 'dbfs:/user/ankit/retail_db';
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Double-check no dangling path
# MAGIC DESCRIBE DATABASE EXTENDED itversity_retail_db;
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC USE itversity_retail_db;
# MAGIC
# MAGIC DROP TABLE IF EXISTS orders;
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC -- 4️⃣ Create Delta table in managed warehouse
# MAGIC CREATE TABLE itversity_retail_db.orders (
# MAGIC   order_id BIGINT,
# MAGIC   order_date STRING,
# MAGIC   order_customer_id BIGINT,
# MAGIC   order_status STRING
# MAGIC )
# MAGIC USING delta;
# MAGIC

# COMMAND ----------

# MAGIC %fs ls user/ankit/retail_db/orders/_delta_log/_commits/

# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT INTO itversity_retail_db.orders VALUES
# MAGIC (1, '2025-09-22', 101, 'DELIVERED');
# MAGIC

# COMMAND ----------

