import requests
from config import config


def upload(logs_file):
    """
        Upload logs to file server
    """
    try:
        requests.post(
            url=f"{config['FILE_SERVER_PROTOCAL']}//{config['FILE_SERVER_HOST']}:{config['FILE_SERVER_PORT']}/{config['FILE_SERVER_API_PREFIX']}/{config['FILE_SERVER_API_VERSION']}/",
            files=logs_file
        )
    except Exception as e:
        print(str(e))
        raise ConnectionError(e)
