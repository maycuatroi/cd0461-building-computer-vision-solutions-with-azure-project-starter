class FormRecognize:
    ENDPOINT = 'https://myformrecognition1.cognitiveservices.azure.com/'
    KEY = 'ae9f24c06fc14da398a0e0a4636ef370'
    KEY2 = 'ca0d8f24d59a49eebd412ce5193baa7a'
    MODEL_ID = 'boarding-pass-extract'


class BlobStorage:
    CONTAINER_NAME = 'videos'
    ACCOUNT_NAME = 'mystorage231047'
    ACCOUNT_KEY = 'vQroVsyMoAMlfwD6QrKYXzPFXb91BnG484lUKFdMH4pMM9AMo1yGfzrNYg1mkrYaLlOvJaifoA8b+AStZnOi6A=='
    SUBSCRIPTION_KEY = 'e144b1f9-a885-4518-b6ed-b2f3026e2a17'
    CONNECTION_STRING = f"DefaultEndpointsProtocol=https;AccountName={ACCOUNT_NAME};AccountKey={ACCOUNT_KEY};EndpointSuffix=core.windows.net"
    ENDPOINT = f"https://{ACCOUNT_NAME}.blob.core.windows.net"
    TRAINING_DATA_URL = f"{ENDPOINT}/training-data"
    LOCATION = 'trial'


class FaceService:
    KEY = '818b9b86f1f64477b47b3a0bbb54982c'
    ENDPOINT = 'https://myfacerecognition231047.cognitiveservices.azure.com/'


class CustomVisionConfig:
    KEY = '366bffb028e54c1dbc7a285ebc4bba75'
    ENDPOINT = 'https://mycustomvision231047.cognitiveservices.azure.com/'
    ENDPOINT = 'https://southcentralus.api.cognitive.microsoft.com/'
    PROJECT_ID = 'a965da96-e73e-4bf7-8eac-a32442589679'
