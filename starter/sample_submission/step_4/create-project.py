from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from msrest.authentication import ApiKeyCredentials

from starter.sample_submission.src.config import CustomVisionConfig

training_client = CustomVisionTrainingClient(
    endpoint=CustomVisionConfig.ENDPOINT,
    credentials=ApiKeyCredentials(in_headers={"Training-key": CustomVisionConfig.KEY})
)

# Created project "Lighter Detection" (lighter-detection)
project = training_client.create_project(name="Lighter Detection")

print(project.id)
