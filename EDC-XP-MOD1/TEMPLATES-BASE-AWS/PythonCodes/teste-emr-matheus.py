import pyspark

# Ler dados do enem
enem = (
    spark.read.format("csv")
              .option("header", True)
              .option("InferSchema", True)
              .option("Delimiter", ";")
              .load("URI do caminho do Arquivo")
)

enem.printSchema()

df = enem.select("NU_IDADE","TP_SEXO","TP_ESTADO_CIVIL","TP_COR_RACA","TP_NACIONALIDADE","NU_NOTA_CN","NU_NOTA_CH","NU_NOTA_LC","NU_NOTA_MT")

df.show(10)

df.count()

(
    df.groupby("TP_SEXO")
    .agg(mean(col("NU_IDADE")).alias("MED_IDADE"),
    count(col("TP_SEXO")).alias("CONTAGEM"),
    max(col("NU_NOTA_MT")).alias("MAX_NOTA_MT")
    min(col("NU_NOTA_MT")).alias("MIN_NOTA_MT")
    .show()
    )
)

(
    enem.write
        .mode("ovewrite")
        .format("parquet")
        .partitionBy('year')
        .save("caminho_data_lake")
)