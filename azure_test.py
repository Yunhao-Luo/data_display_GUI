import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__
 
def download_files():
    try:
        print("Azure Blob Storage v" + __version__ + " - Python quickstart sample")
        
        # Quick start code goes here
        # Retrieve the connection string for use with the application. The storage
        # connection string is stored in an environment variable on the machine
        # running the application called AZURE_STORAGE_CONNECTION_STRING. If the environment variable is
        # created after the application is launched in a console or with Visual Studio,
        # the shell or application needs to be closed and reloaded to take the
        # environment variable into account.
        connect_str = "DefaultEndpointsProtocol=https;AccountName=guitest123;AccountKey=EYfH5nXHpHf/iUp1Au8lIECTcucjgh3RZbM8mO+DPiuzj8nN41274PRY4rBoeSilaaLdNOTX2EfJ+AStgnL0uQ==;EndpointSuffix=core.windows.net"
        
        # Create the BlobServiceClient object which will be used to create a container client
        blob_service_client = BlobServiceClient.from_connection_string(connect_str)

        container_client = blob_service_client.get_container_client("downloadtest")
        
        print("\nListing blobs...")
        
        # List the blobs in the container
        blob_list = container_client.list_blobs()
        for blob in blob_list:
            print("\t" + blob.name)
        
        # Download the blob to a local file
        # Add 'DOWNLOAD' before the .txt extension so you can see both files in the data directory
        local_path = "./data"
        if not os.path.exists(local_path):
            os.mkdir(local_path)
        download_file_path = os.path.join(local_path)
        blob_client = blob_service_client.get_container_client(container= "downloadtest")
        print("\nDownloading blob to \n\t" + download_file_path)

        # To do: create files with names in blob_list and use download_blob().readall() to write contents to each file.
        # Modify the code below to download all files.
        # To do: for blob in blob_list, create a file with blob name & write contents from download_blob into the file.

        print('start downloading...')

        blob_list = container_client.list_blobs()
        os.chdir(download_file_path)

        for blob in blob_list:
                with open(blob.name, "wb") as download_file:
                    download_file.write(blob_client.download_blob(blob.name).readall())
    
    
    except Exception as ex:
        print('Exception:')
        print(ex)
