- This project on Airbnb is about loading the csv file from kaggle to container using python script. Connected to the storage account created for this project by providing azure connection string and container name using BlobServiceClient function.
- Once the csv file is loaded into the container as raw data, databricks is used carry out some transformations like updating the columns datatypes, creating additional datafarmes and loading the tranformed data file again to the container as tranformed data.
- Post this the transformed data file is loaded into a table in azure synapse analytics and additional transformations are carried out on top of it.

![Architecture Diagram](https://raw.githubusercontent.com/adityaa2b/Data-Engineer-learning-guide/main/Hands-on%20projects/Airbnb/Architecture.png)
