from azure.storage.blob import BlobServiceClient
import os

# Azure Storage Account details
AZURE_STORAGE_CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=airbnbdataab;AccountKey=pj0V2sOHbnitwqSzoggpV+NTx/T9+667fFJlzhQKxpm4t5BZp0dQc11LcThIazi8SMZfSbseG+x9+AStkjMKpQ==;EndpointSuffix=core.windows.net"
CONTAINER_NAME = "kaggle-data/raw-data"

# Upload files from Kaggle data folder
local_folder = "D:/Study/Airbnb/Airbnb_Open_Data.csv"

# Create a BlobServiceClient
blob_service_client = BlobServiceClient.from_connection_string(AZURE_STORAGE_CONNECTION_STRING)

#get blob client
blob_client = blob_service_client.get_blob_client(container=CONTAINER_NAME, blob="Airbnb_Open_Data.csv")

# upload file to the container
with open(local_folder, "rb") as data:
    blob_client.upload_blob(data, overwrite=True)
        
print(f"Uploaded file {local_folder} to {CONTAINER_NAME}")