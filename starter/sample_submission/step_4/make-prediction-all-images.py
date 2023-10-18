import os
from glob import glob

import cv2
from PIL import Image
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials

from starter.sample_submission.src.config import CustomVisionConfig

client = CustomVisionPredictionClient(
    endpoint=CustomVisionConfig.ENDPOINT,
    credentials=ApiKeyCredentials(in_headers={"Prediction-key": CustomVisionConfig.PREDICT_KEY})
)

image_paths = glob('starter/lighter_test_images/*')
threshold = 0.9
for i, image_path in enumerate(image_paths):
    mat = cv2.imread(image_path)
    with open(image_path, mode="rb") as test_data:
        results = client.detect_image(
            project_id=CustomVisionConfig.PROJECT_ID,
            published_name=f'Public {CustomVisionConfig.ITERATION_NAME}',
            image_data=test_data
        )
        for prediction in results.predictions:
            bbox = prediction.bounding_box
            # draw bounding box
            if prediction.probability > threshold:
                xmin, ymin = int(bbox.left * mat.shape[1]), int(bbox.top * mat.shape[0])
                xmax, ymax = int((bbox.left + bbox.width) * mat.shape[1]), int((bbox.top + bbox.height) * mat.shape[0])
                mat = cv2.rectangle(mat, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)
                mat = cv2.putText(mat, f'{prediction.tag_name}: {prediction.probability * 100:.2f}%', (xmin, ymin - 10),
                                  cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)
                print(f'{prediction.tag_name}: {prediction.probability * 100:.2f}%')
        img = Image.fromarray(cv2.cvtColor(mat,
                                           cv2.COLOR_BGR2RGB
                                           ))
        root = os.path.dirname(__file__)
        img.save(f'{root}/screenshots/{i}.jpg')
