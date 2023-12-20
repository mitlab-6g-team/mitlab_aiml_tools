import requests
from .utils.config import config
from .utils.tools import format_actor_string


DEFAULT_HEADER = {"Content-Type": "application/json"}
MODULE_NAME = 'file_operation'

TYPE_DICT = {
    'original_dataset': 'OriginalDataset',
    'training_dataset': "TrainingDataset",
    'preprocessing_pipeline': "PreprocessingPipeline",
    'preprocessing_logs': "PreprocessingLogs",
    'preprocessing_image': "PreprocessingImage",
    'training_pipeline': "TrainingPipeline",
    'training_logs': "TrainingLogs",
    'training_image': "TrainingImage",
    'model': "Model",
}


class FileUtility:

    def __init__(self, actor_type):
        self.actor_type = actor_type

    def upload(self, uid: str, file=None):
        """
            Upload file to file server
        """
        DEFAULT_HEADER = {"Uid": str(uid)}
        try:
            formatted_actor_string = format_actor_string(self.actor_type)
            response = requests.post(
                url=f"{config['FILE_SERVER_PROTOCAL']}://{config['FILE_SERVER_HOST']}:{config['FILE_SERVER_PORT']}/{config['FILE_SERVER_API_PREFIX']}/{config['FILE_SERVER_API_VERSION']}/{MODULE_NAME}/{formatted_actor_string}FileManager/upload",
                headers=DEFAULT_HEADER,
                files=file
            )
            return response
        except Exception as e:
            return str(e)

    def download(self, uid: str):
        """
            Download file from file server
        """
        DEFAULT_HEADER = {"Content-Type": "application/json"}
        try:
            formatted_actor_string = format_actor_string(self.actor_type)
            response = requests.post(
                url=f"{config['FILE_SERVER_PROTOCAL']}://{config['FILE_SERVER_HOST']}:{config['FILE_SERVER_PORT']}/{config['FILE_SERVER_API_PREFIX']}/{config['FILE_SERVER_API_VERSION']}/{MODULE_NAME}/{formatted_actor_string}FileManager/download",
                headers=DEFAULT_HEADER,
                json={f"{self.actor_type}_uid": uid}
            )
            return response
        except Exception as e:
            return str(e)
