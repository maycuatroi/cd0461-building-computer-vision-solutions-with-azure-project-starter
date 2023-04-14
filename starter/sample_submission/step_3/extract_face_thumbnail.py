import uuid

import cv2
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from starter.sample_submission.src import config
from starter.sample_submission.src.config import FaceService
seed= 42
# set uuid seed
uuid.seed = seed
# Set up the API endpoint and headers
face_client = FaceClient(FaceService.ENDPOINT, CognitiveServicesCredentials(FaceService.KEY))

video_blob_url = f"{config.BlobStorage.ENDPOINT}/videos/ab9fabbdd6a24a6abd1033757c2ca779avkash-boarding-pass.mp4?sp=r&st=2023-04-14T06:46:50Z&se=2023-04-14T14:46:50Z&spr=https&sv=2021-12-02&sr=b&sig=4Xaar7%2BmwPobWj8ZmJx%2FShI4ovHZR%2FTypzjDnWJbYDo%3D"


thumbnail_id =uuid.uuid4().hex

# get first frame of video
cap = cv2.VideoCapture(video_blob_url)
_,mat = cap.read()
cv2.imwrite(f'../material_preparation_step/thumbnails/{thumbnail_id}.jpg', mat)
# file : starter/sample_submission/material_preparation_step/thumbnails/4f7c6e013bec4ec887bb95adfa9e88fc.jpg