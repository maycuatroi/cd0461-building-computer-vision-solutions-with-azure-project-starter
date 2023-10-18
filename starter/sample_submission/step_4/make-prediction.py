from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials

from starter.sample_submission.src.config import CustomVisionConfig

client = CustomVisionPredictionClient(
    endpoint=CustomVisionConfig.ENDPOINT,
    credentials=ApiKeyCredentials(in_headers={"Prediction-key": CustomVisionConfig.PREDICT_KEY})
)

image_path = 'starter/lighter_test_images/lighter_test_set_4of5.jpg'

with open(image_path, mode="rb") as test_data:
    results = client.detect_image(
        project_id=CustomVisionConfig.PROJECT_ID,
        published_name=f'Public {CustomVisionConfig.ITERATION_NAME}',
        image_data=test_data
    )
    for prediction in results.predictions:
        print(f'{prediction.tag_name}: {prediction.probability * 100:.2f}%')
