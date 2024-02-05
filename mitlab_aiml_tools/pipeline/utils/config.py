import base64

config = {
    "FILE_SERVER_PROTOCAL": 'http',
    "FILE_SERVER_HOST": base64.b64decode('MTQwLjExOC4yLjUy').decode('utf-8'),
    "FILE_SERVER_PORT": base64.b64decode('MzUwMDY=').decode('utf-8'),
    "FILE_SERVER_API_PREFIX": 'api',
    "FILE_SERVER_API_VERSION": 'v0.1',

    "DATASET_FILE_EXTENSION": "tar.gz",
    "PIPELINE_FILE_EXTENSION": "py",
    "IMAGE_FILE_EXTENSION": "",
    "LOGS_FILE_EXTENSION": "txt",
    "MODEL_FILE_EXTENSION": "tar.gz"
}
