class FormRecognize:
    ENDPOINT = 'https://myformrecognition111.cognitiveservices.azure.com/'
    KEY = 'fcc4d0970bb44347849942711567bcd2'
    KEY2 = 'd7a5a5025620413dadb93de36f996f9c'
    MODEL_ID = 'boarding-pass-extract'


class BlobStorage:
    VIDEO_CONTAINER_NAME = 'videos'
    ACCOUNT_NAME = 'mystorage231047'
    ACCOUNT_KEY = 'HcyiVodGOHF1IWkCJmqeg5NkPW48pnAoyToYO19MiylQkcatWfJNOk5ToGjeZ7cpRwhvfo6CdeV3+AStZa2Uig=='
    SUBSCRIPTION_KEY = 'e144b1f9-a885-4518-b6ed-b2f3026e2a17'
    CONNECTION_STRING = f"DefaultEndpointsProtocol=https;AccountName={ACCOUNT_NAME};AccountKey={ACCOUNT_KEY};EndpointSuffix=core.windows.net"
    ENDPOINT = f"https://{ACCOUNT_NAME}.blob.core.windows.net"
    FORM_TRAINING_CONTAINER = 'form-training'
    TRAINING_DATA_URL = f"{ENDPOINT}/{FORM_TRAINING_CONTAINER}"
    LOCATION = 'trial'


class FaceService:
    KEY = '165143feffca4397af47abd105d509ae'
    ENDPOINT = 'https://face-detection-1-abcdas.cognitiveservices.azure.com/'
    PERSON_GROUP_ID = 'board-pass'


class CustomVisionConfig:
    PREDICT_KEY = 'e475682707614191848db74b98fb7051'
    TRAINING_RESOURCE_ID = '/subscriptions/21c53bc7-9f96-4753-9901-99cd641ad4e7/resourceGroups/aind-242944/providers/Microsoft.CognitiveServices/accounts/lighter-detection'
    PREDICT_RESOURCE_ID = '/subscriptions/21c53bc7-9f96-4753-9901-99cd641ad4e7/resourceGroups/aind-242944/providers/Microsoft.CognitiveServices/accounts/lighter-detection-detector'
    ITERATION_NAME = 'Iteration 1'
    KEY = 'c45f95a54214464ea8027aa3e40a6150'
    ENDPOINT = 'https://southcentralus.api.cognitive.microsoft.com/'
    PROJECT_ID = '567ba203-c82b-4adb-b7f7-3a7bf43b2099'
