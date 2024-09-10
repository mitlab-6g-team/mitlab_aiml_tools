import unittest
from uuid import uuid4
from mitlab_aiml_tools.auth.credential import CredentialServer
from mitlab_aiml_tools.pipeline.file import FileUtility


######################## Credential server ########################
CREDENTIAL_SERVER_HOST = '140.118.122.164'
CREDENTIAL_SERVER_PORT = '34801'
CREDENTIAL_ACCESS_KEY = 'user1'
CREDENTIAL_SECRET_KEY = 'test'
# PROTOCAL='http'
# API_PREFIX='entrypoint'
# API_VERSION='v1.1.1'

######################## data server ########################
DATA_SERVER_HOST = '140.118.122.164'
DATA_SERVER_PORT = '34804'
PROTOCAL='http'
API_PREFIX='api'
API_VERSION='v1.1.1'

############################ fake data ############################
file_type="dataset"
download_uid="1fceb3f6-275f-4070-bfb6-3be85160c5fc/3f916f7e-dac9-4fb5-8152-939c86ada8da/original/c3cf30f8-ab25-422f-a5a7-0eb1c1dc9ee9.zip"
upload_path="tests/dataset/training_dataset.zip"
upload_uid="1fceb3f6-275f-4070-bfb6-3be85160c5fc/3f916f7e-dac9-4fb5-8152-939c86ada8da/training/1d139a71-6111-47a8-84f4-918cea1991cc.zip"

model_uid=""
model_access_token=""

credential_server = CredentialServer(
    host=CREDENTIAL_SERVER_HOST,
    port=CREDENTIAL_SERVER_PORT,
    access_key=CREDENTIAL_ACCESS_KEY,
    secret_key=CREDENTIAL_SECRET_KEY
)

file_manager = FileUtility(
        credential_manager=credential_server,
        host=DATA_SERVER_HOST,
        port=DATA_SERVER_PORT,
        protocal=PROTOCAL,
        api_prefix=API_PREFIX,
        api_version=API_VERSION
    )


class TestFileUtility(unittest.TestCase):
    # def test_download(self):
    #     downloaded_response = file_manager.download(file_type=file_type, file_path=file_path)
        
    #     with open("tests/dataset/original_dataset.zip", 'wb') as file:
    #         print(downloaded_response)
    #         if downloaded_response.ok:
    #             file.write(downloaded_response.content)
    #         else:
    #             print("File downloaded failed")

    def test_upload_model(self):
        with open(upload_path, 'rb') as file:
            files = {"file":file}
        file_manager.upload(
            file_type="model",
            file_path={"file_path":upload_uid},
            file=files,
        )
    # def test_download_model(self):
    #     with open(upload_path, 'rb') as file:
    #         files = {f'file':file}
    #         data={"file_path":upload_uid}
    #         file_manager.download(
    #             file_type="model",
    #             model_uid=model_uid,
    #             model_access_token=model_access_token,
    #         )


if __name__ == '__main__':
    unittest.main()
