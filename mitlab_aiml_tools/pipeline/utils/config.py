import base64

config = {
    "FILE_SERVER_PROTOCAL": 'http',
    "FILE_SERVER_HOST": base64.b64decode('MTQwLjExOC4xMjIuMTY0').decode('utf-8'),
    "FILE_SERVER_PORT": base64.b64decode('MzQ5MDQ=').decode('utf-8'),
    "FILE_SERVER_API_PREFIX": 'api',
    "FILE_SERVER_API_VERSION": 'v0.1',

    "ENTRY_SEVER_PROTCAL": 'http',
    "ENTRY_SEVER_HOST": '',
    "ENTRY_SEVER_PORT": '',
    "ENTRY_SEVER_API_PREFIX": '',
    "ENTRY_SEVER_API_VERSION": '',

    "DATASET_FILE_EXTENSION": "zip",
    "PIPELINE_FILE_EXTENSION": "py",
    "IMAGE_FILE_EXTENSION": "",
    "LOG_FILE_EXTENSION": "txt",
    "MODEL_FILE_EXTENSION": "zip"
}
