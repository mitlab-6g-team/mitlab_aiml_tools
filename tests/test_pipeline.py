import unittest
from uuid import uuid4
from mitlab_aiml_tools.auth.credential import CredentialServer
from mitlab_aiml_tools.pipeline.file import FileUtility

### Test Input ###
FILE_TYPE = 'original_dataset'
##################


# Test data
# Credential server
CREDENTIAL_SERVER_HOST = '192.168.190.150'
CREDENTIAL_SERVER_PORT = '40678'
CREDENTIAL_ACCESS_KEY = 'test'
CREDENTIAL_SECRET_KEY = 'test12345'
# Example
MODEL_PATH = 'test_model.zip'
MODEL_EXAMPLE_UID = '033ace30-0128-4fdc-a197-75ccb2e291f9'
ORIGINAL_DATASET_PATH = 'test_original_dataset.zip'
ORIGINAL_DATASET_EXAMPLE_UID = 'd42b4b1c-5b00-421b-b62b-cf83482ce714'

credential_server = CredentialServer(
    host=CREDENTIAL_SERVER_HOST,
    port=CREDENTIAL_SERVER_PORT,
    access_key=CREDENTIAL_ACCESS_KEY,
    secret_key=CREDENTIAL_SECRET_KEY
)

file_manager = FileUtility(credential_manager=credential_server)


class TestFileUtility(unittest.TestCase):
    TEST_CONFIG = {"EXAMPLE_UID": ORIGINAL_DATASET_EXAMPLE_UID, "PATH": ORIGINAL_DATASET_PATH} if FILE_TYPE == 'original_dataset' else {
        "EXAMPLE_UID": MODEL_EXAMPLE_UID, "PATH": MODEL_PATH}

    def test_download(self):
        downloaded_response = file_manager.download(
            file_type=FILE_TYPE, uid=self.TEST_CONFIG['EXAMPLE_UID']
        )
        with open(self.TEST_CONFIG['PATH'], 'wb') as file:
            if downloaded_response.ok:
                file.write(downloaded_response.content)
            else:
                print("File downloaded failed")

    def test_upload(self):
        with open(self.TEST_CONFIG['PATH'], 'rb') as file:
            files = {f'{FILE_TYPE}_file': (self.TEST_CONFIG['PATH'], file)}
            file_manager.upload(
                file_type=FILE_TYPE,
                uid=uuid4(),
                file=files,
            )


if __name__ == '__main__':
    unittest.main()
