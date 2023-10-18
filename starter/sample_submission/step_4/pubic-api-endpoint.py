from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from msrest.authentication import ApiKeyCredentials

from starter.sample_submission.src.config import CustomVisionConfig

client = CustomVisionTrainingClient(
    endpoint=CustomVisionConfig.ENDPOINT,
    credentials=ApiKeyCredentials(in_headers={"Training-key": CustomVisionConfig.KEY})
)

project = client.get_project(project_id=CustomVisionConfig.PROJECT_ID)

# get lastest iteration
iterations = client.get_iterations(project.id)
iteration = iterations[0]
print(iteration.id)

# publish iteration
# client.unpublish_iteration(project.id, iteration.id)
iteration = client.publish_iteration(project.id, iteration_id=iteration.id,
                                     publish_name=f'Public {CustomVisionConfig.ITERATION_NAME}',
                                     prediction_id=CustomVisionConfig.PREDICT_RESOURCE_ID)
print("Done!")
