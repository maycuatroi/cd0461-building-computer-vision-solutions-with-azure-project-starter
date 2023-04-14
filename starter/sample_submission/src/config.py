


class FormRecognize:
    ENDPOINT = 'https://myformrecogniton231047.cognitiveservices.azure.com/'
    KEY = 'f043ad5a2d9a44e7bf6e9b9865791ac0'


class BlobStorage:
    ACCOUNT_NAME = 'mystorage231047'
    ACCOUNT_KEY = 'OqY40dmGJcV9XrOFHthZQcAtuBJWr9r8IxwBjQOy3wTvLZZoUe/6YHx6YAoN7FwE+72VI/wStP7d+AStSH93cw=='
    CONNECTION_STRING = f"DefaultEndpointsProtocol=https;AccountName={ACCOUNT_NAME};AccountKey={ACCOUNT_KEY};EndpointSuffix=core.windows.net"
    ENDPOINT = f"https://{ACCOUNT_NAME}.blob.core.windows.net"
    TRAINING_DATA_URL = f"{ENDPOINT}/training-data"