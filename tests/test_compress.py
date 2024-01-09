import unittest
from mitlab_aiml_tools.pipeline.compress import CompressionUtility

ARCHIVE_FILE_PATH = './tests/compressed_dataset.tar.gz'
SOURCE_FOLDER_PATH = './tests/dataset'
TARGET_FOLDER_PATH = './tests/decompressed_dataset'


class TestCompressUtility(unittest.TestCase):

    def test_compress(self):
        CompressionUtility.compress(
            source_path=SOURCE_FOLDER_PATH, zip_file_path=ARCHIVE_FILE_PATH)

    def test_decompress(self):
        CompressionUtility.decompress(
            zip_file_path=ARCHIVE_FILE_PATH, extract_path=TARGET_FOLDER_PATH)


if __name__ == '__main__':
    unittest.main()
