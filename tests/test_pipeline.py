import unittest
from uuid import uuid4
from mitlab_aiml_tools.auth.credential import CredentialServer
from mitlab_aiml_tools.pipeline.file import FileUtility

### Test Input ###
FILE_TYPE = 'original_dataset'
##################


######################## Credential server ########################
CREDENTIAL_SERVER_HOST = '140.118.122.164'
CREDENTIAL_SERVER_PORT = '34801'
CREDENTIAL_ACCESS_KEY = 'user_1'
CREDENTIAL_SECRET_KEY = 'test'
PROTOCAL=False
API_PREFIX='entrypoint'
API_VERSION='v1.1.1'

############################ fake data ############################
file_type="dataset"
file_path="1fceb3f6-275f-4070-bfb6-3be85160c5fc/3f916f7e-dac9-4fb5-8152-939c86ada8da/original/c3cf30f8-ab25-422f-a5a7-0eb1c1dc9ee9.zip"


credential_server = CredentialServer(
    host=CREDENTIAL_SERVER_HOST,
    port=CREDENTIAL_SERVER_PORT,
    access_key=CREDENTIAL_ACCESS_KEY,
    secret_key=CREDENTIAL_SECRET_KEY
)

file_manager = FileUtility(credential_manager=credential_server)


class TestFileUtility(unittest.TestCase):
    def test_download(self):
        downloaded_response = file_manager.download(
            file_type=file_type, file_path=file_path
        )
        with open("dataset/original_dataset.csv", 'wb') as file:
            if downloaded_response.ok:
                file.write(downloaded_response.content)
            else:
                print("File downloaded failed")

    # def test_upload(self):
    #     with open(self.TEST_CONFIG['PATH'], 'rb') as file:
    #         files = {f'{FILE_TYPE}_file': (self.TEST_CONFIG['PATH'], file)}
    #         file_manager.upload(
    #             file_type=FILE_TYPE,
    #             uid=uuid4(),
    #             file=files,
    #         )


if __name__ == '__main__':
    unittest.main()
