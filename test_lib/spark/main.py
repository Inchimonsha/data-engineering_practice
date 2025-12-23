from pyspark.python.pyspark.shell import spark
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

schema = StructType(fields=[
    StructField("col_1", IntegerType()),
    StructField("col_2", StringType ())
])

df = spark.read.csv("/path/file_name", schema=schema, sep=";")