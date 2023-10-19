from azure.storage.blob import BlobServiceClient

from starter.sample_submission.src.config import BlobStorage as BS

client = BlobServiceClient.from_connection_string(BS.CONNECTION_STRING)
container_client = client.get_container_client(BS.VIDEO_CONTAINER_NAME)
is_container_exist = container_client.exists()

print(f'Container {BS.VIDEO_CONTAINER_NAME} exists: {is_container_exist}')
if not is_container_exist:
    container_client.create_container()
    print(f'Container {BS.VIDEO_CONTAINER_NAME} created')

