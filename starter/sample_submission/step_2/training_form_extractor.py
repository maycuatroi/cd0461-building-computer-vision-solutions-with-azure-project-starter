from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import FormTrainingClient

from starter.sample_submission.src import config
from starter.sample_submission.src.config import FormRecognize

AZURE_FORM_RECOGNIZER_ENDPOINT = FormRecognize.ENDPOINT
AZURE_FORM_RECOGNIZER_KEY = FormRecognize.KEY

endpoint = AZURE_FORM_RECOGNIZER_ENDPOINT
key = AZURE_FORM_RECOGNIZER_KEY

form_training_client = FormTrainingClient(endpoint=endpoint, credential=AzureKeyCredential(key))
saved_model_list = form_training_client.list_custom_models()
trainingDataUrl = config.BlobStorage.TRAINING_DATA_URL

training_process = form_training_client.begin_training(trainingDataUrl, use_training_labels=False)
custom_model = training_process.result()

print(custom_model)

print(f"Custom Model ID's: {custom_model.model_id}")
print(f"Custom Model status: {custom_model.status}")