from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential
from starter.sample_submission.src.config import FormRecognize

# Set the API endpoint for the Form Recognizer ID's API
endpoint = FormRecognize.ENDPOINT
# Set the subscription key for the Form Recognizer ID's API
subscription_key = FormRecognize.KEY2
document_analysis_client = DocumentAnalysisClient(
    endpoint=endpoint, credential=AzureKeyCredential(subscription_key)
)
# Set the content type for the digital ID image
content_type = "image/jpeg"

# Set the local path to the digital ID image
image_path = "../material_preparation_step/digital_id/ca-dl-avkash.png"

# Read the binary data from the digital ID image
image_data = open(image_path, "rb").read()
poller = document_analysis_client.begin_analyze_document("prebuilt-idDocument", image_data)
digital_id = poller.result()
document = digital_id.documents[0]
fields = document.fields
for field_name, field_value in fields.items():
    print(f'{field_name}: {field_value.content}')

# Address: 1234 Circle Ave, Apt 123 San Mateo, CA, 94401
# CountryRegion: None
# DateOfBirth: 01/01/1990
# DateOfExpiration: 01/01/2025
# DateOfIssue: 08/08/2020
# DocumentNumber: D12345678
# Endorsements: NONE
# EyeColor: BLK
# FirstName: AVKASH CHAUHAN
# HairColor: BRN
# Height: 5'7"
# LastName: CHAUHAN
# Region: None
# Restrictions: SEXM
# VehicleClassifications: C
# Weight: 140 lbs


# screen shot: material_preparation_step/screenshots/step_2_1.PNG
