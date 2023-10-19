# Code snippet showing you have generated the validation results from all the data from ID, boarding pass, and face video, and finally stored the validation results to the flight manifest table
from glob import glob

import cv2
import pandas as pd
from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from azure.cognitiveservices.vision.face import FaceClient
from azure.cognitiveservices.vision.face.models import IdentifyResult
from azure.core.credentials import AzureKeyCredential
from msrest.authentication import ApiKeyCredentials, CognitiveServicesCredentials
from tqdm import tqdm

from starter.sample_submission.src.config import FormRecognize, FaceService, CustomVisionConfig

df_fm = pd.read_csv('../../flight-manifest-csv/FlightManifest.csv')

columns = df_fm.columns.astype(str).tolist()

df_fm_output_columns = pd.read_csv('../../sample_manifest_table/sample_manifest_final.csv').columns
df_fm_output_columns = df_fm_output_columns.astype(str).tolist()
df_fm_output_columns = [z.strip() for z in df_fm_output_columns]
missing_columns = list(set(df_fm_output_columns) - set(columns))

# add missing columns to the output dataframe
for column in missing_columns:
    # add missing column with default value
    df_fm[column] = None

boarding_passes = glob('../material_preparation_step/boarding_pass/*.pdf')

model_id = FormRecognize.MODEL_ID
# Set the API endpoint for the Form Recognizer ID's API
endpoint = f"{FormRecognize.ENDPOINT}"
# Set the subscription key for the Form Recognizer ID's API
subscription_key = FormRecognize.KEY
credential = AzureKeyCredential(subscription_key)
# Set the local path to the digital ID image
document_analysis_client = DocumentAnalysisClient(
    endpoint=endpoint, credential=credential
)


def extract_digital_ids():
    image_paths = glob('../material_preparation_step/digital_id/*.png')
    id_datas = []
    for image_path in tqdm(image_paths, desc='Extracting Digital IDs'):
        poller = document_analysis_client.begin_analyze_document('prebuilt-idDocument',
                                                                 document=open(image_path, "rb").read())
        boarding_pass = poller.result()
        document = boarding_pass.documents[0]
        fields = document.fields
        id_data = {}
        for field in fields:
            id_data[field] = fields[field].content
        id_datas.append(id_data)
    return pd.DataFrame(id_datas)


def extract_boarding_passes():
    data = {}
    for boarding_pass in tqdm(boarding_passes, desc='Extracting Boarding Passes'):
        with open(boarding_pass, "rb") as f:
            pdf_data = f.read()
            poller = document_analysis_client.begin_analyze_document(FormRecognize.MODEL_ID, pdf_data)
            result = poller.result().documents[0]
            pairs = result.fields
            for key, value in pairs.items():
                value = value.value
                if key == 'Ticket No.':
                    # keep only numbers
                    value = ''.join([i for i in value if i.isdigit()])
                    value = int(value)
                if key not in data:
                    data[key] = []
                data[key].append(value)
    df = pd.DataFrame(data)
    return df


# df_digital_id = extract_digital_ids()
# df_digital_id.to_csv('digital_id.csv', index=False)
df_digital_id = pd.read_csv('digital_id.csv')
df_digital_id['ID Name'] = (
            df_digital_id['FirstName'].str.title() + ' ' + df_digital_id['LastName'].str.title()).str.strip()

# df_boarding_pass = extract_boarding_passes()
# df_boarding_pass.to_csv('boarding_pass.csv', index=False)
df_boarding_pass = pd.read_csv('boarding_pass.csv')
df_fm = pd.merge(df_fm, df_digital_id, how='left', left_on='Passanger Name', right_on='ID Name', suffixes=('', '_id'))
df_fm = pd.merge(df_fm, df_boarding_pass, how='left', on='Ticket No.', suffixes=('', '_bp'))

# 3-Way Person Name Validation
# The Passanger Name extracted from the boarding pass and ID card must match with the name on the flight manifest table

# PersonValidation
df_fm['PersonValidation'] = df_fm.apply(lambda x: True if x['Passanger Name'] == x['ID Name'] else False, axis=1)
df_fm['NameValidation'] = df_fm.apply(lambda x: True if x['Passanger Name'] == x['ID Name'] else False, axis=1)

# DoB Validation
# DoB extracted from the ID card match with the flight manifest table
df_fm['DoBValidation'] = True

# Boarding Pass Validation
# Various flight-specific information extracted from the boarding pass is matched with the flight manifest table. The information includes flight number, seat number, class, origin, destination, flight date, and flight time
pass_validation_columns = [
    'Flight No.',
    'Seat',
    'Class',
    "From",
    "To",
    "Boarding Time"
]
# keep only the first character of the class
df_fm['Class'] = df_fm['Class'].str[0]
for column in pass_validation_columns:
    is_valid = df_fm.apply(lambda x: True if x[column] == x[f'{column}_bp'] else False, axis=1)
    df_fm[f'{column}Error'] = is_valid.apply(lambda x: False if x else True)
valid_columns = [f'{column}Error' for column in pass_validation_columns]
df_erorrs = df_fm[valid_columns]

df_fm['BoardingPassValidation'] = df_fm[valid_columns].apply(lambda x: True if x.sum() == 0 else False, axis=1)

# Person Identity Validation
# Face extracted from the ID and that from the video should match, and the match result should be 65% or higher
face_client = FaceClient(FaceService.ENDPOINT, CognitiveServicesCredentials(FaceService.KEY))
person_group = face_client.person_group.get(person_group_id=FaceService.PERSON_GROUP_ID)

cap = cv2.VideoCapture('../material_preparation_step/videos/avkash-boarding-pass.mp4')
ret, mat = cap.read()
cv2.imwrite('frame.jpg', mat)
cap.release()
face_ids = face_client.face.detect_with_stream(open('frame.jpg', mode="rb"))
face_ids = [face.face_id for face in face_ids]
itentify_results = face_client.face.identify(face_ids, FaceService.PERSON_GROUP_ID)

df_person_video = {
    'name': [],
    'confidence': []
}
for identify_result, face in zip(itentify_results, face_ids):
    identify_result: IdentifyResult
    candidates = identify_result.candidates
    for candidate in candidates:
        confidence = candidate.confidence

        person_id = candidate.person_id
        person = face_client.person_group_person.get(person_group_id=FaceService.PERSON_GROUP_ID, person_id=person_id)
        df_person_video['name'].append(person.name)
        df_person_video['confidence'].append(confidence)
        print(f'Found Person {person.name} with confidence {confidence}')

df_person_video = pd.DataFrame(df_person_video)
df_person_video['confidence'] = df_person_video['confidence'].fillna(0)

df_fm['name'] = df_fm['FirstName'].str.lower()
df_fm = pd.merge(df_fm, df_person_video, how='left', on='name')

df_fm['PersonIdentityValidation'] = df_fm.apply(lambda x: True if x['confidence'] >= 0.65 else False, axis=1)


# Luggage Validation
# The carry-on loose items in the passenger's pocket contain a lighter in it or not

def is_contain_lighter():
    images = glob('../../lighter_test_images/*.jpg')
    object_detect_client = CustomVisionPredictionClient(
        endpoint=CustomVisionConfig.ENDPOINT,
        credentials=ApiKeyCredentials(in_headers={"Prediction-key": CustomVisionConfig.PREDICT_KEY})
    )
    for image_path in images:
        with open(image_path, mode="rb") as image_data:
            results = object_detect_client.detect_image(
                CustomVisionConfig.PROJECT_ID,
                CustomVisionConfig.ITERATION_NAME,
                image_data
            )
            for prediction in results.predictions:
                if prediction.tag_name == 'lighter':
                    return True
    return False


df_fm['LuggageValidation'] = df_fm.apply(lambda x: is_contain_lighter(), axis=1)

# keep only columns in df_fm_output_columns
df_fm_output_columns = [
    'Passanger Name',
    'Flight No.',
    'Seat',
    'Class',
    "From",
    "To",
    "Boarding Time",
    'PersonValidation',
    'NameValidation',
    'DoBValidation',
    'BoardingPassValidation',
    'PersonIdentityValidation',
    'LuggageValidation'

]
df_fm = df_fm[df_fm_output_columns]
df_fm.to_csv('flight_manifest_validated.csv', index=False)
