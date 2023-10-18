from glob import glob
from time import sleep

from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from msrest.authentication import ApiKeyCredentials

from starter.sample_submission.src.config import CustomVisionConfig

training_client = CustomVisionTrainingClient(
    endpoint=CustomVisionConfig.ENDPOINT,
    credentials=ApiKeyCredentials(in_headers={"Training-key": CustomVisionConfig.KEY})
)

# Created project "Lighter Detection" (lighter-detection)
images = glob('starter/lighter_images/*')
batch_size = 64
for i in range(0, len(images), batch_size):
    batch_images = images[i:i + batch_size]

    project = training_client.create_images_from_files(
        project_id=CustomVisionConfig.PROJECT_ID,
        batch=batch_images,
    )

