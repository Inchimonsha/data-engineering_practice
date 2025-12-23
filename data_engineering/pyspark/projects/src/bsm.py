import os
import findspark
findspark.init(r"C:/main/source/utils/spark-4.0.0-bin-hadoop3")


from pyspark.sql import SparkSession

csv_path = r"C:\main\data_science\repos\ml_practice\data_engineering\resources\data\ratings.csv"

if not os.path.exists(csv_path):
    raise FileNotFoundError(f"Файл не найден: {csv_path}")

spark = SparkSession.builder.master("local[*]").getOrCreate()

# data = spark.read.csv(csv_path, inferSchema=True, header=True)
# data.show(5)
