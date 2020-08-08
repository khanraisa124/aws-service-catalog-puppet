import boto3
import time


client = boto3.client("servicecatalog")


while True:
    print(client.search_products_as_admin())
    time.sleep(1)
