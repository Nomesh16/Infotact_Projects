from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("EchoChain").getOrCreate()

df_spark = spark.read.csv("../EchoChain_20000.csv", header=True, inferSchema=True)

df_spark.printSchema()

df_spark.groupBy("Brand").avg("Circularity_Score").show()

spark.stop()