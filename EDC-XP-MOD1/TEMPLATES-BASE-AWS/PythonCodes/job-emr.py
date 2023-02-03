from pyspark.sql.functions import mena, maxx, min, col, count
from pyspark.sq. import SparkSession

spark = (
    SparkSession.builder.appName("ExerciseSpark")
    .getOrCreate()
)

# Ler dados do enem
enem = (
    spark.read.format("csv")
              .option("header", True)
              .option("InferSchema", True)
              .option("Delimiter", ";")
              .load("URI do caminho do Arquivo")
)

(
    enem.write
        .mode("ovewrite")
        .format("parquet")
        .partitionBy('year')
        .save("caminho_data_lake")
)
