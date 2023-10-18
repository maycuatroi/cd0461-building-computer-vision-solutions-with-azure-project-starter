from time import sleep

from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from msrest.authentication import ApiKeyCredentials

from starter.sample_submission.src.config import CustomVisionConfig

training_client = CustomVisionTrainingClient(
    endpoint=CustomVisionConfig.ENDPOINT,
    credentials=ApiKeyCredentials(in_headers={"Training-key": CustomVisionConfig.KEY})
)

# Created project "Lighter Detection" (lighter-detection)
project = training_client.get_project(project_id=CustomVisionConfig.PROJECT_ID)

# start training
iteration = training_client.train_project(project.id)
print("Training...")
while (iteration.status != "Completed"):
    iteration = training_client.get_iteration(project.id, iteration.id)
    print("Training status: " + iteration.status)
    print("Waiting 10 seconds...")
    sleep(10)
