import requests
from azure.ai.formrecognizer import DocumentAnalysisClient, FormTrainingClient
from azure.core.credentials import AzureKeyCredential

from starter.sample_submission.src.config import FormRecognize

model_id = FormRecognize.MODEL_ID
# Set the API endpoint for the Form Recognizer ID's API
endpoint = f"{FormRecognize.ENDPOINT}"
# Set the subscription key for the Form Recognizer ID's API
subscription_key = FormRecognize.KEY
credential = AzureKeyCredential(subscription_key)
# Set the local path to the digital ID image
image_path = "../material_preparation_step/boarding_pass/boarding-avkash.pdf"
document_analysis_client = DocumentAnalysisClient(
    endpoint=endpoint, credential=credential
)

pdf_data = open(image_path, "rb").read()
# poller = document_analysis_client.begin_analyze_document(model_id, document=pdf_data)

poller = document_analysis_client.begin_analyze_document("prebuilt-document", pdf_data)
result = poller.result()

print("----Key-value pairs found in document----")
for kv_pair in result.key_value_pairs:
    if kv_pair.key and kv_pair.value:
        print("Key '{}': Value: '{}'".format(kv_pair.key.content, kv_pair.value.content))
    else:
        print("Key '{}': Value:".format(kv_pair.key.content))

print("----------------------------------------")