# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC #This is the main notebook in the main branch

# COMMAND ----------

df = spark.range(1000)

print(f"Count is: {df.count()}")
