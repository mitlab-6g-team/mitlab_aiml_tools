import requests
from utils.config import config


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


class FileUtility:
    def upload(file=None):
        """
            Upload file to file server
        """
        pass

    def download(type=None):
        """
            Download file from file server
        """
        try:
            response = requests.post(
                url=f"{config['FILE_SERVER_PROTOCAL']}//{config['FILE_SERVER_HOST']}:{config['FILE_SERVER_PORT']}/{config['FILE_SERVER_API_PREFIX']}/{config['FILE_SERVER_API_VERSION']}/{config['MODULE_NAME']}/{type}FileManager/download",
                headers=DEFAULT_HEADER,
                json={}
            )
        except Exception as e:
            print(str(e))
            raise ConnectionError(e)
