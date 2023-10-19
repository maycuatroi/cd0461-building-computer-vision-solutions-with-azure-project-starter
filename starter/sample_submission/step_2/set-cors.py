from azure.storage.blob import BlobServiceClient
from azure.storage.blob import CorsRule

from starter.sample_submission.src.config import BlobStorage

blob_service_client = BlobServiceClient.from_connection_string(BlobStorage.CONNECTION_STRING)

cors_rule = CorsRule(
    allowed_origins=['*'],
    allowed_methods=['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'],
    allowed_headers=['*'],
    exposed_headers=['*'],
    max_age_in_seconds=3600
)

# Set the CORS rules on the service
service_properties = blob_service_client.get_service_properties()
service_properties['cors'] = [cors_rule]
blob_service_client.set_service_properties(service_properties)
print('CORS configured successfully')