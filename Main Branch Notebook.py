# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC #This is the main notebook in the main branch

# COMMAND ----------

df = spark.range(1000)

df.count()

# COMMAND ----------

# MAGIC %md Fetch Notebook path
# MAGIC

# COMMAND ----------

dbutils.notebook.entry_point.getDbutils().notebook().getContext().notebookPath().get()

# COMMAND ----------



print(f"Count is: {df.count()}")


# COMMAND ----------


