import os
import uuid

from starter.sample_submission.src.config import BlobStorage

from azure.storage.blob import BlobServiceClient, ContentSettings

subscription_key = BlobStorage.ACCOUNT_KEY
location = BlobStorage.LOCATION
account_id = BlobStorage.ACCOUNT_NAME
video_path = "../material_preparation_step/videos/avkash-boarding-pass.mp4"
video_name = os.path.basename(video_path)
unique_video_name = uuid.uuid4().hex + video_name

# upload video to blob storage


blob_service_client = BlobServiceClient.from_connection_string(BlobStorage.CONNECTION_STRING)
container_client = blob_service_client.get_container_client(BlobStorage.VIDEO_CONTAINER_NAME)
content_type = 'video/mp4'

# Upload video to blob storage
blob_client = container_client.get_blob_client(unique_video_name)
with open(video_path, "rb") as data:
    blob_client.upload_blob(data, blob_type="BlockBlob", content_settings=ContentSettings(content_type=content_type))

print(f'File uploaded to Video Indexer with ID: {unique_video_name}')
