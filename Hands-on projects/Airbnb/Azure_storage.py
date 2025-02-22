from azure.storage.blob import BlobServiceClient
import os

# Azure Storage Account details
AZURE_STORAGE_CONNECTION_STRING = "YOUR STORAGE ACCOUNT DETAILS"
CONTAINER_NAME = "CONTAINER DETAILS"

# Upload files from Kaggle data folder
local_folder = "YOUR DATA FILE LOCATION"

# Create a BlobServiceClient
blob_service_client = BlobServiceClient.from_connection_string(AZURE_STORAGE_CONNECTION_STRING)

#get blob client
blob_client = blob_service_client.get_blob_client(container=CONTAINER_NAME, blob="FILENAME")

# upload file to the container
with open(local_folder, "rb") as data:
    blob_client.upload_blob(data, overwrite=True)
        
print(f"Uploaded file {local_folder} to {CONTAINER_NAME}")
