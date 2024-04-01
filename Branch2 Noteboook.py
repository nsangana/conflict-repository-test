# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC #this is branch 2 notebook

# COMMAND ----------

spark.sparkContext.getConf().getAll()

# COMMAND ----------

print("hello")

# COMMAND ----------

dbutils.notebook.entry_point.getDbutils().notebook().getContext().notebookPath().get()
