import requests
from config import config


DEFAULT_HEADER = "application/json"


def download():
    """
        Download file from file server
    """
    try:
        requests.post(
            url=f"{config['FILE_SERVER_PROTOCAL']}//{config['FILE_SERVER_HOST']}:{config['FILE_SERVER_PORT']}/{config['FILE_SERVER_API_PREFIX']}/{config['FILE_SERVER_API_VERSION']}/",
            headers=DEFAULT_HEADER,
            json={}
        )
    except Exception as e:
        print(str(e))
        raise ConnectionError(e)
