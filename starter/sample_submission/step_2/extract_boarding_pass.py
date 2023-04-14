import requests
from azure.ai.formrecognizer import DocumentAnalysisClient, FormTrainingClient
from azure.core.credentials import AzureKeyCredential

from starter.sample_submission.src.config import FormRecognize

model_id=FormRecognize.MODEL_ID
# Set the API endpoint for the Form Recognizer ID's API
endpoint = f"{FormRecognize.ENDPOINT}"
# Set the subscription key for the Form Recognizer ID's API
subscription_key = FormRecognize.KEY
credential=AzureKeyCredential(subscription_key)
# Set the local path to the digital ID image
image_path = "../material_preparation_step/boarding_pass/boarding-avkash.pdf"
document_analysis_client = DocumentAnalysisClient(
    endpoint=endpoint, credential=credential
)


pdf_data = open(image_path, "rb").read()
poller = document_analysis_client.begin_analyze_document(model_id, document=pdf_data)

boarding_pass = poller.result()
document = boarding_pass.documents[0]
fields = document.fields
for field_name,field_value in fields.items():

        print(f'{field_name}: {field_value.content}')
        """
        ==>
        Carrier: UA
        From: San Francisco
        Gate: G1
        Boarding Time: 10:00 AM PST
        ticket numer: None
        To: Chicago
        Flight No: 234
        Seat: 20A
        Baggage: NO
        Passenger Name: Avkash Chauhan
        Class: E
        Date: April 20, 2022
        """