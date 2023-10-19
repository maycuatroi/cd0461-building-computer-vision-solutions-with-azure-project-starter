import os
import uuid

import cv2
from azure.cognitiveservices.vision.face import FaceClient
from azure.cognitiveservices.vision.face.models import DetectedFace, IdentifyResult
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
id_image_path = "../material_preparation_step/digital_id/ca-dl-avkash.png"
mat_id = cv2.imread(id_image_path)

# get first frame of video
cap = cv2.VideoCapture(video_sas_url)
_, mat = cap.read()
image_path = f'../material_preparation_step/thumbnails/{thumbnail_id}.jpg'
cv2.imwrite(image_path, mat)
person_group = face_client.person_group.get(person_group_id=FaceService.PERSON_GROUP_ID)

# Detect faces
face_ids = []
faces = face_client.face.detect_with_stream(open(image_path, mode="rb"))
for face in faces:
    face_ids.append(face.face_id)

# Identify faces
itentify_results = face_client.face.identify(face_ids, FaceService.PERSON_GROUP_ID)

for identify_result, face in zip(itentify_results, faces):
    identify_result: IdentifyResult
    candidates = identify_result.candidates
    for candidate in candidates:
        confidence = candidate.confidence * 100
        confidence = f'{confidence:.2f}%'
        person_id = candidate.person_id
        person = face_client.person_group_person.get(person_group_id=FaceService.PERSON_GROUP_ID, person_id=person_id)
        print(f'Found Person {person.name} with confidence {confidence}')
        # plot bounding box
        rect = face.face_rectangle

        cv2.rectangle(mat, (rect.left, rect.top), (rect.left + rect.width, rect.top + rect.height), (0, 255, 0), 2)
        cv2.putText(mat, f'{person.name} {confidence}', (rect.left, rect.top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9,
                    (36, 255, 12), 2)
cv2.imwrite(f'../material_preparation_step/thumbnails/{thumbnail_id}-with-bounding-box.jpg', mat)
cv2.imshow('image', mat)
cv2.waitKey(0)
