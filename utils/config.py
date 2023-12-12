import os
from dotenv import load_dotenv

load_dotenv('../../.env')


config = {
    "FILE_SERVER_PROTOCAL": os.getenv("FILE_SERVER_PROTOCAL"),
    "FILE_SERVER_HOST": os.getenv("FILE_SERVER_HOST"),
    "FILE_SERVER_PORT": os.getenv("FILE_SERVER_PORT"),
    "FILE_SERVER_API_PREFIX": os.getenv("FILE_SERVER_API_PREFIX"),
    "FILE_SERVER_API_VERSION": os.getenv("FILE_SERVER_API_VERSION"),
}
