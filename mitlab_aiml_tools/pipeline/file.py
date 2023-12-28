import requests
from .utils.config import config
from .utils.tools import format_actor_string
from ..auth.credential import authenticated_only
from ..auth.credential import CredentialServer


MODULE_NAME = 'file_operation'

ALLOWED_TYPE_DICT = {
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
    """
        Handling the upload and download function for the file server

        Attributes:
            file_type (str): the type of the file
            (Allowed types: original_dataset, training_dataset, preprocessing_pipeline, preprocessing_logs, preprocessing_image, training_pipeline, training_logs, training_image, mode)

    """

    def __init__(self, credential_manager: CredentialServer, file_type: str):
        """
            Initialization for the File Utility

            Args:
                credential_manager (class): credential server to manage authenticate
                file_type (str): file type
        """
        self.credential_manager = credential_manager
        self.file_type = self._validate_file_type(file_type)

    def _validate_file_type(self, value: str):
        """
            Validate whether the file type is legal or not

            Args:
                value (str): the value the need to validate

            Returns:
                (Success): <File Type String>
                (Failed): Raise Value Error

        """
        if value not in ALLOWED_TYPE_DICT.keys():
            raise ValueError(
                f"Invalid value for 'file_type'. Allowed types are {', '.join(ALLOWED_TYPE_DICT.keys())}")
        else:
            return value

    @authenticated_only
    def upload(self, uid: str, file: None):
        """
            Upload file to file server

            Args:
                uid (str): the UID value for the file
                file (file): the file that needed to upload

            Returns:
                (Success) : "File uploaded successfully"
                (Failed) : "File uploaded failed"
                (Exception): <Error Message>

        """
        DEFAULT_HEADER = {"Uid": str(uid)}
        try:
            formatted_actor_string = format_actor_string(self.file_type)
            response = requests.post(
                url=f"{config['FILE_SERVER_PROTOCAL']}://{config['FILE_SERVER_HOST']}:{config['FILE_SERVER_PORT']}/{config['FILE_SERVER_API_PREFIX']}/{config['FILE_SERVER_API_VERSION']}/{MODULE_NAME}/{formatted_actor_string}FileManager/upload",
                headers=DEFAULT_HEADER,
                files=file
            )
            if response.status_code == 200:
                return "File uploaded successfully"
            else:
                return "File uploaded failed"
        except Exception as e:
            return str(e)

    @authenticated_only
    def download(self, uid: str):
        """
            Download file from file server

            Args:
                uid (str): the UID value for the file

            Returns:
                (Success):  <File>
                (Failed): "File downloaded failed"
                (Exception): <Error Message>
        """
        DEFAULT_HEADER = {"Content-Type": "application/json"}
        try:
            formatted_actor_string = format_actor_string(self.file_type)
            response = requests.post(
                url=f"{config['FILE_SERVER_PROTOCAL']}://{config['FILE_SERVER_HOST']}:{config['FILE_SERVER_PORT']}/{config['FILE_SERVER_API_PREFIX']}/{config['FILE_SERVER_API_VERSION']}/{MODULE_NAME}/{formatted_actor_string}FileManager/download",
                headers=DEFAULT_HEADER,
                json={f"{self.file_type}_uid": uid}
            )
            if response.status_code == 200:
                return response
            else:
                return "File downloaded failed"
        except Exception as e:
            return str(e)
