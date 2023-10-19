import time

from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials

from starter.sample_submission.src.config import FaceService

face_client = FaceClient(FaceService.ENDPOINT, CognitiveServicesCredentials(FaceService.KEY))

person_group_id = FaceService.PERSON_GROUP_ID
person_group = face_client.person_group.get(person_group_id=person_group_id)
face_client.person_group.train(person_group_id)
training_status = face_client.person_group.get_training_status(person_group_id=person_group.person_group_id)
while training_status.status != 'succeeded':
    training_status = face_client.person_group.get_training_status(person_group_id=person_group_id)
    print(f'Training status: {training_status.status}')
    time.sleep(5)
