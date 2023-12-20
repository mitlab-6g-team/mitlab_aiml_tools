import unittest
from uuid import uuid4
from pipeline.file import FileUtility

# File type
FILE_TYPE = 'original_dataset'

# Test data
MODEL_PATH = 'test_model.h5'
MODEL_DOWNLOAD_EXAMPLE_UID = '3c20d028-e24f-c9e1-5f73-faa8e47970d3'
ORIGINAL_DATASET_PATH = 'test_orginal_dataset.tar.gz'
ORIGINAL_DATASET_UID = '04460272-06c2-6492-a7dc-ebf50b08cc00'


file_manager = FileUtility(actor_type=FILE_TYPE)


class TestFileUtility(unittest.TestCase):

    def test_download(self):
        res = file_manager.download(uid=ORIGINAL_DATASET_UID)
        with open(ORIGINAL_DATASET_PATH, 'wb') as file:
            file.write(res.content)
        print(res)

    def test_upload(self):
        with open(ORIGINAL_DATASET_PATH, 'rb') as file:
            files = {f'{FILE_TYPE}_file': (ORIGINAL_DATASET_PATH, file)}
            res = file_manager.upload(
                uid=uuid4(),
                file=files,
            )
        print(res)


if __name__ == '__main__':
    unittest.main()
