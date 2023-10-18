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
    PREDICT_KEY = 'e475682707614191848db74b98fb7051'
    TRAINING_RESOURCE_ID = '/subscriptions/21c53bc7-9f96-4753-9901-99cd641ad4e7/resourceGroups/aind-242944/providers/Microsoft.CognitiveServices/accounts/lighter-detection'
    PREDICT_RESOURCE_ID = '/subscriptions/21c53bc7-9f96-4753-9901-99cd641ad4e7/resourceGroups/aind-242944/providers/Microsoft.CognitiveServices/accounts/lighter-detection-detector'
    ITERATION_NAME = 'Iteration 1'
    KEY = 'c45f95a54214464ea8027aa3e40a6150'
    ENDPOINT = 'https://southcentralus.api.cognitive.microsoft.com/'
    PROJECT_ID = '567ba203-c82b-4adb-b7f7-3a7bf43b2099'
