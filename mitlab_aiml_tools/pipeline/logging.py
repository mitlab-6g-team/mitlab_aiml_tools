from ..auth.credential import authenticated_only
from ..auth.credential import CredentialServer


class LogsConverter:
    """
        Handling the conversion of string to logs file and upload logs file to file server

        Attributes:
            credential_manager (class): credential manager for authenticatication
            log_file_path (str): the logs file_path

        Args: 
            input_string (str): the input strining need to convert to logs file
    """

    def __init__(self, credential_manager: CredentialServer, log_file_path: str):
        """
            Initialization for the Logs Converter

        Args:
            credential_manager (class): credential manager for authenticatication
            log_file_path(str): the logs file_path
        """
        self.credential_manager = credential_manager
        self.log_file_path = log_file_path

    @authenticated_only
    def covert(self, input_string):
        """
            Compress all the file in the folder

            Args:
                input_string (str): the input strining need to convert to logs file

            Returns:
                (Success): "Convert successfully"
                (Exception): <Error Message>  
        """
        try:
            with open(self.log_file_path, 'a+') as log_file:
                log_file.write(input_string + '\n')
            return "Convert successfully"
        except Exception as error:
            return str(error)

    @authenticated_only
    def _upload(self, uid, file):
        try:
            # TODO: Finish the logs file upload feature
            pass
        except Exception as error:
            return str(error)
