import boto3
import pandas as pd

#Criar um client para interagir com o AWS S3
#Baixando arquivo do bucket para local e exibindo o df
s3_client = boto3.client('s3')

s3_client.download_file('my_bucket_name', 'my_key_name','my_local_file_name')

df = pd.read_csv('my_local_file_name.csv', sep=";")
print(df)

#para executar o código digitar no terminal: python interact_s3.py

#Subindo um arquivo local para o bucket

s3_client.upload_file("nome_do_arquivo.csv","nome_do_bucket","nome_do_arquivo_no_bucket")