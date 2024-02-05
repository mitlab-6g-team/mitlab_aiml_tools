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
            credential_manager (class): credential manager for authenticatication
            protocal (str): the protocal of file server
            host (str): the host of file server
            port (str): the port of file server
            api_prefix (str): the api prefix of file server
            api_version (str): the api version of file server

        Args: 
            file_type (str): the type of the file
            uid (str): the UID value for the file
            file (file): the file that needed to upload
    """

    def __init__(self,
                 credential_manager: CredentialServer,
                 protocal=config['FILE_SERVER_PROTOCAL'],
                 host=config['FILE_SERVER_HOST'],
                 port=config['FILE_SERVER_PORT'],
                 api_prefix=config['FILE_SERVER_API_PREFIX'],
                 api_version=config['FILE_SERVER_API_VERSION'],
                 ):
        """
            Initialization for the File Utility

            Args:
                credential_manager (class): credential manager for authenticatication
                protocal (str): the protocal of file server
                host (str): the host of file server
                port (str): the port of file server
                api_prefix (str): the api prefix of file server
                api_version (str): the api version of file server
        """
        self.credential_manager = credential_manager if credential_manager is not None else ValueError(
            "credential_manager cannot be empty")
        self.protocal = protocal if protocal is not None else ValueError(
            "protocal cannot be empty")
        self.host = host if host is not None else (
            "host cannot be empty")
        self.port = port if port is not None else ValueError(
            "port cannot be empty")
        self.api_prefix = api_prefix if protocal is not None else ValueError(
            "api_prefix cannot be empty")
        self.api_version = api_version if protocal is not None else ValueError(
            "api_version cannot be empty")

    def _validate_file_type(self, value: str):
        """
            Validate whether the file type is legal or not

            Args:
                value (str): the value the need to validate
                (Allowed values: original_dataset, training_dataset, preprocessing_pipeline, preprocessing_logs, preprocessing_image, training_pipeline, training_logs, training_image, mode)

            Returns:
                (Success): <File Type String>
                (Failed): Raise Value Error

        """
        if value not in ALLOWED_TYPE_DICT.keys():
            raise ValueError(
                f"Invalid value for 'file_type'. Allowed types are {', '.join(ALLOWED_TYPE_DICT.keys())}")
        else:
            return value

    def _select_file_extension(self, value):
        """
            select file extension for uploading file and downloading file

            Args:
                value (str): the value the need to validate
                (Allowed values: original_dataset, training_dataset, preprocessing_pipeline, preprocessing_logs, preprocessing_image, training_pipeline, training_logs, training_image, model)

            Returns:
                (Success): <File Name String>
                (Failed): Raise Value Error
        """
        if value in ['original_dataset', 'training_dataset']:
            return config['DATASET_FILE_EXTENSION']
        elif value in ['preprocessing_pipeline', 'training_pipeline']:
            return config['PIPELINE_FILE_EXTENSION']
        elif value in ['preprocessing_logs', 'training_logs']:
            return config['LOGS_FILE_EXTENSION']
        elif value in ['preprocessing_image', 'training_image']:
            return config['IMAGE_FILE_EXTENSION']
        elif value in ['model']:
            return config['MODEL_FILE_EXTENSION']

    @authenticated_only
    def upload(self, file_type: str, uid: str, file: None):
        """
            Upload file to mitlab file server

            Args:
                file_type (str): the type of the file
                uid (str): the UID value for the file
                file (file): the file that needed to upload

            Returns:
                (Success) : "File uploaded successfully"
                (Failed) : "File uploaded failed"
                (Exception): <Error Message>

        """
        try:
            file_type = self._validate_file_type(file_type)
            file_extension = self._select_file_extension(file_type)
            formatted_actor_string = format_actor_string(file_type)
            response = requests.post(
                url=f"{self.protocal}://{self.host}:{self.port}/{self.api_prefix}/{self.api_version}/{MODULE_NAME}/{formatted_actor_string}FileManager/upload",
                headers={"Uid": f"{str(uid)}.{file_extension}"},
                files=file
            )
            if response.status_code == 200:
                return "File upload successfully"
            else:
                return "File upload failed"
        except Exception as e:
            return str(e)

    @authenticated_only
    def download(self, file_type: str, uid: str):
        """
            Download file from mitlab file server

            Args:
                file_type (str): the type of the file
                uid (str): the UID value for the file

            Returns:
                (Success):  <File>
                (Failed): "File downloaded failed"
                (Exception): <Error Message>
        """
        DEFAULT_HEADER = {"Content-Type": "application/json"}
        try:
            file_type = self._validate_file_type(file_type)
            file_extension = self._select_file_extension(file_type)
            formatted_actor_string = format_actor_string(file_type)
            response = requests.post(
                url=f"{self.protocal}://{self.host}:{self.port}/{self.api_prefix}/{self.api_version}/{MODULE_NAME}/{formatted_actor_string}FileManager/download",
                headers=DEFAULT_HEADER,
                json={f"{file_type}_uid": f"{uid}.{file_extension}"}
            )
            if response.status_code == 200:
                return response.content
            else:
                return "File download failed"
        except Exception as e:
            return str(e)
