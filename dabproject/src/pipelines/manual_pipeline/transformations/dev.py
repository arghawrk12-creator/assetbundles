import dlt

@dlt.table
def dev():
  df = spark.range(10)
  return df