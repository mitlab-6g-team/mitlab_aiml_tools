import requests
from .utils.config import config
from ..auth.credential import authenticated_only
from ..auth.credential import CredentialServer


MODULE_NAME = 'pipeline_operation'

ALLOWED_TYPE_DICT = {
    'original_dataset': 'OriginalDataset',
    'training_dataset': "TrainingDataset",
    'preprocessing_pipeline': "PreprocessingPipeline",
    'preprocessing_log': "PreprocessingLogs",
    'preprocessing_image': "PreprocessingImage",
    'training_pipeline': "TrainingPipeline",
    'training_log': "TrainingLogs",
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

    def _validate_file_type(self, type: str):
        """
            Validate whether the file type is legal or not

            Args:
                value (str): the value the need to validate
                (allowed values: original_dataset, training_dataset , model)

            Returns:
                (Success): <File Type String>
                (Failed): Raise Value Error

        """

        allow_type=['model','dataset']

        if type not in allow_type:
            return False , f"invalid file_type, allowed types are {', '.join(ALLOWED_TYPE_DICT.keys())}"
        return True , "great"

    def _validate_type(self, value, expect_type):
        """
        Validate the type of a given value.

        Args:
            value: The value to check.
            expect_type: The type that value is expected to be.
        
        Returns:
            bool: True if the value matches the expected type.

        Raises:
            TypeError: If the value does not match the expected type.
            ValueError: If value or expect_type is None.
        """


        if expect_type is None or not isinstance(expect_type, type):
            raise TypeError("Expected a valid type for 'expect_type', but got None or an invalid type.")

        if value is None:
            raise ValueError("The value cannot be None.")

        if isinstance(value, expect_type):
            return True
        else:
            raise TypeError(f"Expected type {expect_type.__name__}, but got type {type(value).__name__}")

    @authenticated_only
    def upload(self, file_type:str ,file_path:str, file=None):
        """
        Upload file to mitlab file server.

        Args:
            file_type (str): The type of the file.
            file (file): The file that needs to be uploaded.

        Returns:
            str: "File uploaded successfully" on success.
            str: "File upload failed" on failure.
            str: <Error Message> on exception.
        """
        
        try:
            # Validate the file type
            is_success, return_message = self._validate_file_type(file_type)
            
            if not is_success:
                raise ValueError(return_message)
            
            # Construct the upload URL
            url = f"{self.protocal}://{self.host}:{self.port}/{self.api_prefix}/{self.api_version}/{MODULE_NAME}/GeneralFileManager/upload"
            
            # Perform the file upload
            response = requests.post(url=url, files=file , data={"file_path":file_path})

            # Check response status
            if response.status_code == 200:
                print("great2")
                return "File uploaded successfully"
            else:
                print("upload fail")
                return "File upload failed"
        except Exception as e:
            return str(e)

    @authenticated_only
    def download(self, file_type:str,**kwargs):
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
        default_header = {"Content-Type": "application/json"}

        try:
            is_success, return_message = self._validate_file_type(file_type)
            if not is_success:
                raise ValueError(return_message)
            
            for key, value in kwargs.items():
                self._validate_type(value, str)

            
            urls=f"{self.protocal}://{self.host}:{self.port}/{self.api_prefix}/{self.api_version}/{MODULE_NAME}/{'AuthFileManager' if file_type == 'model' else 'GeneralFileManager'}/download"
            request={}
            if file_type == "model" :
                request["model_uid"] = kwargs.get("model_uid")
                request["model_access_token"] = kwargs.get("model_access_token")
            elif file_type == "dataset":
                request["file_path"] = kwargs.get("file_path")

            if not all(request.values()):
                raise ValueError("Missing required parameters for the file type.")

            response = requests.post(
                url=urls,
                headers=default_header,
                json=request
            )
            return response
        except Exception as e:
            return str(e)
