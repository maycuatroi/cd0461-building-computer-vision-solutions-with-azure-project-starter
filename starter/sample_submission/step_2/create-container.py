from azure.storage.blob import BlobServiceClient

from starter.sample_submission.src.config import BlobStorage as BS

client = BlobServiceClient.from_connection_string(BS.CONNECTION_STRING)
container_client = client.get_container_client(BS.FORM_TRAINING_CONTAINER)
is_container_exist = container_client.exists()

print(f'Container {BS.FORM_TRAINING_CONTAINER} exists: {is_container_exist}')
if not is_container_exist:
    container_client.create_container()
    print(f'Container {BS.FORM_TRAINING_CONTAINER} created')

