import uuid

import cv2
from azure.cognitiveservices.vision.face import FaceClient
from azure.cognitiveservices.vision.face.models import DetectedFace
from azure.storage.blob import BlobServiceClient
from msrest.authentication import CognitiveServicesCredentials
from starter.sample_submission.src import config
from starter.sample_submission.src.config import FaceService
from starter.sample_submission.src.config import BlobStorage as BS

seed = 42
# set uuid seed
uuid.seed = seed
# Set up the API endpoint and headers
face_client = FaceClient(FaceService.ENDPOINT, CognitiveServicesCredentials(FaceService.KEY))

# video_blob_url = f"{config.BlobStorage.ENDPOINT}/videos/ab9fabbdd6a24a6abd1033757c2ca779avkash-boarding-pass.mp4?sp=r&st=2023-04-14T06:46:50Z&se=2023-04-14T14:46:50Z&spr=https&sv=2021-12-02&sr=b&sig=4Xaar7%2BmwPobWj8ZmJx%2FShI4ovHZR%2FTypzjDnWJbYDo%3D"
# get video blob url from blob storage
client: BlobServiceClient = BlobServiceClient.from_connection_string(BS.CONNECTION_STRING)
container_client = client.get_container_client(BS.VIDEO_CONTAINER_NAME)
video = container_client.get_blob_client('a474067d305d441cb167e5211cc7d181avkash-boarding-pass.mp4')
# get public url, downloadable url
video_sas_url = f'{video.url}?sp=r&st=2023-10-19T17:15:56Z&se=2023-10-20T01:15:56Z&spr=https&sv=2022-11-02&sr=b&sig=bdRG%2BNC1RVg%2BlXsaPQI3m0jT%2BTBEXJcMAexkcYKm2QQ%3D'
thumbnail_id = uuid.uuid4().hex

# get first frame of video
cap = cv2.VideoCapture(video_sas_url)
_, mat = cap.read()
image_path = f'../material_preparation_step/thumbnails/{thumbnail_id}.jpg'
cv2.imwrite(image_path, mat)
results = face_client.face.detect_with_stream(open(image_path, mode="rb"), detection_model='detection_03')

for detected_face in results:
    detected_face: DetectedFace
    bbox = detected_face.face_rectangle
    # draw bounding box
    xmin, ymin = int(bbox.left), int(bbox.top)
    xmax, ymax = int((bbox.left + bbox.width)), int((bbox.top + bbox.height))
    mat = cv2.rectangle(mat, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)
    mat = cv2.putText(mat, f'{detected_face.face_id}', (xmin, ymin - 10),
                      cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)
print(results)
cv2.imwrite(image_path, mat)
# file : starter/sample_submission/material_preparation_step/thumbnails/4f7c6e013bec4ec887bb95adfa9e88fc.jpg
