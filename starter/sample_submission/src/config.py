


class FormRecognize:
    ENDPOINT = 'https://myformrecogniton231047.cognitiveservices.azure.com/'
    KEY = 'f043ad5a2d9a44e7bf6e9b9865791ac0'
    MODEL_ID='boarding-pass-extract'


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
    KEY='818b9b86f1f64477b47b3a0bbb54982c'
    ENDPOINT='https://myfacerecognition231047.cognitiveservices.azure.com/'