import unittest
from uuid import uuid4
from mitlab_aiml_tools.pipeline.file import FileUtility

# File type
FILE_TYPE = 'model'

# Test data
MODEL_PATH = 'test_model.h5'
MODEL_DOWNLOAD_EXAMPLE_UID = '3c20d028-e24f-c9e1-5f73-faa8e47970d3'
ORIGINAL_DATASET_PATH = 'test_original_dataset.tar.gz'
ORIGINAL_DATASET_EXAMPLE_UID = '04460272-06c2-6492-a7dc-ebf50b08cc00'


file_manager = FileUtility(file_type=FILE_TYPE)


class TestFileUtility(unittest.TestCase):

    def test_download(self):
        res = file_manager.download(uid=MODEL_DOWNLOAD_EXAMPLE_UID)
        with open(MODEL_PATH, 'wb') as file:
            file.write(res.content)
        print(res)

    def test_upload(self):
        with open(MODEL_PATH, 'rb') as file:
            files = {f'{FILE_TYPE}_file': (MODEL_PATH, file)}
            res = file_manager.upload(
                uid=uuid4(),
                file=files,
            )
        print(res)


if __name__ == '__main__':
    unittest.main()
