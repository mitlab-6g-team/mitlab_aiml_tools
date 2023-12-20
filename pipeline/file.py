import requests
from utils.config import config
from utils.tools import format_actor_string

DEFAULT_HEADER = "application/json"
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

print(MODULE_NAME)


class FileUtility:

    def __init__(self, actor_type, file, uid_value) -> None:
        self.actor_type = actor_type
        self.file = file
        self.uid_value = uid_value

    def upload(self):
        """
            Upload file to file server
        """
        try:
            formatted_actor_type = format_actor_string(self.actor_type)
            response = requests.post(
                url=f"{config['FILE_SERVER_PROTOCAL']}//{config['FILE_SERVER_HOST']}:{config['FILE_SERVER_PORT']}/{config['FILE_SERVER_API_PREFIX']}/{config['FILE_SERVER_API_VERSION']}/{MODULE_NAME}/{formatted_actor_type}FileManager/upload",
                headers=DEFAULT_HEADER,
                files=self.file
            )
            print(response, response.json())
        except Exception as e:
            print(str(e))
            raise ConnectionError(e)

    def download(self):
        """
            Download file from file server
        """
        try:
            formatted_actor_type = format_actor_string(self.actor_type)
            response = requests.post(
                url=f"{config['FILE_SERVER_PROTOCAL']}//{config['FILE_SERVER_HOST']}:{config['FILE_SERVER_PORT']}/{config['FILE_SERVER_API_PREFIX']}/{config['FILE_SERVER_API_VERSION']}/{MODULE_NAME}/{formatted_actor_type}FileManager/download",
                headers=DEFAULT_HEADER,
                json={
                    f"{self.actor_type}_uid": self.uid_value
                }
            )
            print(response, response.json())
        except Exception as e:
            print(str(e))
            raise ConnectionError(e)
