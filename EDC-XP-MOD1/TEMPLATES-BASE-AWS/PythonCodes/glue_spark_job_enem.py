import sys
from pyspark.context import SparkContext
from awsglue.utils import getResolvedOptions
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: ['JOB_NAME']
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
GlueContext = GlueContext(sc)
Spark = GlueContext.Spark_Session
job = Job(GlueContext)
job.init(args['JOB_NAME'],args)

# A partir daqui o mesmo código executado no emr

# Ler dados do enem
enem = (
    spark.read.format("csv")
              .option("header", True)
              .option("InferSchema", True)
              .option("Delimiter", ";")
              .load("URI do caminho do Arquivo")
)

# Escrever no datalake em parquet
(
    enem.write
        .mode("ovewrite")
        .format("parquet")
        .partitionBy('year')
        .save("caminho_data_lake")
)