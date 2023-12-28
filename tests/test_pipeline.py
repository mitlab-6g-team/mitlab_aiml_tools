import unittest
from uuid import uuid4
from mitlab_aiml_tools.auth.credential import CredentialServer
from mitlab_aiml_tools.pipeline.file import FileUtility

# File type
FILE_TYPE = 'model'

# Test data
MODEL_PATH = 'test_model.h5'
MODEL_DOWNLOAD_EXAMPLE_UID = '3c20d028-e24f-c9e1-5f73-faa8e47970d3'
ORIGINAL_DATASET_PATH = 'test_original_dataset.tar.gz'
ORIGINAL_DATASET_EXAMPLE_UID = '04460272-06c2-6492-a7dc-ebf50b08cc00'

credential_server = CredentialServer(
    host='192.168.190.150',
    port='40678',
    access_key='test',
    secret_key='test12345'
)

file_manager = FileUtility(credential_manager=credential_server)


class TestFileUtility(unittest.TestCase):

    def test_download(self):
        res = file_manager.download(
            file_type=FILE_TYPE, uid=MODEL_DOWNLOAD_EXAMPLE_UID
        )
        with open(MODEL_PATH, 'wb') as file:
            file.write(res.content)

    def test_upload(self):
        with open(MODEL_PATH, 'rb') as file:
            files = {f'{FILE_TYPE}_file': (MODEL_PATH, file)}
            file_manager.upload(
                file_type=FILE_TYPE,
                uid=uuid4(),
                file=files,
            )


if __name__ == '__main__':
    unittest.main()
