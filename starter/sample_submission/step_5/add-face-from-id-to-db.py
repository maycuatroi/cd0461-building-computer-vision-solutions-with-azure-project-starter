import os
from glob import glob

import pandas as pd
from azure.cognitiveservices.vision.face import FaceClient
from azure.cognitiveservices.vision.face.models import APIErrorException
from msrest.authentication import CognitiveServicesCredentials
from starter.sample_submission.src.config import FaceService

face_client = FaceClient(FaceService.ENDPOINT, CognitiveServicesCredentials(FaceService.KEY))

person_group_id = FaceService.PERSON_GROUP_ID
is_person_group_exist = face_client.person_group.get(person_group_id=person_group_id)
if not is_person_group_exist:
    face_client.person_group.create(person_group_id=person_group_id, name=person_group_id)

id_folder = '../material_preparation_step/digital_id'
person_images = glob(f'{id_folder}/*.png')
person_data = {
    'name': [],
    'id': []
}
for image_path in person_images:
    person_name = os.path.basename(image_path).split('.')[0]
    person_data['name'].append(person_name)
    person = face_client.person_group_person.create(person_group_id=person_group_id, name=person_name)
    person_data['id'].append(person.person_id)
df = pd.DataFrame(person_data)
df.to_csv('person_data.csv', index=False)

for person_name, person_id in df[['name', 'id']].values:
    id_image_path = f'../material_preparation_step/digital_id/{person_name}.png'
    res = face_client.person_group_person.add_face_from_stream(person_group_id=person_group_id, person_id=person_id,
                                                                   image=open(id_image_path, mode="rb"))
    print(res)